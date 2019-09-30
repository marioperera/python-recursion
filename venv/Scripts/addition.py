x =[1,2,3,4,5,6,7,8,9,0]

def rec_addition(array):
    if len(array) ==0:
        return 0
    if len(array) ==1: return array[0]
    else:
        return array[0] +rec_addition(array[1:])


print(rec_addition(x))
val =0
