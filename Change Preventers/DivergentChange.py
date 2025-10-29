class EstatisticasCriciuma:
    def __init__(self):
        self.gols = 0
        self.cartoes = 0
        self.publico = 0

    def registrar_gol(self, quantidade):
        self.gols += quantidade
        print(f"Gols registrados: {self.gols}")

    def registrar_cartao(self, quantidade):
        self.cartoes += quantidade
        print(f"Cartões registrados: {self.cartoes}")

    def registrar_publico(self, quantidade):
        self.publico = quantidade
        print(f"Público registrado: {self.publico} torcedores")

    def relatorio_geral(self):
        print("\n=== Relatório do Criciúma ===")
        print(f"Gols: {self.gols}")
        print(f"Cartões: {self.cartoes}")
        print(f"Público: {self.publico}")

if __name__ == "__main__":
    jogo = EstatisticasCriciuma()
    jogo.registrar_gol(2)
    jogo.registrar_cartao(3)
    jogo.registrar_publico(15200)
    jogo.relatorio_geral()

