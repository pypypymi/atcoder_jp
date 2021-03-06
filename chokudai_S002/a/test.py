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
3 4
1000000000 1
111111111 111111111"""
        output = """12
1000000000
12345678987654321"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  from functools import reduce
  n = int(input())
  print(*[reduce(lambda x,y:x*y,map(int,input().split())) for i in range(n)], sep='\n')