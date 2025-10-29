class Jogador:
    def __init__(self, nome, idade, gols_marcados):
        self.nome = nome
        self.idade = idade
        self.gols_marcados = gols_marcados


class Transferencia:
    def calcular_valor(self, jogador):
        base = 1000000
        if jogador.idade < 25:
            base *= 1.5
        elif jogador.idade > 30:
            base *= 0.8
        base += jogador.gols_marcados * 20000
        print(f"Valor estimado de transferência de {jogador.nome}: R${base:,.2f}")


if __name__ == "__main__":
    jogador = Jogador("Cristiano Ronaldo", 39, 66)
    transferencia = Transferencia()
    transferencia.calcular_valor(jogador)
