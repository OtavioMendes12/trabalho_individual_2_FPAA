def hamiltonian_path(graph, path, visited):
    if len(path) == len(graph):
        return True

    last = path[-1]
    for neighbor in graph[last]:
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)
            if hamiltonian_path(graph, path, visited):
                return True
            path.pop()
            visited[neighbor] = False

    return False
