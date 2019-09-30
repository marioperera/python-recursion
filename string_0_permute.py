
def permute(input):
    output =""
    if(len(input)==0):return output
    else:
        return output+input[:2][1]+input[:2][0] +permute(input[2:])

print(permute("abcdpqrs"))