from othernode import Node


def main():
    sixalphalist = ['y', 'y', 'o', 'g', 'o', 'p',
                    'g', 'r', 'g', 'b', 'p', 'o',
                    'r', 'o', 'p', 'o', 'y', 'r',
                    'b', 'g', 'y', 'b', 'g', 'y',
                    'y', 'o', 'b', 'o', 'r', 'o',
                    'b', 'r', 'g', 'y', 'p', 'b']
    node = Node(None, sixalphalist, 0, len(sixalphalist), 6)
    print(node.board[0])
    node.start_coloring(node.board[0])
    print(node.node_id)
    node.start_coloring('g')
    print(node.node_id)
    node.print_board()
    node.start_coloring('r')
    node.start_coloring('o')
    node.start_coloring('g')

    node.start_coloring('b')
    node.start_coloring('y')
    print(node.node_id)
    node.print_board()


if __name__ == '__main__':
    main()