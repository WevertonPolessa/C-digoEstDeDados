# Este projeto foi desenvolvido como parte do trabalho da disciplina de **Estrutura de Dados**, com o objetivo de aplicar na prática os conceitos de **Árvore Binária** e **Grafos*


---
# Tema: Sistema de Organização de Jogos e Rede de Jogadores. 🎮

O sistema permite:
- Organizar categorias de jogos usando árvore binária.
- Simular uma rede de jogadores e suas conexões através de um grafo.
- Fazer buscas tanto nas categorias dos jogos quanto nas conexões dos jogadores.
---


**Etapas do Desenvolvimento**
# Etapa 1 — Classe Nó da Árvore Binária
- Criamos uma classe chamada `No`, que representa cada nó da árvore.
- Cada nó possui:
  - Um valor (nome da categoria).
  - Referências para a esquerda e para a direita.

# Etapa 2 — Montagem da Árvore Binária
- Montamos a árvore com as seguintes categorias:
  - Raiz: Jogos
    - Esquerda: Ação
      - Esquerda: FPS
      - Direita: Luta
    - Direita: Estratégia
      - Esquerda: Puzzle
      - Direita: Simulação

# Etapa 3 — Implementação da busca na árvore binária e impressão das categorias da árvore
Criamos uma função para buscar uma categoria na árvore binária.
Se o nó buscado for encontrado, retorna verdadeiro.
Se não for encontrado, retorna falso.

# Etapa 4 — Cadastro dos jogos por categoria
Criamos um dicionário chamado jogos_por_categoria que armazena uma lista de jogos para cada categoria que existe na árvore.
Isso facilita para o usuário visualizar as opções disponíveis.

# Etapa 5 — Cadastro dos Jogos por Categoria

Criamos um dicionário chamado jogos_por_categoria que armazena uma lista de jogos para cada categoria existente na árvore.

Exemplo:

FPS: Counter-Strike, Valorant, Call of Duty

Puzzle: Tetris, Candy Crush, Portal.

# Etapa 6 — Grafo para Rede de Jogadores

Implementamos um grafo para simular a rede de amizades entre jogadores.

Cada jogador é um vértice e suas conexões (amizades) são as arestas.

# Etapa 7 — Busca de Conexões no Grafo

Criamos uma busca em largura (BFS) que permite verificar se dois jogadores estão conectados dentro da rede de amizades.

Exibe o caminho da conexão (ex.: Ana -> Bruno -> Carla).

# Etapa 8 — Menu Interativo

Desenvolvemos um menu simples e intuitivo que permite:

Buscar uma categoria de jogo e ver os jogos disponíveis nela.

Selecionar um jogo específico da lista.

Consultar conexões entre dois jogadores da rede.

Sair do programa.

# 🧠 Tecnologias Utilizadas

Python

Estrutura de Dados:

Árvore Binária

Grafos (Busca em Largura - BFS)

# 🎯 Objetivo do Projeto

Simular uma plataforma de jogos utilizando conceitos de Estrutura de Dados.

Aplicar na prática o uso de árvore binária para organização de categorias e grafos para representação de redes.

# 🚀 Possíveis Melhorias Futuras

Permitir cadastrar novas categorias e novos jogos.

Tornar a rede de jogadores editável (adicionar e remover conexões).

Implementar uma interface gráfica.









