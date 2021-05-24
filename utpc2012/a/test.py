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
        input = """2012/12/02"""
        output = """yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000/01/01"""
        output = """no"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9999/12/31"""
        output = """no"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = input().split("/")
  y = list(s[0])
  md = list(s[1]+s[2])
  y.sort()
  md.sort()
  print("yes") if y==md else print("no")
  
  