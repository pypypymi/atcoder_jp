A,D = map(int,input().split())
print((A+1)*D if (A+1)*D >= (A)*(D+1) else (A)*(D+1))