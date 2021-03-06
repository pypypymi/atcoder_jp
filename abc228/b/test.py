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
        input = """4 2
3 1 1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 12
7 11 10 1 7 20 14 2 17 3 2 5 19 20 8 14 18 2 10 10"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  N, X = map(int, input().split())
  A = [0]+list(map(int, input().split()))
  Y = [False]*(N+1)
  cnt = 0
  while Y[X] == False:
      Y[X] = True
      X = A[X]
      cnt += 1
  print(cnt)
