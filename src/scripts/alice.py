import base64
import datetime
import sys
import json
import os
import shutil
from pathlib import Path

import maya

from nucypher.characters.lawful import Bob, Ursula
from nucypher.config.characters import AliceConfiguration
from nucypher.config.constants import TEMPORARY_DOMAIN
from nucypher.utilities.logging import GlobalLoggerSettings


GlobalLoggerSettings.start_console_logging()

TEMP_ALICE_DIR = Path('/', 'tmp', 'heartbeat-demo-alice')



try:
    SEEDNODE_URI = sys.argv[1]
except IndexError:
    SEEDNODE_URI = "localhost:11500"

POLICY_FILENAME = "policy-metadata.json"



passphrase = "TEST_ALICIA_INSECURE_DEVELOPMENT_PASSWORD"


shutil.rmtree(TEMP_ALICE_DIR, ignore_errors=True)

ursula = Ursula.from_seed_and_stake_info(seed_uri=SEEDNODE_URI,
                                         federated_only=True,
                                         minimum_stake=0)

alice_config = AliceConfiguration(
    config_root=TEMP_ALICE_DIR,
    domain=TEMPORARY_DOMAIN,
    known_nodes={ursula},
    start_learning_now=False,
    federated_only=True,
    learn_on_same_thread=True,
)

alice_config.initialize(password=passphrase)

alice_config.keystore.unlock(password=passphrase)
alicia = alice_config.produce()


alice_config_file = alice_config.to_configuration_file()

alicia.start_learning_loop(now=True)
label = "heart-data-❤️-"+os.urandom(4).hex()
label = label.encode()

policy_pubkey = alicia.get_policy_encrypting_key_from_label(label)

print("The policy public key for "
      "label '{}' is {}".format(label.decode("utf-8"), bytes(policy_pubkey).hex()))

import heart_monitor
heart_monitor.generate_heart_rate_samples(policy_pubkey,
                                          samples=50,
                                          save_as_file=True)


from doctor_keys import get_doctor_pubkeys
doctor_pubkeys = get_doctor_pubkeys()


doctor_strange = Bob.from_public_keys(verifying_key=doctor_pubkeys['sig'],
                                      encrypting_key=doctor_pubkeys['enc'],
                                      federated_only=True)

policy_end_datetime = maya.now() + datetime.timedelta(days=1)

threshold, shares = 2, 3


print("Creating access policy for the Doctor...")
policy = alicia.grant(bob=doctor_strange,
                      label=label,
                      threshold=threshold,
                      shares=shares,
                      expiration=policy_end_datetime)
print("Done!")


policy_info = {
    "policy_pubkey": bytes(policy.public_key).hex(),
    "alice_sig_pubkey": bytes(alicia.stamp).hex(),
    "label": label.decode("utf-8"),
    "treasure_map": base64.b64encode(bytes(policy.treasure_map)).decode()
}

filename = POLICY_FILENAME
with open(filename, 'w') as f:
    json.dump(policy_info, f)