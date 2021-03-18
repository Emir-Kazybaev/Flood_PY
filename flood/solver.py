class Solver:
    def __init__(self, nodes, colors):
        self.nodes = []
        self.nodes.append(nodes[0])
        self.id_set = set()
        self.colors = colors
        # self.added = 0
        # self.discarded = 0

    def add_children(self):
        # for color in range(self.num_of_colors):
        for color in self.colors:
            node = self.nodes[0].get_child()
            if color != node.old_color:
                node.start_coloring(color)
                if node.node_id not in self.id_set:
                    # print(node.node_id, node.score, "ADDED")
                    # self.added += 1
                    node.parent = self.nodes[0]
                    node.steps += 1
                    self.nodes.append(node)
                    self.id_set.add(node.node_id)
                # self.discarded += 1
                #     print( "NOT ADDED")
                #     print(node.node_id)
                #     node.print_board()
                #     self.id_set.get(node.node_id).print_board()
        # if (len(self.nodes) % 10 == 0):
        #     print(self.nodes[0].score)
        #     self.nodes[0].printB()
        self.nodes.pop(0)
        # print(len(self.nodes))

    def bfs(self):
        solution = []
        while True:
            if self.nodes[0].solved():
                print("Solved")
                current_node = self.nodes[0]
                while current_node.parent is not None:
                    solution.insert(0, current_node)
                    current_node = current_node.parent
                break
            self.add_children()
        for node in solution:
            print(node.steps)
            node.print_board()
            print("############")
        # print("Added {}, Discarded {}. Total {}".format(self.added, self.discarded, self.added + self.discarded))
