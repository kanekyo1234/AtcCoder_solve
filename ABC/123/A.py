a=[int(input()) for _ in range(5)]
k=int(input())
for i in range(4):  
    for j in range(i+1,5):
        if abs(a[i]-a[j])>k:
            
            print(":(")
            exit()
print("Yay!")