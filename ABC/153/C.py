n,k=map(int,input().split())
h=list(map(int,input().split()))
h.sort(reverse=True)
for i in range(min(k,n)):
    h[i]=0
print(sum(h))