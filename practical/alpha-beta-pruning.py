class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = -float('inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Example usage:
if __name__ == "__main__":
    # Example tree:
    #         root
    #        /    \
    #      3      5
    #     / \    / \
    #    6  9  1   2
    leaf1 = Node(6)
    leaf2 = Node(9)
    leaf3 = Node(1)
    leaf4 = Node(2)
    
    internal1 = Node(0, [leaf1, leaf2])
    internal2 = Node(0, [leaf3, leaf4])
    
    root = Node(0, [internal1, internal2])
    
    best_value = alpha_beta(root, 2, -float('inf'), float('inf'), True)
    
    print(f"Best value: {best_value}")
