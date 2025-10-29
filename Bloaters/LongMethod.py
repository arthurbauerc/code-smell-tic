def partida_criciuma():
    gols = int(input("Gols do Criciúma: "))
    adversario = input("Adversário: ")
    gols_adversario = int(input(f"Gols do {adversario}: "))
    
    print("===== Resultado =====")
    print(f"Criciúma {gols} x {gols_adversario} {adversario}")

    if gols > gols_adversario:
        print("Criciúma venceu! 🐯")
    elif gols == gols_adversario:
        print("Empate.")
    else:
        print(f"{adversario} venceu.")

    pontos = 0
    if gols > gols_adversario:
        pontos += 3
    elif gols == gols_adversario:
        pontos += 1
    print(f"Total de pontos ganhos: {pontos}")

if __name__ == "__main__":
  partida_criciuma()
