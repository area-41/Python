import os
import click
from app.models.conta import ContaCorrente
from app.services.persistence_manager import PersistenceManager
from cryptography.fernet import Fernet

# 1. Configuração da Chave
CHAVE_MESTRA = os.getenv("BANCO_CHAVE_MESTRA")

if not CHAVE_MESTRA:
    # Geramos uma temporária se não houver no ambiente
    CHAVE_MESTRA = Fernet.generate_key()
    # Removemos o print daqui para não sujar o output da CLI toda hora
else:
    CHAVE_MESTRA = CHAVE_MESTRA.encode()

# 2. Instanciamos a persistência usando a variável correta: CHAVE_MESTRA
persistence = PersistenceManager(CHAVE_MESTRA)

@click.group()
def bank():
    """Sistema Bancário 41Bank - Gerenciamento via CLI."""
    pass

@bank.command()
@click.argument('nome')
@click.option('--saldo', default=0.0, type=float, help='Saldo inicial da conta.')
def criar(nome, saldo):
    """Cria uma nova conta e persiste no disco."""
    # Note: Usamos o titular via property ou _titular conforme ajustamos antes
    nova_conta = ContaCorrente(nome, saldo, "senha_padrao")
    persistence.salvar_conta(nova_conta)
    click.echo(f"✅ Conta de {nome} criada com sucesso!")

@bank.command()
@click.argument('nome')
def saldo(nome):
    """Consulta o saldo de uma conta criptografada."""
    dados = persistence.carregar_conta(nome)
    if dados:
        click.echo(f"💰 Saldo de {nome}: R$ {dados['saldo']:.2f}")
    else:
        click.echo(f"❌ Conta '{nome}' não encontrada.")

@bank.command()
@click.argument('origem')
@click.argument('destino')
@click.argument('valor', type=float)
def transferir(origem, destino, valor):
    """Realiza transferência entre duas contas criptografadas."""
    # 1. Carrega os dados das contas
    # 2. Instancia os objetos ContaCorrente
    # 3. Chama o BancoService.transferir()
    # 4. Salva o novo estado de ambas as contas
    click.echo(f"💸 Transferindo R$ {valor} de {origem} para {destino}...")

if __name__ == "__main__":
    bank()