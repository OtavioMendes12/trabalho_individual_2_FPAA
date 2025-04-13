# Projeto: HamiltonPathFinder

## 📌 Descrição do projeto

Este projeto tem como objetivo implementar um algoritmo em Python para encontrar um **Caminho Hamiltoniano** em um grafo não direcionado. Um Caminho Hamiltoniano é um caminho que passa por todos os vértices exatamente uma vez. A implementação utiliza uma abordagem de **backtracking** para testar todas as possibilidades de caminhos até encontrar (ou não) uma solução válida.

---

## 🧠 Lógica do algoritmo implementado

### Arquivo: `functions.py`

```python
def hamiltonian_path(graph, path, visited):
```
- Função recursiva para encontrar o caminho Hamiltoniano.

```python
    if len(path) == len(graph):
        return True
```
- Verifica se todos os vértices foram visitados.

```python
    last = path[-1]
```
- Pega o último vértice do caminho atual.

```python
    for neighbor in graph[last]:
```
- Itera sobre os vizinhos do vértice atual.

```python
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)
```
- Se o vizinho não foi visitado, marca e adiciona ao caminho.

```python
            if hamiltonian_path(graph, path, visited):
                return True
            path.pop()
            visited[neighbor] = False
```
- Caso o caminho não seja válido, realiza backtracking.

```python
    return False
```
- Retorna False se nenhum caminho válido for encontrado.

---

## ▶️ Como executar o projeto

### 1. Criar e ativar ambiente virtual:

```bash
python -m venv .venv
```

- **Windows**:
```bash
.venv\Scripts\activate
```

- **Linux/macOS**:
```bash
source .venv/bin/activate
```

### 2. Instalar bibliotecas (opcional, para visualização):

```bash
pip install networkx matplotlib
```

### 3. Executar o algoritmo:

```bash
python main.py
```

### 4. Visualizar o grafo (opcional):

```bash
python view.py
```

---

## 📄 Relatório Técnico

### Classes de complexidade (P, NP, NP-Completo, NP-Difícil)

- O problema do **Caminho Hamiltoniano** pertence à classe **NP-Completo**.
- Justificativa:
  - Está em NP: podemos verificar uma solução em tempo polinomial.
  - Está relacionado ao Problema do Caixeiro Viajante, que também é NP-Completo.

---

### Análise da complexidade assintótica de tempo

- O algoritmo de backtracking possui complexidade **O(n!)** no pior caso, pois testa todas as permutações possíveis dos vértices.
- Determinada por análise combinatória (fatorial de n vértices).

---

### Aplicação do Teorema Mestre

- ❌ O Teorema Mestre **não se aplica** neste caso.
- Justificativa:
  - O algoritmo não segue uma forma de divisão e conquista.
  - Não existe uma recorrência do tipo T(n) = aT(n/b) + f(n).

---

### Análise dos casos de complexidade

| Caso         | Descrição                                     | Complexidade |
|--------------|-----------------------------------------------|--------------|
| Melhor caso  | Caminho encontrado nas primeiras tentativas   | O(n)         |
| Caso médio   | Explora parte significativa dos caminhos      | O(n!)        |
| Pior caso    | Testa todas as combinações possíveis          | O(n!)        |

---

## 📊 Visualização do grafo (opcional)

A função `visualize()` usa `networkx` e `matplotlib` para exibir o grafo e destacar o Caminho Hamiltoniano.

A imagem gerada é salva em:
```
assets/hamiltonian_path.png
```

---

## 📁 Estrutura de arquivos

```
HamiltonPathFinder/
├── main.py
├── functions.py
├── view.py
├── assets/
│   └── hamiltonian_path.png
└── README.md
```

---

## 📄 Licença

MIT
