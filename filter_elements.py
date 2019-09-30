inputs = [4, 5, 2, 5, 4, 3, 1, 3, 4]
res = []
dict = {}


def filter_(res, dict, inputs, max):
    if len(inputs) == 0: return res
    if inputs[0] not in dict:
        dict[inputs[0]] = 1

    else:
        dict[inputs[0]] += 1
        if dict[inputs[0]] >= max:
            if inputs[0] not in res:
                res.append(inputs[0])

    filter_(res, dict, inputs[1:], max)
    return res


print(filter_(res, dict, inputs, 2))
for element in res:
    if element in inputs:
        print(element)
    break