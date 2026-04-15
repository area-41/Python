from app.models.conta import ContaCorrente

def test_criacao_conta_saldo_positivo():
    conta = ContaCorrente("Victor", 1000, "hash_senha")
    assert conta.saldo == 1000

def test_saque_protegido():
    # Aqui você testaria se o saldo privado não é acessado diretamente
    # e se a lógica de alteração de saldo funciona.
    pass
