class TreinoCriciuma:
    def __init__(self, treinador):
        self.treinador = treinador
        self.jogadores = []
        self.exercicios = []

    def adicionar_jogador(self, nome):
        self.jogadores.append(nome)
        print(f"Jogador {nome} adicionado ao treino.")

    def adicionar_exercicio(self, descricao):
        self.exercicios.append(descricao)
        print(f"Exercício '{descricao}' adicionado ao treino.")

    def iniciar_treino(self):
        print(f"\nTreino comandado por {self.treinador}")
        print("Jogadores em campo:", ", ".join(self.jogadores))
        print("Exercícios do dia:")
        for e in self.exercicios:
            print("-", e)

if __name__ == "__main__":
    treino = TreinoCriciuma("Cláudio Tencati")
    treino.adicionar_jogador("Cristiano Ronaldo")
    treino.adicionar_jogador("Zé Carlos")
    treino.adicionar_exercicio("Finalização de média distância")
    treino.adicionar_exercicio("Posicionamento defensivo")
    treino.iniciar_treino()