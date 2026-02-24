import hashlib
import secrets


class SecurityService:
    @classmethod
    def hash_password(cls, password: str) -> str:
        """
        Cria um hash seguro usando SHA-256 e um Salt aleatório.
        Retorno: 'salt:hash'
        """
        # Gerar um salt aleatório para cada senha
        salt = secrets.token_hex(8)

        # Combinar a senha com o salt e geramos o hash
        hash_obj = hashlib.sha256((salt + password).encode())
        hash_hex = hash_obj.hexdigest()

        return f"{salt}:{hash_hex}"

    @classmethod
    def verify_password(cls, stored_password: str, provided_password: str) -> bool:
        """
        Verifica se a senha digitada bate com o que está no JSON.
        """
        # Separar o salt do hash que estava guardado
        try:
            salt, stored_hash = stored_password.split(":")

            # Gerar um novo hash com a senha digitada e o MESMO salt
            current_hash = hashlib.sha256((salt + provided_password).encode()).hexdigest()

            # Comparar os dois hashes
            return current_hash == stored_hash
        except ValueError:
            return False