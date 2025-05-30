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


