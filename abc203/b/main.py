n,k = map(int,input().split())
print(sum([int("{}0{}".format(i,j)) for i in range(1,n+1) for j in range(1,k+1)]))