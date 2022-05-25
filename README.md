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
| non_trusted_farwarder_or_factory	|	For meta-transaction, transaction should happen from valid factory or forwarder contract. |
| file_already_uploaded	|	You cannot upload a file that is already uploaded by a different user address
| zero_file_size	|	Your file size must not be null while uploading. |
| only_storage_node	|	Only assigned storage node has access to the function. |
| only_file_owner	|	You are not the file owner thus action cannot be done. Kindly verify your account address. |
| zero_validity	|	Validity is the access specifier and cannot be zero while sharing a file. |
| already_active_user	|	Your account was not deleted to reactivate. |
| invalid_app_ID	|	Use a valid app ID. Try configuring the app at https://dashboard.arcana.network/ to get app ID. |
| app_not_found	|	Configure the app at https://dashboard.arcana.network/. |
| only_gateway_node	|	Only gateway node has access to the function. |
| file_not_found	|	File not found. |
| invalid_function_signature	|	Meta-transaction failed. The function you are trying to call does not exist. Check the function signature. |
