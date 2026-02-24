# Uso de Métodos Privados

class Lampada:
    def __init__(self, marca="Philips"):
        self.__ligada = False
        self.__queimada = False
        self.__vida_util = 5  # A lâmpada aguenta 5 "ligadas" antes de ter risco real
        self.marca = marca

    def ligar(self):
        if not self.__esta_queimada():
            if self.__vida_util > 0:
                self.__ligada = True
                print('A lâmpada foi ligada.')
                self.__vida_util -= 1
            else:
                print('A lâmpada está queimada e não pode ser ligada.')
        else:
            print('A lâmpada está queimada e não pode ser ligada.')

    def desligar(self):
        self.__ligada = False
        print('A lâmpada foi desligada.')

    # Método privado: lógica interna que o usuário do objeto não precisa ver
    @staticmethod
    def __esta_queimada():
        return False

    def status(self):
        return 'ligada' if self.__ligada else 'desligada'

    @staticmethod
    def exibir_menu():
        print("\n" + "=" * 50)
        print("Interruptor")
        print("=" * 50)
        print("1. LIGAR")
        print("2. DESLIGAR")
        print("0. Sair")
        print("=" * 50)

    def interruptor(self):
        self.exibir_menu()
        while True:
            opcao = input("Escolha uma opção do interruptor de luz: ")
            if opcao == "1":
                lamp.ligar()
            elif opcao == "2":
                lamp.desligar()
            elif opcao == "0":
                print("\nEncerrando sistema... Até logo!")
                break
            else:
                print("\nOpção inválida.")


if __name__ == "__main__":
    lamp = Lampada()
    lamp.interruptor()
