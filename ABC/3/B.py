s=list(str(input()))
t=list(str(input()))
jagh=['a','t','c','o','d','e','r']
for i in range(len(s)):
    if s[i]!=t[i]:
        if s[i]=='@':
            if  t[i] not in jagh:
                print("You will lose")
                break
        elif t[i]=='@':
            if s[i] not in jagh:
                print("You will lose")
                break
        else:
            print("You will lose")
            break


else:
    print("You can win")