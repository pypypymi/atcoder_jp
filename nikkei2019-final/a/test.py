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
        input = """4
4 1 3 3"""
        output = """4
6
8
11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
10 20 30 40 50"""
        output = """50
90
120
140
150"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
61049214 115057849 356385814 932678664 505961980 877482753 476308661 571830644 210047210 873430114"""
        output = """932678664
1438640644
2316123397
2792432058
3364262702
3720648516
4447740026
4804125840
4919183689
4980232903"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  from itertools import accumulate
  n = int(input())
  A = list(map(int, input().split()))
  B = [0] + list(accumulate(A))
  for k in range(n):
      print(max([B[i + k + 1] - B[i] for i in range(n - k)]))
      
      
      
