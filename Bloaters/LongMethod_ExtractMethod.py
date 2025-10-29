def obter_resultado():
    gols = int(input("Gols do Criciúma: "))
    adversario = input("Adversário: ")
    gols_adversario = int(input(f"Gols do {adversario}: "))
    return gols, adversario, gols_adversario

def exibir_placar(gols, adversario, gols_adversario):
    print("===== Resultado =====")
    print(f"Criciúma {gols} x {gols_adversario} {adversario}")

def determinar_vencedor(gols, adversario, gols_adversario):
    if gols > gols_adversario:
        print("Criciúma venceu! 🐯")
        return 3
    elif gols == gols_adversario:
        print("Empate.")
        return 1
    else:
        print(f"{adversario} venceu.")
        return 0

def partida_criciuma():
    gols, adversario, gols_adversario = obter_resultado()
    exibir_placar(gols, adversario, gols_adversario)
    pontos = determinar_vencedor(gols, adversario, gols_adversario)
    print(f"Total de pontos ganhos: {pontos}")

if __name__ == "__main__":
    partida_criciuma()
