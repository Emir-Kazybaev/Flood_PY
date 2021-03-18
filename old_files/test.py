def main():
    lis = ((1,2,3),(9,4,1),(0,5,8))
    print(get_hash(lis))


def get_hash(lis):
    matrix_hash = ""
    for i in range(3):
        for j in range(3):
            if (lis[i][j] == 0):
                matrix_hash = matrix_hash + str(1)
            else:
                matrix_hash = matrix_hash + str(lis[i][j])
    return matrix_hash


main()