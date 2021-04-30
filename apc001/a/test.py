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
        input = """8 6"""
        output = """16"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
    import math
    x,y = map(int,input().split())
    print(-1) if x%y==0 else print((x * y // math.gcd(x, y))-x)
