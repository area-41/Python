from cryptography.fernet import Fernet
import hashlib


class SecurityManager:
    """Gera o hashing de senhas e criptografia de arquivos."""

    @staticmethod
    def hash_password(password: str) -> str:
        # No mundo real, use bcrypt ou argon2
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def encrypt_data(data: str, key: bytes) -> bytes:
        f = Fernet(key)
        return f.encrypt(data.encode())

    @staticmethod
    def generate_key():
        """Gere esta chave uma única vez e guarde-a em uma variável de ambiente."""
        return Fernet.generate_key()

    @staticmethod
    def encrypt_data(data: str, key: bytes) -> bytes:
        f = Fernet(key)
        return f.encrypt(data.encode())

"""
Para senhas, nunca usamos criptografia reversível, mas sim Hashing (como Argon2 ou BCrypt). 
Para dados sensíveis em arquivos, usamos Fernet (AES).
 """
