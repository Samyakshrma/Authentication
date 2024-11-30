# Define user roles
ROLES = {
    "admin": ["create", "update", "delete"],
    "user": ["read"],
}

# Function to check permissions based on role
def check_permission(role: str, action: str) -> bool:
    return action in ROLES.get(role, [])
