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
        input = """0601889"""
        output = """6881090"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """86910"""
        output = """01698"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """01010"""
        output = """01010"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s= list(input())[::-1]
  for i,s_i in enumerate(s):
    if(s_i=="6"):s[i]=9
    elif(s_i=="9"):s[i]=6
  s = list(map(str,s))
  print("".join(s))