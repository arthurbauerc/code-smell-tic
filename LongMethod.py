{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMmxge2lAUJesTnz77H0XVl"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QdWI4pZH2W6p",
        "outputId": "0086e524-9985-4912-92c7-d36e54db4655"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Gols do Criciúma: 2\n",
            "Adversário: avaí\n",
            "Gols do avaí: 1\n",
            "===== Resultado =====\n",
            "Criciúma 2 x 1 avaí\n",
            "Criciúma venceu! 🐯\n",
            "Total de pontos ganhos: 3\n"
          ]
        }
      ],
      "source": [
        "def partida_criciuma():\n",
        "    gols = int(input(\"Gols do Criciúma: \"))\n",
        "    adversario = input(\"Adversário: \")\n",
        "    gols_adversario = int(input(f\"Gols do {adversario}: \"))\n",
        "\n",
        "    print(\"===== Resultado =====\")\n",
        "    print(f\"Criciúma {gols} x {gols_adversario} {adversario}\")\n",
        "\n",
        "    if gols > gols_adversario:\n",
        "        print(\"Criciúma venceu! 🐯\")\n",
        "    elif gols == gols_adversario:\n",
        "        print(\"Empate.\")\n",
        "    else:\n",
        "        print(f\"{adversario} venceu.\")\n",
        "\n",
        "    pontos = 0\n",
        "    if gols > gols_adversario:\n",
        "        pontos += 3\n",
        "    elif gols == gols_adversario:\n",
        "        pontos += 1\n",
        "    print(f\"Total de pontos ganhos: {pontos}\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "  partida_criciuma()\n"
      ]
    }
  ]
}