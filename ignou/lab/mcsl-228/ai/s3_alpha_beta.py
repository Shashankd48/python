class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value

    if maximizing_player:
        value = float('-inf')
        for child in node.children:
            value = max(value, alpha_beta_pruning(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alpha_beta_pruning(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

# Example usage
root = Node()
root.children = [Node(3), Node(5), Node(6)]

root.children[0].children = [Node(9), Node(1)]
root.children[1].children = [Node(2)]
root.children[2].children = [Node(7), Node(4)]

alpha = float('-inf')
beta = float('inf')
maximizing_player = True
result = alpha_beta_pruning(root, 3, alpha, beta, maximizing_player)
print("Optimal value:", result)
