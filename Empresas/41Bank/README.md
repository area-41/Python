# 41Bank

### 🏦 Banking System Core (Python)
Sistema bancário robusto desenvolvido em Python, focado em concorrência segura (thread-safety) e proteção de dados sensíveis. 
O projeto aplica princípios de Programação Orientada a Objetos (POO), criptografia AES para persistência e hashing para credenciais.

### Arquitetura e Concorrência
O sistema foi desenhado para suportar operações multithread, simulando um ambiente real onde múltiplos acessos à mesma conta podem ocorrer simultaneamente.

#### Gestão de Threads e Locks
Para garantir a integridade dos saldos, utilizamos primitivas de sincronização do módulo threading:

#### Locks por Instância: Cada objeto Conta possui seu próprio threading.Lock. Isso garante que duas threads não alterem o saldo da mesma conta ao mesmo tempo.

#### Prevenção de Deadlock: Nas transferências, implementamos uma estratégia de ordenação de recursos. Sempre adquirimos os locks seguindo a ordem crescente do ID de memória dos objetos. Isso evita que a Thread A (esperando Conta 2) e a Thread B (esperando Conta 1) entrem em um impasse eterno.

#### Instruções de Segurança
O sistema não armazena informações sensíveis em texto claro. Utilizamos duas camadas de proteção:

1. Hashing de Senhas
As senhas dos usuários passam por um processo de hashing SHA-256. Diferente da criptografia, o hash é unidirecional; o sistema compara o hash da tentativa de login com o hash armazenado, garantindo que nem mesmo os administradores do banco de dados conheçam a senha real.

2. Criptografia de Arquivos (AES-128)
Os arquivos de persistência (.dat) são protegidos via Fernet (criptografia simétrica).

Como gerar sua chave secreta:
Para que o sistema funcione, você deve gerar uma chave e configurá-la como variável de ambiente ou injetá-la no PersistenceManager:

Python

    from cryptography.fernet import Fernet

### Gere uma chave segura
    chave = Fernet.generate_key()
    print(chave.decode()) # Guarde isso com segurança!


#### Documentação da API
    Conta(ABC) (Classe Abstrata)
    Classe base que define o comportamento de uma conta bancária.
    
    _titular (protegido): Nome do proprietário.
    
    __saldo (privado): Saldo atual (acessível via property saldo).
    
    transferir(valor, destino): Executa a lógica de movimentação entre contas com lock duplo.
    
    calcular_taxa(): Método abstrato para definir custos de operação.
    
    ContaCorrente(Conta)
    Implementa taxa de operação padrão.
    
    Permite limites de cheque especial (opcional).
    
    PersistenceManager
    salvar_conta(conta): Converte o objeto para JSON, criptografa com AES e grava em data/.
    
    carregar_conta(titular): Localiza o arquivo, decriptografa e reconstrói o estado do objeto.

#### Como Executar
Instale as dependências:

    pip install cryptography
Execute os testes de concorrência:

    python main.py
    
#### Próximos Passos (Roadmap)
[ ] Implementar JWT para sessões de usuário.

[ ] Migrar persistência de arquivos flat para SQLite criptografado.

[ ] Interface via FastAPI para operações remotas.
