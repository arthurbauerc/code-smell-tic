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

    def estatisticas_gerais_antigas(self):
        return "Função desativada para nova versão de relatórios."

    def enviar_relatorio_por_email(self):
        print("Relatório enviado por e-mail!")  

if __name__ == "__main__":
    treino = TreinoCriciuma("Paulo Bayer")
    treino.adicionar_jogador("Fabrício Lentz")
    treino.adicionar_jogador("Messi")
    treino.adicionar_exercicio("Finalização de média distância")
    treino.adicionar_exercicio("Posicionamento defensivo")
    treino.iniciar_treino()

    