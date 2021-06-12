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
        input = """4 10
2 6 3 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 10
1 9"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 100
1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n,p = map(int,input().split())
  a = list(map(int,input().split()))
  index=0
  while p>=a[index]:
    p-=a[index]
    index+=1
    if index==len(a):break
  print(index)