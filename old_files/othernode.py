class Node:

    def __init__(self, parent, board, steps, score, N):
        self.parent = parent
        self.board = board
        self.steps = steps
        self.score = score
        self.old_color = ''
        self.node_id = ''
        self.N = N

    def start_coloring(self, color):
        if color != self.old_color:
            print("Coloring to", color)
            self.coloring(0, color)
            self.old_color = color
            self.node_id = self.__get_node_id()

    def coloring(self, ind, color):
        self.score -= 1
        self.board[ind] = color
        if ind % self.N != self.N and self.legal(ind + 1):
            self.coloring(ind + 1, color)
        if self.legal(ind + self.N):
            self.coloring(ind + self.N, color)
        if ind % self.N != 0 and self.legal(ind - 1):
            self.coloring(ind - 1, color)
        if self.legal(ind - self.N):
            self.coloring(ind - self.N, color)

    def solved(self):
        return True if self.score == 0 else False

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

    def __get_node_id(self):
        matrix_hash = ""
        for i in range(len(self.board)):
            matrix_hash = matrix_hash + self.board[i]
        return matrix_hash

    def get_child(self):
        return Node(self, self.board[:], self.fill, self.steps, self.score)
