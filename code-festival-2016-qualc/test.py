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
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """FESTIVALCODE"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """CF"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """FCF"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

def resolve():
  s = input()
  if "C" in s:
    c_i = s.index("C")
    result="No"
    for i in range(c_i+1,len(s)):
      if s[i]=="F":
        result="Yes"
        break
    print(result)
  else:
    print("No")