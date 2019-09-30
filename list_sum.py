

def list_sum(list):
    val =0
    for element in list:
        if type(element) == type([]):
            val =val+list_sum(element)
        else:
            val= val+element
    return val

print(list_sum([1, 2, [3,4],[5,6]]))