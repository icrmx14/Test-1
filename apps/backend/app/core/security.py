"""Security stubs for JWT, MFA, and token management."""


def create_access_token(data: dict) -> str:
    """Create a JWT access token."""
    pass


def verify_access_token(token: str) -> dict:
    """Verify and decode a JWT access token."""
    pass


def hash_password(password: str) -> str:
    """Hash a plaintext password."""
    pass


def verify_password(plain: str, hashed: str) -> bool:
    """Verify a password against its hash."""
    pass


def generate_mfa_secret() -> str:
    """Generate a new MFA secret."""
    pass


def verify_mfa_token(secret: str, token: str) -> bool:
    """Verify an MFA TOTP token."""
    pass
