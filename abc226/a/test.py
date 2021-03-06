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
        input = """3.456"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """99.500"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0.000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


def resolve():
  from decimal import Decimal, ROUND_HALF_UP
  x = float(input())
  a = Decimal(str(x))
  b = a.quantize(Decimal('0'), rounding=ROUND_HALF_UP)
  print(b)

