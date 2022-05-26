---
slug: /stgsdk_err
id: idstgsdkerr
title: Storage
---

| Error	| Description |
| ----  | ------ |
| unauthorized_user	| Trying to download a file which is neither owned by you nor shared with you. |
| only_file_owner	|	Only the owner of the file have access to the function i.e, either to delete, revoke or transfer file. |
| non_active_user	|	Your account is either disabled or deleted. |
| non_registered_user	|	Your account is not registered for the app. |
| only_factory_contract	|	Only factory contract can set the app level limit i.e, storage and bandwidth. |
| no_app_space	|	Your current app's storage or bandwidth limit has been consumed. |
| no_user_space	|	You have already consumed your storage or bandwidth limit. |
| non_trusted_forwarder_or_factory	|	For meta-transaction, transaction should happen from valid factory or forwarder contract. |
| file_already_uploaded	|	You cannot upload a file that is already uploaded by a different user address.
| zero_file_size	|	Your file size must not be null while uploading. |
| only_storage_node	|	Only assigned storage node has access to the function. |
| zero_validity	|	Validity must be a non-zero value as it is the access specifier of the duration for which file sharing is enabled. |
| avoid_sharing_file_themselves | Avoid sharing file to themselves. |
| already_shared | file is already shared with the user. |
| file_not_found	|	File with the specified DID does not exist in the Arcana Store. |
| no_file_access | Access not granted by current user. |
| invalid_address | address provided is not valid or zero address. |
| file_ownership_transfer_to_same_address | New owner cannot be same as old owner while changing file owner. |
| invalid_app_ID	|	Make sure you specify the correct app ID assigned to dApp after configuration at the dashboard https://dashboard.arcana.network/|
| app_not_found	|	Configure the app at https://dashboard.arcana.network/. |
| only_gateway_node	|	Only gateway node has access to the function. |
| invalid_function_signature	|	Meta-transaction failed. The function you are trying to call does not exist. Check the function signature. |
