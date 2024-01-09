# A Huffman Tree Node
import heapq


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

    def __str__(self):
        return f"{self.symbol} -> {self.freq}"


# characters for huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f']

# frequency of characters
freq = [5, 9, 12, 13, 16, 45]

# list containing unused nodes
nodes = []

for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = 0
    right.huff = 1
    new_node = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, new_node)


def print_nodes(node, val=''):
    val += str(node.huff)
    if node.left:
        print_nodes(node.left, val)
    if node.right:
        print_nodes(node.right, val)
    if not node.left and not node.right:
        print(f"{node.symbol}-->{val}")


print_nodes(nodes[0])
