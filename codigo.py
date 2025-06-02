#ARVORE BINÁRIA - CATEGORIA DOS JOGOS
from collections import deque

class No: 
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def criar_arvore_jogos():
    raiz = No("Jogos")
    raiz.esquerda = No("Ação")
    raiz.direita = No("Estratégia")
    raiz.esquerda.esquerda = No("FPS")
    raiz.esquerda.direita = No("Luta")
    raiz.direita.esquerda = No("Puzzle")
    raiz.direita.direita = No("Simulação")
    return raiz

def buscar_categoria(no, categoria):
    if no is None:
        return False
    if no.valor.lower() == categoria.lower():
        return True
    return buscar_categoria(no.esquerda, categoria) or buscar_categoria(no.direita, categoria)

def imprimir_categorias(no):
    if no is not None:
        imprimir_categorias(no.esquerda)
        print(f"- {no.valor}")
        imprimir_categorias(no.direita)


jogos_por_categoria = {
    "FPS": ["Counter-Strike", "Valorant", "Call of Duty"],
    "Luta": ["Street Fighter", "Mortal Kombat", "Tekken"],
    "Ação": ["GTA V", "Assassin's Creed", "Spider-Man"],
    "Puzzle": ["Tetris", "Candy Crush", "Portal"],
    "Simulação": ["The Sims", "SimCity", "Flight Simulator"],
    "Estratégia": ["Age of Empires", "Clash of Clans", "Civilization VI"],
    "Jogos": ["Jogo Genérico 1", "Jogo Genérico 2"]
}

rede_jogadores = {
    "Ana": ["Bruno", "Diego"],
    "Bruno": ["Ana", "Carla"],
    "Carla": ["Bruno", "Diego"],
    "Diego": ["Ana", "Carla"],
    "Lucas": ["Fernanda"],
    "Fernanda": ["Lucas"]
}

def buscar_conexao(inicio, destino):
    fila = deque()
    fila.append((inicio, [inicio]))
    visitados = {inicio}

    while fila:
        atual, caminho = fila.popleft()
        if atual == destino:
            return caminho
        for amigo in rede_jogadores.get(atual, []):
            if amigo not in visitados:
                visitados.add(amigo)
                fila.append((amigo, caminho + [amigo]))
    
    return None

def menu():
    raiz = criar_arvore_jogos()

    while True:
        print("\n=== PLATAFORMA DE JOGOS ===")
        print("1. Buscar categoria de jogo e listar jogos")
        print("2. Ver conexão entre jogadores")
        print("3. Sair")

        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == "1":
            print("\nCategorias disponíveis (em ordem):")
            imprimir_categorias(raiz)
            categoria_input = input("\nDigite a categoria que deseja buscar (ex: FPS, Puzzle): ").strip()

            
            categoria_encontrada_na_arvore = buscar_categoria(raiz, categoria_input)
            
            
            chave_categoria_dict = None
            if categoria_encontrada_na_arvore:
                for key in jogos_por_categoria.keys():
                    if key.lower() == categoria_input.lower():
                        chave_categoria_dict = key
                        break
            
            if chave_categoria_dict:
                print(f"\n✔ Categoria '{chave_categoria_dict}' encontrada!")
                jogos = jogos_por_categoria.get(chave_categoria_dict, [])
                if jogos:
                    print("\nJogos disponíveis nessa categoria:")
                    for idx, jogo in enumerate(jogos, start=1):
                        print(f"{idx}. {jogo}")
                    
                    escolha = input("\nDigite o número do jogo que deseja 'acessar' ou pressione Enter para voltar: ")
                    if escolha.isdigit():
                        escolha_int = int(escolha)
                        if 1 <= escolha_int <= len(jogos):
                            print(f"\n🎮 Você acessou o jogo: {jogos[escolha_int-1]}")
                        else:
                            print("❌ Número inválido.")
                    elif escolha == "":
                        print("Voltando ao menu...")
                    else:
                        print("❌ Entrada inválida.")
                else:
                    print(f"Nenhum jogo cadastrado diretamente na categoria '{chave_categoria_dict}'.")
            elif categoria_encontrada_na_arvore:
                 print(f"✔ Categoria '{categoria_input}' encontrada na árvore, mas sem jogos listados diretamente no dicionário com essa chave exata.")
            else:
                print(f"❌ Categoria '{categoria_input}' não foi encontrada na árvore.")
        
        elif opcao == "2":
            print("\nJogadores disponíveis:")
            for jogador in sorted(rede_jogadores.keys()):
                print(f"- {jogador}")
            inicio = input("Digite o nome do primeiro jogador: ").strip()
            destino = input("Digite o nome do segundo jogador: ").strip()

            if inicio in rede_jogadores and destino in rede_jogadores:
                if inicio == destino:
                    print("\n🔗 Você já é o jogador de destino!")
                else:
                    caminho = buscar_conexao(inicio, destino)
                    if caminho:
                        print("\n🔗 Conexão encontrada:")
                        print(" -> ".join(caminho))
                    else:
                        print(f"❌ Os jogadores '{inicio}' e '{destino}' não estão conectados diretamente ou indiretamente.")
            else:
                print("❌ Um ou ambos os jogadores não encontrados. Verifique os nomes digitados.")
        
        elif opcao == "3":
            print("👋 Saindo do sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__": 
    menu()            

