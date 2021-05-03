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
        input = """CODEFESTIVAL"""
        output = """CODE FESTIVAL"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """POSTGRADUATE"""
        output = """POST GRADUATE"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """ABCDEFGHIJKL"""
        output = """ABCD EFGHIJKL"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = input()
  print(s[:4]+" " +s[4:])