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
        input = """5 3 20 15"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 10 100 1"""
        output = """1000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,a,x,y = map(int,input().split())
  print(a*x+(n-a)*y) if n>a else print(n*x)
