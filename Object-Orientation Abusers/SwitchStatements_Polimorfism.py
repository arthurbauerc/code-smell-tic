class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def acao_em_campo(self):
        raise NotImplementedError("Cada jogador deve definir sua ação em campo.")

class Goleiro(Jogador):
    def acao_em_campo(self):
        print(f"{self.nome} defende o gol do Criciúma!")

class Zagueiro(Jogador):
    def acao_em_campo(self):
        print(f"{self.nome} bloqueia o atacante adversário!")

class Meia(Jogador):
    def acao_em_campo(self):
        print(f"{self.nome} organiza a jogada no meio-campo.")

class Atacante(Jogador):
    def acao_em_campo(self):
        print(f"{self.nome} finaliza para o gol!")

if __name__ == "__main__":
    jogadores = [
        Goleiro("Alisson"),
        Zagueiro("Rodrigo"),
        Meia("Jhonata Robert"),
        Atacante("Diego")
    ]

    for j in jogadores:
        j.acao_em_campo()