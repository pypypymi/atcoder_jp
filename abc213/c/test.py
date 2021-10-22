import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """4 5 2
3 2
2 5"""
        output = """2 1
1 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000 1000000000 10
1 1
10 10
100 100
1000 1000
10000 10000
100000 100000
1000000 1000000
10000000 10000000
100000000 100000000
1000000000 1000000000"""
        output = """1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  from bisect import bisect_left
  h,w,n = map(int,input().split())
  cards = [tuple(map(int,input().split())) for _ in range(n)]

  anum = list(set(x for x,_ in cards))
  bnum = list(set(y for _,y in cards))

  anum.sort()
  bnum.sort()

  for a,b in cards:
    ca = bisect_left(anum,a)
    cb = bisect_left(bnum,b)
    print(ca+1,cb+1)

