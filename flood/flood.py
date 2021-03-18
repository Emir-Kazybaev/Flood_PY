from node import Node
from solver import Solver
import math

COLORS = ['y', 'o', 'r', 'g', 'b', 'p']

class Flood:
    def __init__(self, lis):
        self.steps = 0
        self.lis = lis
        self.colors = COLORS[:self.calc_colors()]
        self.nodes = []
        self.create_root()

    def create_root(self):
        node = Node(None, self.lis, 0, '', int(math.sqrt(len(self.lis))))
        node.start_coloring(node.board[0])
        self.nodes.append(node)

    def calc_colors(self):
        s = set()
        for i in self.lis:
            if i not in s:
                s.add(i)
        print(len(s))
        return len(s)

    def bfs(self):
        solution = Solver(self.nodes, self.colors)
        solution.bfs()
