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
        input = """25 80"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """50 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 15"""
        output = """15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  l,x = map(int,input().split())  
  judge = x//l
  print(x-l*judge) if judge%2==0 else print(l-(x-l*judge))
