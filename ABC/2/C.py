x1, y1, x2, y2, x3, y3 = map(int, input().split())

ans = abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)) / 2
print(ans)
