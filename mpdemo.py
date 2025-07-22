import time
import multiprocessing

def mysleep(n):
  print(f'sleeping for {n}')
  time.sleep(n)


def main():
  l = [1, 2, 3, 2, 4, 2, 3, 5, 3, 2]
  pool = multiprocessing.Pool(4)
  pool.map(mysleep, l)


if __name__ == '__main__':
  main()
