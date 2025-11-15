def has_cycle(graph):
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False


def find_cycle(graph):
    visited = set()
    parent = {}

    def dfs(u, p):
        visited.add(u)
        parent[u] = p
        for v in graph.get(u, []):
            if v not in visited:
                result = dfs(v, u)
                if result:
                    return result
            elif v != p:
                cycle = [v]
                curr = u
                while curr != v:
                    cycle.append(curr)
                    curr = parent[curr]
                cycle.append(v)
                cycle.reverse()
                return cycle
        return None

    for node in graph:
        if node not in visited:
            result = dfs(node, None)
            if result:
                return result
    return None
