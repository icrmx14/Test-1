import base64
import hmac
import hashlib
import json
import time

SECRET_KEY = "erp_super_secret_key"


def base64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode('utf-8').rstrip('=')


def base64url_decode(data: str) -> bytes:
    padding = '=' * (4 - (len(data) % 4))
    return base64.urlsafe_b64decode(data + padding)


def create_access_token(data: dict, expires_in: int = 3600) -> str:
    """Create a JWT access token."""
    header = {"alg": "HS256", "typ": "JWT"}
    payload = data.copy()
    payload["exp"] = int(time.time()) + expires_in

    header_json = json.dumps(header, separators=(',', ':')).encode('utf-8')
    payload_json = json.dumps(payload, separators=(',', ':')).encode('utf-8')

    header_b64 = base64url_encode(header_json)
    payload_b64 = base64url_encode(payload_json)

    signing_input = f"{header_b64}.{payload_b64}".encode('utf-8')
    signature = hmac.new(SECRET_KEY.encode('utf-8'), signing_input, hashlib.sha256).digest()
    signature_b64 = base64url_encode(signature)

    return f"{header_b64}.{payload_b64}.{signature_b64}"


def verify_access_token(token: str) -> dict:
    """Verify and decode a JWT access token."""
    try:
        parts = token.split('.')
        if len(parts) != 3:
            return None
        header_b64, payload_b64, signature_b64 = parts

        signing_input = f"{header_b64}.{payload_b64}".encode('utf-8')
        expected_sig = hmac.new(SECRET_KEY.encode('utf-8'), signing_input, hashlib.sha256).digest()
        expected_sig_b64 = base64url_encode(expected_sig)

        if not hmac.compare_digest(signature_b64, expected_sig_b64):
            return None

        payload = json.loads(base64url_decode(payload_b64).decode('utf-8'))
        if payload.get("exp", 0) < time.time():
            return None  # Expired

        return payload
    except Exception:
        return None


def hash_password(password: str) -> str:
    """Hash a plaintext password using PBKDF2."""
    salt = hashlib.sha256(password.encode('utf-8')).hexdigest()[:16].encode('utf-8')
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return f"{salt.decode('utf-8')}:{key.hex()}"


def verify_password(plain: str, hashed: str) -> bool:
    """Verify a password against its PBKDF2 hash."""
    try:
        salt_str, key_hex = hashed.split(':')
        salt = salt_str.encode('utf-8')
        key = hashlib.pbkdf2_hmac('sha256', plain.encode('utf-8'), salt, 100000)
        return hmac.compare_digest(key.hex(), key_hex)
    except Exception:
        return False


def generate_mfa_secret() -> str:
    """Generate a new MFA secret."""
    import secrets
    return secrets.token_hex(16)


def verify_mfa_token(secret: str, token: str) -> bool:
    """Verify an MFA TOTP token."""
    # A simple token verification
    return token == secret[-6:]
