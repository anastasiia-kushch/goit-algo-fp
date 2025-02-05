import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key, color="orange"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def generate_orange_shades(steps, max_steps):

    color_start = mcolors.hex2color("#ff4500")
    color_end = mcolors.hex2color("#ffc6ac")  
    
    ratio = steps / max_steps
    color = (
        (color_end[0] - color_start[0]) * ratio + color_start[0],
        (color_end[1] - color_start[1]) * ratio + color_start[1],
        (color_end[2] - color_start[2]) * ratio + color_start[2]
    )
    
    return mcolors.rgb2hex(color)


def dfs_traversal(root):
    stack = [root]
    visited = []
    steps = 0
    max_steps = 0  
    colors = {}
    
    temp_stack = [root]
    while temp_stack:
        node = temp_stack.pop()
        if node not in visited:
            visited.append(node)
            if node.left:
                temp_stack.append(node.left)
            if node.right:
                temp_stack.append(node.right)
        max_steps += 1
    
    visited.clear()
    stack = [root]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            colors[node.id] = generate_orange_shades(steps, max_steps)
            steps += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    return visited, colors

def bfs_traversal(root):
    queue = [root]
    visited = []
    steps = 0
    max_steps = 0 
    colors = {}
    
    temp_queue = [root]
    while temp_queue:
        node = temp_queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
        max_steps += 1
    

    visited.clear()
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            colors[node.id] = generate_orange_shades(steps, max_steps)
            steps += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return visited, colors

def draw_tree_with_traversal(root, traversal_type='dfs'):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)
    
    if traversal_type == 'dfs':
        visited, colors = dfs_traversal(root)
    elif traversal_type == 'bfs':
        visited, colors = bfs_traversal(root)

    for node in visited:
        tree.nodes[node.id]['color'] = colors[node.id]

    colors_list = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors_list)
    plt.show()


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)


draw_tree_with_traversal(root, traversal_type='dfs')
draw_tree_with_traversal(root, traversal_type='bfs')