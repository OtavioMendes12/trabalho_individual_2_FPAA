from functions import hamiltonian_path

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

start = 0
path = [start]
visited = [False] * len(graph)
visited[start] = True

if hamiltonian_path(graph, path, visited):
    print("Caminho Hamiltoniano encontrado:", path)
else:
    print("Nenhum Caminho Hamiltoniano encontrado.")
