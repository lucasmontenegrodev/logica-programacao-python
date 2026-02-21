import random

def jogar():
    numero_secreto = random.randint(0, 100)
    tentativas_maximas = 5

    print("    JOGO DE ADIVINHAÇÃO DE NÚMEROS")
    print(f"Adivinhe o número secreto entre 0 e 100.")
    print(f"Você tem {tentativas_maximas} tentativas. Boa sorte!\n")

    for tentativa in range(1, tentativas_maximas + 1):
        restantes = tentativas_maximas - tentativa + 1
        print(f"[Tentativa {tentativa}/{tentativas_maximas} | Restantes: {restantes}]")

        while True:
            try:
                palpite = int(input("Digite seu palpite: "))
                if palpite < 0 or palpite > 100:
                    print("  Por favor, digite um número entre 0 e 100.\n")
                else:
                    break
            except ValueError:
                print("  Entrada inválida. Digite um número inteiro.\n")

        if palpite == numero_secreto:
            print(f"\n Parabéns! Você acertou o número {numero_secreto} em {tentativa} tentativa(s)!")
            print("Você venceu o jogo! 🎉")
            return
        elif palpite < numero_secreto:
            print(f" O número secreto é MAIOR que {palpite}.\n")
        else:
            print(f" O número secreto é MENOR que {palpite}.\n")

    print("\nGAME OVER")
    print(f"O número secreto era: {numero_secreto}")

jogar()