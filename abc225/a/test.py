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
        input = """aba"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ccc"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """xyz"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = list(input())
  from itertools import permutations
  print(len(set(permutations(s))))
