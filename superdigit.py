def get_sum(digits):
    val = 0
    for digit in digits:
        val += int(digit)
    return val


def super_digit(values):
    if len(str(values)) == 1:
        return values
    else:
        return super_digit(get_sum(str(values)))


print(super_digit("148148148"))
