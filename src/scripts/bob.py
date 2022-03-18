import base64
import json
from pathlib import Path
from timeit import default_timer as timer

import maya
import msgpack
import shutil
import sys

from nucypher_core import MessageKit, EncryptedTreasureMap
from nucypher_core.umbral import PublicKey

from nucypher.characters.lawful import Bob, Enrico, Ursula
from nucypher.config.constants import TEMPORARY_DOMAIN
from nucypher.crypto.keypairs import DecryptingKeypair, SigningKeypair
from nucypher.crypto.powers import DecryptingPower, SigningPower
from nucypher.network.middleware import RestMiddleware
from nucypher.utilities.logging import GlobalLoggerSettings

GlobalLoggerSettings.start_console_logging()


try:
    SEEDNODE_URI = sys.argv[1]
except IndexError:
    SEEDNODE_URI = "localhost:11500"


TEMP_DOCTOR_DIR = Path(__file__).parent.absolute() / "doctor-files"


shutil.rmtree(TEMP_DOCTOR_DIR, ignore_errors=True)

ursula = Ursula.from_seed_and_stake_info(seed_uri=SEEDNODE_URI,
                                         federated_only=True,
                                         minimum_stake=0)

from doctor_keys import get_doctor_privkeys

doctor_keys = get_doctor_privkeys()

bob_enc_keypair = DecryptingKeypair(private_key=doctor_keys["enc"])
bob_sig_keypair = SigningKeypair(private_key=doctor_keys["sig"])
enc_power = DecryptingPower(keypair=bob_enc_keypair)
sig_power = SigningPower(keypair=bob_sig_keypair)
power_ups = [enc_power, sig_power]

print("Creating the Doctor ...")

doctor = Bob(
    domain=TEMPORARY_DOMAIN,
    federated_only=True,
    crypto_power_ups=power_ups,
    start_learning_now=True,
    abort_on_learning_error=True,
    known_nodes=[ursula],
    save_metadata=False,
    network_middleware=RestMiddleware(),
)

print("Doctor = ", doctor)

with open("policy-metadata.json", 'r') as f:
    policy_data = json.load(f)

policy_pubkey = PublicKey.from_bytes(bytes.fromhex(policy_data["policy_pubkey"]))
alices_sig_pubkey = PublicKey.from_bytes(bytes.fromhex(policy_data["alice_sig_pubkey"]))
label = policy_data["label"].encode()
treasure_map = EncryptedTreasureMap.from_bytes(base64.b64decode(policy_data["treasure_map"].encode()))


data = msgpack.load(open("heart_data.msgpack", "rb"), raw=False)
message_kits = (MessageKit.from_bytes(k) for k in data['kits'])


for message_kit in message_kits:
    start = timer()
    retrieved_plaintexts = doctor.retrieve_and_decrypt(
        [message_kit],
        alice_verifying_key=alices_sig_pubkey,
        encrypted_treasure_map=treasure_map
    )
    end = timer()

    plaintext = msgpack.loads(retrieved_plaintexts[0], raw=False)


    heart_rate = plaintext['heart_rate']
    timestamp = maya.MayaDT(plaintext['timestamp'])

    terminal_size = shutil.get_terminal_size().columns
    max_width = min(terminal_size, 120)
    columns = max_width - 12 - 27
    scale = columns / 40
    scaled_heart_rate = int(scale * (heart_rate - 60))
    retrieval_time = "Retrieval time: {:8.2f} ms".format(1000 * (end - start))
    line = ("-" * scaled_heart_rate) + "❤︎ ({} BPM)".format(heart_rate)
    line = line.ljust(max_width - 27, " ") + retrieval_time
    print(line)