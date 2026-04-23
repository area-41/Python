from app.models.conta import ContaCorrente
from app.services.persistence_manager import PersistenceManager
import os
from cryptography.fernet import Fernet
# from app.core.security import SecurityManager

import threading
from app.models.conta import ContaCorrente
from app.services.persistence_manager import PersistenceManager
from app.services.banco_service import BancoService
from cryptography.fernet import Fernet

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

def realizar_transacoes_em_massa(origem, destino, valor, repeticoes):
    """Simula um usuário realizando várias transferências."""
    for _ in range(repeticoes):
        BancoService.transferir(origem, destino, valor)


def main():
    # 1. Configuração Inicial
    chave = Fernet.generate_key()
    persistence = PersistenceManager(chave)
    
    conta_victor = ContaCorrente("Victor", 2000.0, "senha123")
    conta_destino = ContaCorrente("Investimentos", 500.0, "senha456")

    # 2. Configuração do Teste de Estresse
    # 10 threads enviando 10 reais cada, 50 vezes por thread.
    # Total esperado: 10 * 50 * 10 = 5000 reais (mas o saldo é 2000!)
    # Isso testará se o sistema impede saldo insuficiente sob pressão.
    threads = []
    num_threads = 10
    transferencias_por_thread = 50
    valor_transferencia = 10 

    print(f"🚀 Iniciando {num_threads} threads de transferência simultâneas...")

    for i in range(num_threads):
        t = threading.Thread(
            target=realizar_transacoes_em_massa, 
            args=(conta_victor, conta_destino, valor_transferencia, transferencias_por_thread)
        )
        threads.append(t)
        t.start()

    # 3. Aguardar todas as threads finalizarem (Join)
    for t in threads:
        t.join()

    print("\n✅ Transações finalizadas.")
    print(f"Saldo Final Victor: {conta_victor.saldo}")
    print(f"Saldo Final Investimentos: {conta_destino.saldo}")

    # 4. Persistência Final do Estado Consistente
    persistence.salvar_conta(conta_victor)
    persistence.salvar_conta(conta_destino)
    print("\n💾 Estados finais persistidos com criptografia.")

if __name__ == "__main__":
    main()
