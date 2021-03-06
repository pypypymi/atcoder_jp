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
        input = """3
3 4 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
4 4 8 2 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
8 8 7 7 6 6 5 5"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  from collections import Counter
  n = int(input())
  a = Counter(map(int, input().split()))
  print(sorted(a.items(),key=lambda x:(x[1],x[0]))[0][0])
