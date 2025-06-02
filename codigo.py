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
    visitados = {inicio} # Para evitar ciclos e caminhos redundantes

    while fila:
        atual, caminho = fila.popleft()
        if atual == destino:
            return caminho
        for amigo in rede_jogadores.get(atual, []):
            if amigo not in visitados:
                visitados.add(amigo)
                fila.append((amigo, caminho + [amigo]))
    
    return None
