EXAMPLE OF JSON YOU CAN FIND IN INFO.TXT

Get all users:

Method: GET
Endpoint: /api/users/
Parameters: None

Get one user by id:

Method: GET
Endpoint: /api/users/<user_id>/
Parameters: user_id (integer)

Create a new user:

Method: POST
Endpoint: /api/users/new/
Parameters: JSON object with the following fields:
name (string)
email (string)
role (string)
is_admin (boolean)

Update a user:

Method: PUT
Endpoint: /api/users/<user_id>/update/
Parameters: JSON object with the following fields (all are optional):
name (string)
email (string)
role (string)
is_admin (boolean)

Patch a user:

Method: PATCH
Endpoint: /api/users/<user_id>/patch/
Parameters: JSON object with the following fields (all are optional):
name (string)
email (string)
role (string)
is_admin (boolean)

Delete a user:

Method: DELETE
Endpoint: /api/users/<user_id>/delete/
Parameters: user_id (integer)
