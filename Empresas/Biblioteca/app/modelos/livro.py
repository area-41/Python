class Livro:
    """
    Representa um livro com atributos detalhados e controle de estado privado.
    """
    def __init__(self, titulo: str, autor: str, ano: int, editora: str,
                 paginas: int, isbn: str, genero: str, edicao: str = "1ª"):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano
        self.editora = editora
        self.paginas = paginas
        self.isbn = isbn
        self.genero = genero
        self.edicao = edicao
        # Atributo privado
        self.__emprestado: bool = False

    def emprestar(self) -> bool:
        if not self.__emprestado:
            self.__emprestado = True
            return True
        return False

    def devolver(self) -> None:
        self.__emprestado = False

    def status(self) -> str:
        return 'Emprestado' if self.__emprestado else 'Disponível'

    """
    def __str__(self) -> str:
        # Definindo um ícone visual para o status
        status_cor = "🟢 Disponível" if not self.__emprestado else "🔴 Emprestado"

        return (
            f"{'=' * 60}\n"
            f"📖 TÍTULO: {self.titulo.upper()} ({self.edicao} Ed.)\n"
            f"✍️  AUTOR:  {self.autor:<25} | 🏷️ GÊNERO: {self.genero}\n"
            f"🏢 EDITORA: {self.editora:<25} | 📅 ANO:    {self.ano_publicacao}\n"
            f"🔢 ISBN:    {self.isbn:<25} | 📄 PÁGS:   {self.paginas}\n"
            f"📊 STATUS:  {status_cor}\n"
            f"{'=' * 60}"
        )
    
    def __str__(self) -> str:
        return (f"[{self.isbn}] {self.titulo} - {self.autor} | "
                f"Editora: {self.editora} ({self.ano_publicacao}) | "
                f"{self.paginas} pág. | Gênero: {self.genero} | "
                f"Status: {self.status()}")
    """

    def __str__(self) -> str:
        status_txt = "DISP" if not self.__emprestado else "EMPR"
        return (f"[{status_txt}] {self.isbn} | {self.titulo[:25]:<25} | {self.autor[:15]:<15} | "
                f"{self.editora[:10]:<10} | {self.ano_publicacao} | {self.paginas}p | {self.genero}")