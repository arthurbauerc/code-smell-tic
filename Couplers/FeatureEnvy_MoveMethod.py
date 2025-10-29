class Jogador:
    def __init__(self, nome, idade, gols_marcados):
        self.nome = nome
        self.idade = idade
        self.gols_marcados = gols_marcados

    def calcular_valor_transferencia(self):
        base = 1000000
        if self.idade < 25:
            base *= 1.5
        elif self.idade > 30:
            base *= 0.8
        base += self.gols_marcados * 20000
        return base


class Transferencia:
    def exibir_valor(self, jogador):
        valor = jogador.calcular_valor_transferencia()
        print(f"Valor estimado de transferência de {jogador.nome}: R${valor:,.2f}")


if __name__ == "__main__":
    jogador = Jogador("Cristiano Ronaldo", 39, 66)
    transferencia = Transferencia()
    transferencia.exibir_valor(jogador)
