class Node:

    def __init__(self, parent, board, steps, old_color, N):
        self.parent = parent
        self.board = board
        self.steps = steps
        self.old_color = old_color
        self.node_id = ""
        self.N = N

    def start_coloring(self, color):
        self.coloring(0, color)
        self.old_color = color
        self.__generate_id()

    def coloring(self, ind, color):
        self.board[ind] = color
        if ind + 1 % self.N != 0 and self.legal(ind + 1):
            self.coloring(ind + 1, color)
        if self.legal(ind + self.N):
            self.coloring(ind + self.N, color)
        if self.legal(ind - self.N):
            self.coloring(ind - self.N, color)
        if ind % self.N != 0 and self.legal(ind - 1):
            self.coloring(ind - 1, color)

    def solved(self):
        for i in range(len(self.board)):
            if self.board[i] != self.board[0]:
                return False
        return True

    def legal(self, ind):
        if 0 <= ind < len(self.board):
            if self.board[ind] == self.old_color:
                return True
        return False

    def print_board(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.board[i * self.N + j], end=' ')
            print()
        print()

    def __generate_id(self):
        self.node_id = ""
        for i in range(len(self.board)):
            self.node_id = self.node_id + self.board[i]

    # def __get_node_id(self):
    #     return ''.join(self.board)

    def get_child(self):
        return Node(self, self.board.copy(), self.steps, self.old_color, self.N)
