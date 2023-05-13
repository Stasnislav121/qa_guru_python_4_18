from voluptuous import Schema, PREVENT_EXTRA, ALLOW_EXTRA

user_schema = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

single_user_schema = Schema(
    {
        "data": user_schema,
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)



resource_schema = Schema(
    {
        "id": int,
        "name": str,
        "year": int,
        "color": str,
        "pantone_value": str
    },
    extra=ALLOW_EXTRA,
    required=True
)

list_resources_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [resource_schema],
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)


create_user_schema = Schema(
    {
        "name": "morpheus",
        "job": "leader",
        "id": str,
        "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

registration_successful_schema = Schema(
    {
        "id": int,
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

registration_unsuccessful_schema = Schema(
    {
        "error": "Missing password"
    },
    extra=PREVENT_EXTRA,
    required=True
)

delayed_response_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [user_schema],
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)