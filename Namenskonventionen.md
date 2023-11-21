Versionierung:
- https://www.xmatters.com/blog/blog-four-rest-api-versioning-strategies
- MAJOR.MINOR.PATCH in URI (e.g. http://www.example.com/api/v1/products)
- Query parameters (e.g. http://www.example.com/api/products?version=1)
- Request Header (e.g. Accepts-version: 1.0)
- Request Content-Type-Header (e.g. Accept: application/vnd.xm.device+json; version=1)

Namenskonventionen:
- https://restfulapi.net/resource-naming/
- Always use nouns rather than verbs 
- Use plural nouns to represent collections
- Maintain a consistent structure in the API
- Use a structured approach for nested resources
- Avoid long URIs

Korrekter Einsatz der HTTP-Methoden:
- POST: Create new resources
- GET: Read resources
- PUT: Update entire resources
- PATCH: Update part of a resource
- DELETE: Delete resources

Beispiel: PUT vs PATCH

PUT /users/1
{
    "username": "skwee357",
    "email": "skwee357@gmail.com"       // new email address
}

PATCH /users/1
{
    "email": "skwee357@gmail.com"       // new email address
}
