def trangular(n):
    if(n==0):return 0
    if(n==1): return 1
    else: return n+trangular(n-1)

print(trangular(12))
print(trangular(72))
print(trangular(662))