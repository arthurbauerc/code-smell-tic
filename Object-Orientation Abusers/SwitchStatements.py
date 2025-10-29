class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def acao_em_campo(self):
        if self.posicao == "goleiro":
            print(f"{self.nome} defende o gol do Criciúma!")
        elif self.posicao == "zagueiro":
            print(f"{self.nome} bloqueia o atacante adversário!")
        elif self.posicao == "meia":
            print(f"{self.nome} organiza a jogada no meio-campo.")
        elif self.posicao == "atacante":
            print(f"{self.nome} finaliza para o gol!")
        else:
            print(f"{self.nome} não tem posição definida.")


if __name__ == "__main__":
    
    goleiro = Jogador("Alisson", "goleiro")
    zagueiro = Jogador("Rodrigo", "zagueiro")
    meia = Jogador("Jhonata Robert", "meia")
    atacante = Jogador("Diego", "atacante")
    
    print("--- Escalando o time! ---")
    goleiro.acao_em_campo()
    zagueiro.acao_em_campo()
    meia.acao_em_campo()
    atacante.acao_em_campo()