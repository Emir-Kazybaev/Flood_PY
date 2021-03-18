import time
from flood import Flood


def main():
    four = ['y', 'r', 'o', 'b', 'b', 'y', 'o', 'b', 'y', 'r', 'g', 'b', 'o', 'o', 'r', 'b']
    six = ['y', 'o', 'o', 'o', 'o', 'p',
           'r', 'o', 'g', 'b', 'p', 'o',
           'o', 'o', 'p', 'o', 'y', 'r',
           'b', 'g', 'y', 'b', 'g', 'y',
           'y', 'o', 'b', 'o', 'r', 'o',
           'b', 'r', 'g', 'y', 'p', 'b']
    seven = ['y', 'b', 'o', 'g', 'o', 'p', 'p',
             'g', 'r', 'g', 'b', 'p', 'o', 'y',
             'r', 'o', 'p', 'o', 'y', 'r', 'r',
             'b', 'g', 'y', 'b', 'g', 'y', 'r',
             'y', 'o', 'b', 'o', 'r', 'o', 'b',
             'b', 'r', 'g', 'y', 'p', 'b', 'g',
             'g', 'g', 'y', 'p', 'b', 'p', 'g', ]
    eight = ['y', 'y', 'o', 'g', 'o', 'p', 'p', 'r',
             'g', 'r', 'g', 'b', 'p', 'o', 'y', 'o',
             'r', 'o', 'p', 'o', 'y', 'r', 'r', 'b',
             'b', 'g', 'y', 'b', 'g', 'y', 'r', 'r',
             'y', 'o', 'b', 'o', 'r', 'o', 'b', 'b',
             'b', 'r', 'g', 'y', 'p', 'b', 'g', 'b',
             'g', 'g', 'y', 'p', 'b', 'p', 'g', 'o',
             'r', 'o', 'p', 'o', 'y', 'r', 'r', 'b', ]
    twelve = ['y', 'r', 'o', 'b', 'o', 'g', 'p', 'p', 'b', 'r', 'g', 'o', 'p', 'o', 'g', 'o', 'y', 'p', 'r', 'b', 'y',
              'r', 'r', 'r',
              'y', 'o', 'o', 'o', 'p', 'o', 'r', 'p', 'p', 'y', 'o', 'r', 'r', 'y', 'y', 'y', 'p', 'r', 'g', 'o', 'g',
              'y', 'o', 'g',
              'r', 'y', 'r', 'o', 'r', 'r', 'b', 'o', 'g', 'g', 'y', 'p', 'y', 'b', 'p', 'g', 'r', 'o', 'g', 'p', 'p',
              'p', 'g', 'b',
              'b', 'r', 'o', 'r', 'p', 'b', 'g', 'p', 'r', 'p', 'r', 'g', 'p', 'p', 'g', 'b', 'p', 'p', 'r', 'p', 'b',
              'g', 'p', 'p',
              'g', 'g', 'b', 'y', 'y', 'r', 'o', 'b', 'r', 'p', 'b', 'r', 'r', 'r', 'p', 'b', 'g', 'r', 'y', 'o', 'o',
              'g', 'r', 'p',
              'r', 'p', 'g', 'p', 'y', 'o', 'y', 'p', 'b', 'o', 'o', 'r', 'y', 'y', 'o', 'p', 'p', 'y', 'g', 'r', 'r',
              'g', 'b', 'b']
    start = time.time()
    flood = Flood(eight)
    flood.bfs()
    end = time.time()
    print("Time taken {}".format(end - start))


if __name__ == '__main__':
    main()
