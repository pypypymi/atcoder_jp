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
        input = """2
3
4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
4
10"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  x = int(input())
  y = int(input())
  z = int(input())
  print(1) if x+y< z+0.5 else print(0)