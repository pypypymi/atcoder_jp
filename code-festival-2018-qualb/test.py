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
        input = """3"""
        output = """67"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """17"""
        output = """95"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """57"""
        output = """99"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  n = int(input())
  print(100-len([i for i in range(1,101) if i%n==0]))