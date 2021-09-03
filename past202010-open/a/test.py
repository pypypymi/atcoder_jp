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
        input = """15 49 7"""
        output = """A"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """53 2 1"""
        output = """B"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,b,c = map(int,input().split())
  if a>b>c:print("B")
  elif a>c>b:print("C")
  elif b>a>c:print("A")
  elif b>c>a:print("C")
  elif c>a>b:print("A")
  else:print("B")
  

  