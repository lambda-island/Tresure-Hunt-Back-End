# back-end

base url: https://lambda-island.herokuapp.com/

provide "username" and "password" to baseurl/api/auth to recieve jwt token

{
  "username": "example_name",
  "password": "examplePassword"
}

for any requests to main endpoints provide auth header

Headers = {"Authorizations": "Bearer {jwt token here}"}
