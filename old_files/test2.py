import time

def matcopy(mat):
    cm = [row[:] for row in mat]

def main():
    arrtest = [12,3,13,2,3,1,4,11,1,4,5,14,67,8,9,4,0,7,1,2,4,6,9,15,4,9,5,8,1,5,2,3,5,6,1,7]
    matsetup = [[12,3,13,2,3,1],[4,11,1,4,5,14],[67,8,9,4,0,7],[1,2,4,6,9,15],[4,9,5,8,1,5],[2,3,5,6,1,7]]
    arr = []
    mat = []
    start_arr = time.time()
    for a in range(100000):
        cp = arrtest[:]
        arr.append(cp)
    end_arr = time.time()

    start_mat = time.time()
    for a in range(100000):
        cp = [row[:] for row in matsetup]
        arr.append(cp)
    end_mat = time.time()

    print(end_arr-start_arr)
    print(end_mat - start_mat)


main()