from app.modelos.veiculo import Veiculo


class GerenciadorEstoque:
    """
    Classe que gerencia os objetos (Carros/Motos) sem expor a lista interna diretamente,
    protegendo a integridade dos dados
    """

    def __init__(self):
        # Atributo privado (__): impede acesso externo direto
        self.__veiculos = []

    def adicionar_veiculo(self, veiculo: Veiculo):
        """Adiciona um veículo validando se ele herda de Veiculo."""
        if isinstance(veiculo, Veiculo):
            self.__veiculos.append(veiculo)
            print(f"✅ {veiculo.modelo} adicionado com sucesso!")
        else:
            raise TypeError("Apenas objetos do tipo Veiculo podem ser adicionados.")

    def listar_estoque(self):
        """Retorna uma representação formatada do estoque."""
        if not self.__veiculos:
            return "O estoque está vazio."

        return [f"{v.marca} {v.modelo} - Preço: {v.preco}" for v in self.__veiculos]

    def buscar_por_modelo(self, modelo: str):
        """Exemplo de busca usando List Comprehension."""
        return [v for v in self.__veiculos if modelo.lower() in v.modelo.lower()]

    @property
    def total_em_estoque(self):
        """Retorna a quantidade de itens (uso de Getter)."""
        return len(self.__veiculos)
