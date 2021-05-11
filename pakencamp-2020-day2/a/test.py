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

    def test_入力例1(self):
        input = """4 3"""
        output = """4 7"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 5"""
        output = """5 10"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """98 99"""
        output = """99 197"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  a,b = map(int,input().split())
  print(max(a,b),a+b)