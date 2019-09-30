def find_common_prefix(input1, input2):
    output = ""
    if len(input1) == 0:
        return ""
    elif len(input2) == 0:
        return ""
    elif input1[0] != input2[0]:
        return output
    else:
        return output + input2[0] + find_common_prefix(input1[1:], input2[1:])


replace_ = find_common_prefix("abracadabra", "abadabada")

print(replace_)
print("abracadabra".replace(replace_,""))
print("abadabada".replace(replace_,""))
