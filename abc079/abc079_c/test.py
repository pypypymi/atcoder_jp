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
        input = """1222"""
        output = """1+2+2+2=7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0290"""
        output = """0-2+9+0=7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3242"""
        output = """3+2+4-2=7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  A, B, C, D = list(input())
  Ai, Bi, Ci, Di = int(A), int(B), int(C), int(D)
  if Ai + Bi + Ci + Di == 7:
      print(f'{Ai}+{Bi}+{Ci}+{Di}=7')
  elif Ai + Bi + Ci - Di == 7:
      print(f'{Ai}+{Bi}+{Ci}-{Di}=7')
  elif Ai + Bi - Ci + Di == 7:
      print(f'{Ai}+{Bi}-{Ci}+{Di}=7')
  elif Ai + Bi - Ci - Di == 7:
      print(f'{Ai}+{Bi}-{Ci}-{Di}=7')
  elif Ai - Bi + Ci + Di == 7:
      print(f'{Ai}-{Bi}+{Ci}+{Di}=7')
  elif Ai - Bi + Ci - Di == 7:
      print(f'{Ai}-{Bi}+{Ci}-{Di}=7')
  elif Ai - Bi - Ci + Di == 7:
      print(f'{Ai}-{Bi}-{Ci}+{Di}=7')
  elif Ai - Bi - Ci - Di == 7:
      print(f'{Ai}-{Bi}-{Ci}-{Di}=7')
