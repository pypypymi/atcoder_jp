s = list(input())
s2 = list("yahoo")
s.sort()
s2.sort()
print("YES") if "".join(s) == "".join(s2) else print("NO")