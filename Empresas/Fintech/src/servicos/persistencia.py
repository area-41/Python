import json
import os
from src.servicos.logger import logger


class ServicoPersistencia:
    CADASTRAR_PATH = os.path.join("data", "contas.json")

    @classmethod
    def salvar_conta(cls, dados_nova_conta: dict):
        """Salva uma conta garantindo que o titular seja único."""
        os.makedirs("data", exist_ok=True)
        contas = cls.listar_contas()

        # Verificação de Duplicidade (Case Insensitive)
        nome_novo = dados_nova_conta['titular'].lower()

        if any(c['titular'].lower() == nome_novo for c in contas):
            logger.warning(f"Tentativa de cadastro duplicado: {dados_nova_conta['titular']}")
            raise ValueError(f"Já existe uma conta cadastrada para o titular '{dados_nova_conta['titular']}'.")

        contas.append(dados_nova_conta)

        with open(cls.CADASTRAR_PATH, "w", encoding="utf-8") as f:
            json.dump(contas, f, indent=4)

        logger.info(f"Conta persistida com sucesso: {dados_nova_conta['titular']}")

    @classmethod
    def listar_contas(cls) -> list:
        if not os.path.exists(cls.CADASTRAR_PATH):
            return []

        with open(cls.CADASTRAR_PATH, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    @classmethod
    def buscar_conta_por_titular(cls, nome: str) -> dict:
        contas = cls.listar_contas()
        return next((c for c in contas if c['titular'].lower() == nome.lower()), None)

    @classmethod
    def atualizar_conta(cls, titular: str, novos_dados: dict) -> bool:
        """Busca o titular e atualiza seus dados no JSON."""
        contas = cls.listar_contas()
        titular_norm = titular.strip().lower()

        for i, conta in enumerate(contas):
            if conta['titular'].strip().lower() == titular_norm:
                # Atualiza mantendo o nome original, mas mudando saldo/renda
                contas[i].update(novos_dados)
                with open(cls.CADASTRAR_PATH, "w", encoding="utf-8") as f:
                    json.dump(contas, f, indent=4)
                logger.info(f"Dados atualizados para o titular: {titular}")
                return True
        return False

    @classmethod
    def deletar_conta(cls, titular: str) -> bool:
        """Remove uma conta da lista e sobrescreve o JSON."""
        contas = cls.listar_contas()
        titular_norm = titular.strip().lower()

        # Cria uma nova lista sem a conta que queremos deletar
        novas_contas = [c for c in contas if c['titular'].strip().lower() != titular_norm]

        if len(novas_contas) < len(contas):
            with open(cls.CADASTRAR_PATH, "w", encoding="utf-8") as f:
                json.dump(novas_contas, f, indent=4)
            logger.info(f"Conta deletada: {titular}")
            return True
        return False