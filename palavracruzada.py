import random
import time

# Banco de dados de palavras cruzadas com níveis de dificuldade
palavras_cruzadas = {
    'facil': {
        'pistas': ["Pista 1: Esta é uma fruta vermelha", "Pista 2: Animal que mia"],
        'respostas': ["morango", "gato"],
        'dicas': ["Dica 1: É uma fruta doce", "Dica 2: Tem muitas sementes"]
    },
    'medio': {
        'pistas': ["Pista 1: É um planeta do nosso sistema solar", "Pista 2: Instrumento musical de corda"],
        'respostas': ["terra", "violino"],
        'dicas': ["Dica 1: É o terceiro planeta a partir do sol", "Dica 2: Tem uma lua chamada Lua"]
    },
    'dificil': {
        'pistas': ["Pista 1: Este é um elemento químico", "Pista 2: É um animal aquático"],
        'respostas': ["hidrogenio", "tubarao"],
        'dicas': ["Dica 1: É o elemento mais abundante no universo", "Dica 2: É um gás incolor e inflamável"]
    },
    'expert': {
        'pistas': ["Pista 1: Cientista famoso pela teoria da relatividade"],
        'respostas': ["einstein"],
        'dicas': ["Dica 1: Autor da fórmula E=mc^2"]
    }
}

def escolher_palavras_cruzadas():
    nivel = input("Escolha o nível de dificuldade (facil/medio/dificil/expert): ").lower()
    return palavras_cruzadas.get(nivel, palavras_cruzadas['facil'])

def mostrar_dicas(dicas):
    for dica in dicas:
        print("Dica:", dica)
    print()

def jogar_palavras_cruzadas(tempo_limite=None):
    palavras = escolher_palavras_cruzadas()
    pontuacao = 0
    dicas_utilizadas = 0
    tempo_inicial = time.time()
    
    print("\nBem-vindo ao jogo de palavras cruzadas!")
    print("Responda às pistas com as palavras corretas para ganhar pontos.")
    
    for indice, pista in enumerate(palavras['pistas']):
        print("\n" + pista)
        resposta_jogador = input("Sua resposta: ").lower()
        
        if resposta_jogador == palavras['respostas'][indice]:
            print("Correto!")
            pontuacao += 1
        else:
            print("Incorreto!")
            if dicas_utilizadas < len(palavras['dicas']):
                mostrar_dicas(palavras['dicas'][dicas_utilizadas:])
                dicas_utilizadas = len(palavras['dicas'])
            else:
                print("Você usou todas as dicas disponíveis!")
                print("A resposta correta é:", palavras['respostas'][indice])
        
        if tempo_limite and (time.time() - tempo_inicial) > tempo_limite:
            print("Tempo esgotado!")
            break
    
    tempo_total = time.time() - tempo_inicial
    print("\nPontuação final:", pontuacao, "/", len(palavras['pistas']))
    print("Tempo total:", round(tempo_total, 2), "segundos")

def modo_multiplayer():
    num_jogadores = int(input("Quantos jogadores participarão? "))
    
    for jogador in range(1, num_jogadores + 1):
        print(f"\nJogador {jogador}, é sua vez!")
        jogar_palavras_cruzadas()

def modo_estudo():
    palavras = escolher_palavras_cruzadas()
    
    print("\nModo de estudo selecionado.")
    print("Pistas e respostas:")
    for indice, pista in enumerate(palavras['pistas']):
        print(f"\nPista {indice + 1}: {pista}")
        print(f"Resposta: {palavras['respostas'][indice]}")
        if indice < len(palavras['dicas']):
            print("Dicas:")
            for dica in palavras['dicas'][indice:]:
                print(dica)

def criar_palavras_cruzadas_personalizadas():
    print("\nCriando palavras cruzadas personalizadas:")
    nivel = input("Digite um nome para o nível de dificuldade (ex: personalizado): ").lower()
    
    pistas = []
    respostas = []
    dicas = []
    
    while True:
        pista = input("Digite uma pista (ou digite 'fim' para terminar): ")
        if pista.lower() == 'fim':
            break
        resposta = input("Digite a resposta da pista: ")
        dica = input("Digite uma dica para a resposta: ")
        
        pistas.append(pista)
        respostas.append(resposta.lower())
        dicas.append(dica)
    
    palavras_cruzadas[nivel] = {'pistas': pistas, 'respostas': respostas, 'dicas': dicas}
    
    print(f"\nPalavras cruzadas personalizadas para o nível '{nivel}' criadas com sucesso!")

def salvar_palavras_cruzadas():
    with open("palavras_cruzadas_personalizadas.txt", "w") as arquivo:
        for nivel, dados in palavras_cruzadas.items():
            arquivo.write(f"Nível: {nivel}\n")
            arquivo.write(f"Pistas: {', '.join(dados['pistas'])}\n")
            arquivo.write(f"Respostas: {', '.join(dados['respostas'])}\n")
            arquivo.write(f"Dicas: {', '.join(dados['dicas'])}\n\n")
    print("Palavras cruzadas personalizadas salvas com sucesso!")

def carregar_palavras_cruzadas():
    try:
        with open("palavras_cruzadas_personalizadas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            palavras_cruzadas.clear()  # Limpa o banco de dados existente
            nivel = None
            for linha in linhas:
                if linha.startswith("Nível:"):
                    nivel = linha.split(":")[1].strip().lower()
                elif linha.startswith("Pistas:"):
                    pistas = linha.split(":")[1].strip().split(", ")
                elif linha.startswith("Respostas:"):
                    respostas = linha.split(":")[1].strip().split(", ")
                elif linha.startswith("Dicas:"):
                    dicas = linha.split(":")[1].strip().split(", ")
                    palavras_cruzadas[nivel] = {'pistas': pistas, 'respostas': respostas, 'dicas': dicas}
        print("Palavras cruzadas personalizadas carregadas com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo de palavras cruzadas personalizadas encontrado.")

if __name__ == "__main__":
    while True:
        print("\nEscolha uma opção:")
        print("1 - Jogar")
        print("2 - Multiplayer")
        print("3 - Modo de Estudo")
        print("4 - Criar palavras cruzadas personalizadas")
        print("5 - Salvar palavras cruzadas personalizadas")
        print("6 - Carregar palavras cruzadas personalizadas")
        print("7 - Sair")
        
        escolha = input("Sua escolha: ")
        
        if escolha == '1':
            jogar_palavras_cruzadas()
        elif escolha == '2':
            modo_multiplayer()
        elif escolha == '3':
            modo_estudo()
        elif escolha == '4':
            criar_palavras_cruzadas_personalizadas()
        elif escolha == '5':
            salvar_palavras_cruzadas()
        elif escolha == '6':
            carregar_palavras_cruzadas()
        elif escolha == '7':
            break
        else:
            print("Escolha inválida. Tente novamente.")
