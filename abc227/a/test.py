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
        input = """3 3 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 100 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 14 2"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n, k, a = map(int, input().split())
  print(((k+a-2) % n)+1)

