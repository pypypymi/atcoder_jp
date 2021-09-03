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
        input = """AbC
ABc"""
        output = """case-insensitive"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """xyz
xyz"""
        output = """same"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """aDs
kjH"""
        output = """different"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = input()
  t = input()
  print("same") if s == t else print(
      "case-insensitive") if s.lower() == t.lower() else print("different")
