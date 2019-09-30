import math

def getprefixinString(r,y,g,b,inputs):
    res =True
    R=r
    Y=y
    G=g
    B=b
    # print(res)
    # print(inputs)


    if len(inputs) == 0: return res
    if inputs[0] =='R': R=R+1
    if inputs[0] =='Y': Y=Y+1
    if inputs[0] =='G': G=G+1
    if inputs[0] =='B': B=B+1

    if abs(R-G)>1: return res & False
    if abs(Y-B)>1: return res & False

    return res & getprefixinString(R,Y,G,B,inputs[1:])



print(getprefixinString(0,0,0,0,"YGYGRBRB"))
print(getprefixinString(0,0,0,0,"RYRB"))
print(getprefixinString(0,0,0,0,"RGGR"))
print(getprefixinString(0,0,0,0,"RYBG"))