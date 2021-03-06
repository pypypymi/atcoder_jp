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
        input = """2
3 2
7 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 5 3
10 7 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
3 2 5
6 9 8"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    result = list(range(a[0],b[0]+1))
    for i in range(1,len(a)):
        result = set(result)& set(list(range(a[i],b[i]+1)))
    print(len(result))
