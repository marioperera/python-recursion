
def convert_to_base(value,base):
    value =int(value)
    base =int(base)
    if value ==0: return "0"
    if(value ==1): return str(value)
    if(base ==10): return str(value)
    # value =value//base
    # print(value)
    else:
        return convert_to_base(value//base,base) +str(value%base)

print(convert_to_base(45,3))