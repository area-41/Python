from app.models.conta import ContaCorrente
from app.services.persistence_manager import PersistenceManager
# from app.core.security import SecurityManager

# No mundo real, a chave viria de um .env ou Vault
CHAVE_MESTRA = b'SuaChaveFernetGeradaPreviamente==='


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
