def russian_peasnt(a,b):
    if a==0: return 0
    if(a%2 ==0): return 2*russian_peasnt(a/2,b)
    else: return b+russian_peasnt((a-1)/2,b)

russian_peasnt(234567,45678)