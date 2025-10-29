class EstatisticasJogo:
    def __init__(self):
        self.gols = 0
        self.cartoes = 0

    def registrar_gol(self, quantidade):
        self.gols += quantidade
        print(f"Gols registrados: {self.gols}")

    def registrar_cartao(self, quantidade):
        self.cartoes += quantidade
        print(f"Cartões registrados: {self.cartoes}")

    def resumo(self):
        return f"Gols: {self.gols} | Cartões: {self.cartoes}"


class PublicoJogo:
    def __init__(self):
        self.publico = 0

    def registrar_publico(self, quantidade):
        self.publico = quantidade
        print(f"Público registrado: {self.publico} torcedores")

    def resumo(self):
        return f"Público: {self.publico} torcedores"


class JogoCriciuma:
    def __init__(self):
        self.estatisticas = EstatisticasJogo()
        self.publico = PublicoJogo()

    def relatorio_geral(self):
        print("\n=== Relatório do Criciúma ===")
        print(self.estatisticas.resumo())
        print(self.publico.resumo())


if __name__ == "__main__":
    jogo = JogoCriciuma()
    jogo.estatisticas.registrar_gol(2)
    jogo.estatisticas.registrar_cartao(3)
    jogo.publico.registrar_publico(15200)
    jogo.relatorio_geral()
