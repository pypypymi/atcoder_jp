N,K,M = map(int, input().split())
A = list(map(int, input().split()))
if sum(A)>=(N*M):print("0")
elif N*M>sum(A) and (sum(A)+K>=N*M) :print((N*M)-sum(A))
else: print("-1")