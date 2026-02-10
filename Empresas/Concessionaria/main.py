from app.modelos.carro import Carro
from app.modelos.moto import Moto
from app.servicos.estoque import GerenciadorEstoque


def executar_demonstracao():
    """
    Usado para orquestrar a demonstração
    """

    # Instanciando o estoque
    estoque = GerenciadorEstoque()

    # Criando instâncias de Carro (Herança e Encapsulamento)
    carro1 = Carro("Toyota", "Corolla", 150000, 4)
    carro2 = Carro("Honda", "Civic", 145000, 4)
    cb500 = Moto("Honda", "CB 500", 40000, 500)

    # Adicionando ao estoque
    estoque.adicionar_veiculo(carro1)
    estoque.adicionar_veiculo(carro2)
    estoque.adicionar_veiculo(cb500)

    print("\n--- Detalhes do IPVA Estimado ---")
    print(f"IPVA {carro1.modelo}: R$ {carro1.calcular_ipva():.2f}")
    print(f"IPVA {carro2.modelo}: R$ {carro2.calcular_ipva():.2f}")
    print(f"IPVA {cb500.modelo}: R$ {cb500.calcular_ipva():.2f}")

    # Exibindo resultados
    print("\n--- Relatório de Estoque ---")
    for item in estoque.listar_estoque():
        print(item)

    print(f"\nTotal de veículos: {estoque.total_em_estoque}")


if __name__ == "__main__":
    executar_demonstracao()
