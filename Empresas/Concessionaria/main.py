from app.modelos.carro import Carro
from app.modelos.moto import Moto
from app.servicos.estoque import GerenciadorEstoque
from app.utilitarios.validadores import ValidadorVeiculo


def exibir_titulo(texto):
    print(f"\n{'='*10} {texto} {'='*10}")


def executar_demonstracao():
    """
    Usado para orquestrar a demonstração
    """

    # 1. Instanciando o Serviço
    estoque = GerenciadorEstoque()

    exibir_titulo("CADASTRO DE VEÍCULOS")

    # 2. Criando Objetos (Demonstrando Herança e Polimorfismo)
    try:
        # Carro: marca, modelo, preco, portas
        corolla = Carro("Toyota", "Corolla", 150000.00, 4)
        # Moto: marca, modelo, preco, cilindradas
        ninja = Moto("Kawasaki", "Ninja 400", 35000.00, 400)

        estoque.adicionar_veiculo(corolla)
        estoque.adicionar_veiculo(ninja)
    except ValueError as e:
        print(f"❌ Erro ao cadastrar: {e}")

    # 3. Demonstrando Validação Independente (Utilitários)
    exibir_titulo("VALIDAÇÃO DE DADOS")
    placa_teste = "ABC1D23"
    if ValidadorVeiculo.validar_placa(placa_teste):
        print(f"✅ A placa {placa_teste} é válida (Padrão Mercosul).")

    # 4. Demonstrando Encapsulamento e Polimorfismo (Cálculo de IPVA)
    exibir_titulo("RELATÓRIO DE ESTOQUE E TAXAS")
    for veiculo in [corolla, ninja]:
        # O método calcular_ipva se comporta de forma diferente para cada objeto (Polimorfismo)
        print(f"Veículo: {veiculo.modelo} | Preço: {veiculo.preco} | IPVA: R$ {veiculo.calcular_ipva():.2f}")

    # 5. Exibindo resumo final
    print("\n--- Relatório de Estoque ---")
    for item in estoque.listar_estoque():
        print(item)

    print(f"\nTotal de veículos no estoque: {estoque.total_em_estoque}")


if __name__ == "__main__":
    executar_demonstracao()
