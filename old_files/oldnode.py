class Node:

    def __init__(self, parent, board, fill, steps, score, N):
        self.parent = parent
        self.board = board
        self.steps = steps
        self.score = score
        self.last_color = ''
        self.fill = fill
        self.node_id = ''
        self.N = N

    def start_coloring(self, color):
        self.fill = 'X' if self.fill == 'O' else 'O'
        self.coloring(0, color)
        self.last_color = color
        self.node_id = self.__get_node_id()

    def coloring(self, ind, color):
        if self.board[ind] not in ('X', 'O'):
            self.score -= 1
        self.board[ind] = self.fill
        if self.legal(ind + 1, color):
            self.coloring(ind + 1, color)
        if self.legal(ind + self.N, color):
            self.coloring(ind + self.N, color)
        if self.legal(ind - 1, color):
            self.coloring(ind - 1, color)
        if self.legal(ind - self.N, color):
            self.coloring(ind - self.N, color)

    def solved(self):
        return True if self.score == 0 else False

    def legal(self, ind, color):
        if 0 <= ind < len(self.board):
            if self.board[ind] == color:
                return True
            elif self.fill == 'X' and self.board[ind] == 'O':
                return True
            elif self.fill == 'O' and self.board[ind] == 'X':
                return True
        return False

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                print(self.board[i][j], end=' ')
            print()

    def __get_node_id(self):
        matrix_hash = ""
        for i in range(len(self.board)):
            if self.board[i] == 'O':
                matrix_hash = matrix_hash + 'X'
            else:
                matrix_hash = matrix_hash + self.board[i]
        return matrix_hash

    def get_child(self):
        cp = [row[:] for row in self.board]
        return Node(self, cp, self.fill, self.steps, self.score)
