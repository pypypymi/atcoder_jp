w,a,b = map(int,input().split())
a_w = range(a,a+w+1)
b_w = range(b,b+w+1)
if len(set(a_w) & set(b_w))>=1:print(0)
elif a+w<b:print(abs(b-(a+w)))
else:print(abs(a-(b+w)))