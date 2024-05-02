def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        key = [float('inf')] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1

        total_weight = 0
        print("Edge \tWeight")
        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
            if parent[u] is not None:
                print(parent[u], "-", u, "\t", key[u])
                total_weight += key[u]

        print("Total minimum weight:", total_weight)

if __name__ == "__main__":
    print("Enter your choice:")
    print("1. Selection Sort")
    print("2. Prim's Minimal Spanning Tree Algorithm")
    choice = int(input())

    if choice == 1:
        arr = list(map(int, input("Enter elements separated by space: ").split()))
        sorted_arr = selection_sort(arr)
        print("Sorted array:", sorted_arr)
    elif choice == 2:
        V = int(input("Enter the number of vertices: "))
        g = Graph(V)
        print("Enter the adjacency matrix:")
        for i in range(V):
            g.graph[i] = list(map(int, input().split()))

        g.prim_mst()
    else:
        print("Invalid choice")
