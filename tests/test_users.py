import pytest
from jose import jwt
from app import schemas
from app.config import settings 
    
# def test_root(client):
#     res = client.get("/")
#     print(res.json().get("message"))
#     assert res.json().get("message") == "Bind mount works!"
#     assert res.status_code == 200


    
def test_create_user(client):   # client refers to the fixture (must have the same name of the fixture)
    res = client.post("/users/", json={"email":"hello@gmail.com", "password":"1234"})
    new_user = schemas.User(**res.json())
    assert new_user.email == "hello@gmail.com"      # Consider the fields available from the schema returned
    assert new_user.id == 1
    assert res.status_code == 201
    
def test_login_user(test_user, client): # This test depends on two fixtures 
    res = client.post("/login", data={"username":test_user["email"], "password":test_user["password"]})
    login_res = schemas.Token(**res.json()) # Output schema used in the router auth
    payload = jwt.decode(login_res.access_token,
                         settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200
    
# def test_incorrect_login(test_user, client):
#     res = client.post(
#         "/login", data={"username":test_user["email"], "password":"worng-password"})

#     assert res.status_code == 403

# Use a user that exists in the db
@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', '12345', 403),
    ('nicolas@correo.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, '12345', 403),
    ('nicolas@correo.com', None, 403)
])
def test_incorrect_login(client, email, password, status_code):
    res = client.post(
        "/login", data={"username": email, "password": password})

    assert res.status_code == status_code