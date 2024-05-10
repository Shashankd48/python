# Write a Python Program to implement FP tree growth Algorithm on a dataset of your own
# choice.

from collections import defaultdict

class Node:
    def __init__(self, item, count, parent):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = {}
        self.next = None

def construct_tree(dataset, min_support):
    header_table = defaultdict(int)
    for transaction in dataset:
        for item in transaction:
            header_table[item] += 1

    header_table = {k: v for k, v in header_table.items() if v >= min_support}

    if not header_table:
        return None, None

    for k in header_table:
        header_table[k] = [header_table[k], None]

    fp_tree = Node(None, 0, None)
    for transaction, count in dataset.items():
        transaction = [item for item in transaction if item in header_table]
        transaction.sort(key=lambda item: header_table[item][0], reverse=True)
        current_node = fp_tree
        for item in transaction:
            current_node = update_tree(item, current_node, header_table, count)
    return fp_tree, header_table

def update_tree(item, node, header_table, count):
    if item in node.children:
        node.children[item].count += count
    else:
        new_node = Node(item, count, node)
        node.children[item] = new_node
        if header_table[item][1] is None:
            header_table[item][1] = new_node
        else:
            update_header(header_table[item][1], new_node)
    return node.children[item]

def update_header(node_to_test, target_node):
    while node_to_test.next is not None:
        node_to_test = node_to_test.next
    node_to_test.next = target_node

def ascend_tree(node, prefix_path):
    if node.parent is not None:
        prefix_path.append(node.item)
        ascend_tree(node.parent, prefix_path)

def find_prefix_path(base_pat, tree_node):
    conditional_patterns = {}
    while tree_node is not None:
        prefix_path = []
        ascend_tree(tree_node, prefix_path)
        if len(prefix_path) > 1:
            conditional_patterns[frozenset(prefix_path[1:])] = tree_node.count
        tree_node = tree_node.next
    return conditional_patterns

def mine_tree(tree, header_table, min_support, prefix, frequent_itemsets):
    for item, item_info in sorted(header_table.items(), key=lambda x: x[1][0]):
        new_frequent_set = prefix.copy()
        new_frequent_set.add(item)
        frequent_itemsets.append(new_frequent_set)
        conditional_patterns = find_prefix_path(item, item_info[1])
        conditional_tree, conditional_header = construct_tree(conditional_patterns, min_support)
        if conditional_header is not None:
            mine_tree(conditional_tree, conditional_header, min_support, new_frequent_set, frequent_itemsets)

def fp_growth(dataset, min_support):
    fp_tree, header_table = construct_tree(dataset, min_support)
    frequent_itemsets = []
    mine_tree(fp_tree, header_table, min_support, set(), frequent_itemsets)
    return frequent_itemsets

def display_frequent_itemsets(frequent_itemsets):
    print("Frequent Itemsets:")
    for itemset in frequent_itemsets:
        print(", ".join(sorted(list(itemset))))

# Sample dataset
dataset = {
    ('a', 'b', 'd'): 2,
    ('b', 'c', 'e'): 3,
    ('a', 'b', 'c', 'e'): 2,
    ('a', 'e'): 2
}

min_support = 2

frequent_itemsets = fp_growth(dataset, min_support)
display_frequent_itemsets(frequent_itemsets)
