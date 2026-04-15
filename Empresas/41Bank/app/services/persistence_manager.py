import json
import os
from app.core.security import SecurityManager


class PersistenceManager:
    """
    Responsável por transformar os dados da conta em um dicionário,
    criptografar a string JSON resultante e salvar no disco.
    """
    def __init__(self, key: bytes):
        self.key = key
        self.storage_path = "data/accounts/"
        os.makedirs(self.storage_path, exist_ok=True)

    def salvar_conta(self, conta_obj):
        """Serializa o objeto para JSON e salva criptografado."""
        file_path = os.path.join(self.storage_path, f"{conta_obj.titular}.dat")

        # 1. Transformar dados em dicionário
        dados = {
            "titular": conta_obj.titular,
            "saldo": conta_obj.saldo,
            "tipo": conta_obj.__class__.__name__
        }

        # 2. Converter para string JSON
        json_str = json.dumps(dados)

        # 3. Criptografar
        encrypted_data = SecurityManager.encrypt_data(json_str, self.key)

        # 4. Escrita atômica no disco
        with open(file_path, "wb") as f:
            f.write(encrypted_data)

    def carregar_conta(self, titular: str):
        """Lê o arquivo, decriptografa e retorna os dados."""
        file_path = os.path.join(self.storage_path, f"{titular}.dat")

        if not os.path.exists(file_path):
            return None

        with open(file_path, "rb") as f:
            encrypted_data = f.read()

        # Decriptografia (usa a mesma lógica do SecurityManager)
        from cryptography.fernet import Fernet
        f_obj = Fernet(self.key)
        json_str = f_obj.decrypt(encrypted_data).decode()

        return json.loads(json_str)
