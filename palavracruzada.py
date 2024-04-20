def main():
    palavras_cruzadas = [
        "1. Fruta amarela: _ _ _ _ _ _",
        "2. Animal dompestico: _ _ _ _",
        "3. Cor primária: _ _ _ _ "
    ]

    respostas = ["banana", "gato", "azul"]

    print("Bem-vindo ao jogo de palavras cruzadas!")
    print("Preecha as palavras cruzadas com as respostas corretas.")

    pontuacao = 0
    for i, pista in enumerate(palavras_cruzadas):
        print(pista)
        palpite = input("Sua resposta: ")

        if palpite.lower() == respostas[i]:
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Incorreto! A resposta correta é '{respostas[i]}'.")

    print(f"Sua pontuação final é: {pontuacao}/{len(palavras_cruzadas)}")

main()