charset = ['a', 'b', 'c', 'd']
resset = []

# without printing arrays

def k_subsets(len_charachterset, number):
    if len_charachterset == number: return 1
    if number == 0:
        return 1

    else:
        return k_subsets(len_charachterset, number - 1) + k_subsets(len_charachterset - 1, number)


print(k_subsets(4,3 ))
