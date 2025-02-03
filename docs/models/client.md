# Client Model

The Client model represents API clients that are authorized to use the V2V Email Server. Each client is assigned a unique API key and has associated metadata and rate limiting configuration.

## Schema

| Field         | Type    | Description                                        | Constraints                    |
|--------------|---------|----------------------------------------------------|---------------------------------|
| id           | UUID    | Unique identifier for the client                   | Primary key, auto-generated     |
| name         | String  | Name of the client organization                    | Required, max length 100        |
| api_key      | String  | Unique API key for authentication                  | Required, unique, indexed       |
| website_url  | String  | Client's website URL                              | Required, max length 255        |
| contact_email| String  | Contact email for the client                      | Required, max length 255        |
| is_active    | Boolean | Whether the client is currently active            | Default: true                   |
| rate_limit   | Integer | Maximum requests per minute allowed                | Default: 60                     |
| description  | String  | Optional description of the client                 | Optional, max length 500        |

## Usage

### Creating a New Client

```python
from app.models.auth.client import Client

client = Client(
    name="Example Corp",
    api_key="example_key_123",
    website_url="https://example.com",
    contact_email="api@example.com",
    rate_limit=100,  # Optional: override default rate limit
    description="Example corporation API client"  # Optional
)
```

### Authentication

The `api_key` field is used for authenticating API requests. Each request must include this key in the headers. The field is indexed for fast lookups during request authentication.

### Rate Limiting

Each client has a configurable rate limit that defaults to 60 requests per minute. This can be adjusted per client based on their needs and agreement level.

### Security Considerations

- API keys should be kept secure and never exposed in client-side code
- Keys should be rotated periodically or when compromised
- Deactivate clients by setting `is_active` to False instead of deleting records

## Database Migrations

When making changes to the Client model, ensure to:
1. Create appropriate Alembic migrations
2. Update this documentation
3. Update any related API endpoints
4. Update the test suite

## Related Components

- Authentication middleware
- Rate limiting middleware
- Client management API endpoints
- API key generation utilities 