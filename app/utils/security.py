from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    """
    Hashes the password using a secure hashing algorithm.
    """
    return generate_password_hash(password)

def verify_password(password, password_hash):
    """
    Verifies a password against its hash.
    """
    return check_password_hash(password_hash, password)