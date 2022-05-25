# ``` Decentralized Secure File Storage. ```

---
slug: /stgsdk_err
id: idstgsdkerr
title: Storage
---

| Code	| Message	| Reason |
| ----  | ------- | ------ |
| no_file_access	|You can't download this file. | Trying to download a file which is neither owned by you nor shared with you. |
| only_file_owner	| This function can only be called by file owner. |	Only owner of the file have access to the function i.e, either to delete, revoke or transfer file. |
| non_active_user	| User is not active. |	Your account is either disabled or deleted. |
| non_registered_user	| User not registered for the app. |	Your account is not registered for the app. |
| only_factory_contract	| Only factory contract can call this function. |	Only factory contract can set the app level limit i.e, storage and bandwidth. |
| no_app_space	| No space left for app. |	Your current app's storage or bandwidth limit has been consumed. |
| no_user_space	| No space left for user. |	You have already consumed your storage or bandwidth limit. |
| not_a_trusted_farwarder_nor_factory	| Not a trusted forwarder nor factory contract. |	For meta transaction, transaction should happen from valid factory or farwarder contract. |
| file_already_uploaded	| Owner already exist for this file. |	You cannot upload a file that is already uploaded by different user address
| null_file_size	| Should not be 0. |	Your file size must not be null while uploading. |
| only_storage_node	| Function can only be called by the assigned storage node. |	Only assigned storage node has access to the function. |
| only_file_owner	| Not file owner. |	You are not the file owner thus action cannot be done. Kindly verify your account address. |
| validity	| Validity must be non zero. |	Validity is the access specifier and cannot be zero while sharing a file. |
| TRANSACTION	| User was not deleted to reactivate. |	Your account was not deleted to reactivate. |
| TRANSACTION	| An app already created with this Id. |	Use a valid app ID. Try configuring the app at https://dashboard.arcana.network/ to get app ID. |
| TRANSACTION	| App calling the function is not registered. |	configure the app at https://dashboard.arcana.network/. |
| TRANSACTION	| Please add some nodes to authenticate user. |
| TRANSACTION	| Function can only called by nodes. |
| TRANSACTION	| Already voted. |
| TRANSACTION	| Only gateway node can call this function. |	Only gateway node has access to the function. |
| TRANSACTION	| File must be uploaded before downloading it. |	File not found. |
| TRANSACTION	| MinimalForwarder: signature does not match request. |	Meta transaction failed. The function you are trying to call does not exists. check the function signature. |
