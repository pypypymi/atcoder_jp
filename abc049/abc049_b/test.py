import sys
from io import StringIO
import unittest

def resolve():
  h,w = map(int,input().split())
  c = [input() for i in range(h)]
  for i in range(h):
    print(c[i])
    print(c[i])

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
        input = """2 2
*.
.*"""
        output = """*.
*.
.*
.*"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 4
***."""
        output = """***.
***."""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9 20
.....***....***.....
....*...*..*...*....
...*.....**.....*...
...*.....*......*...
....*.....*....*....
.....**..*...**.....
.......*..*.*.......
........**.*........
.........**........."""
        output = """.....***....***.....
.....***....***.....
....*...*..*...*....
....*...*..*...*....
...*.....**.....*...
...*.....**.....*...
...*.....*......*...
...*.....*......*...
....*.....*....*....
....*.....*....*....
.....**..*...**.....
.....**..*...**.....
.......*..*.*.......
.......*..*.*.......
........**.*........
........**.*........
.........**.........
.........**........."""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

