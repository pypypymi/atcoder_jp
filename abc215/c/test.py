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
        input = """aab 2"""
        output = """aba"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """baba 4"""
        output = """baab"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """ydxwacbz 40320"""
        output = """zyxwdcba"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s,k = input().split()
  k = int(k)
  s = list(s)
  import itertools
  l = sorted(set(itertools.permutations(s,len(s))))
  print("".join(l[k-1]))
