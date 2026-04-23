from app.models.conta import ContaCorrente
from app.services.persistence_manager import PersistenceManager
import os
from cryptography.fernet import Fernet
# from app.core.security import SecurityManager


# Tenta ler a chave de uma variável de ambiente. 
# Se não existir, ele gera uma (mas avisa que os dados antigos serão perdidos)
CHAVE_MESTRA = os.getenv("BANCO_CHAVE_MESTRA")

if not CHAVE_MESTRA:
    # Para fins de teste/desenvolvimento, geramos uma na hora
    CHAVE_MESTRA = Fernet.generate_key()
    print("⚠️  Aviso: Usando chave temporária. Dados salvos não serão lidos na próxima execução.")
else:
    # Converte a string da variável de ambiente para bytes
    CHAVE_MESTRA = CHAVE_MESTRA.encode()

def main():
    persistence = PersistenceManager(CHAVE_MESTRA)

    # Criando uma conta
    minha_conta = ContaCorrente("Victor", 1000.0, "senha123")

    # Salvando de forma segura
    persistence.salvar_conta(minha_conta)
    print("Dados da conta persistidos com sucesso (Criptografados).")

    # Simulando carregamento futuro
    dados_carregados = persistence.carregar_conta("Victor")
    print(f"Dados recuperados: {dados_carregados}")


if __name__ == "__main__":
    main()
