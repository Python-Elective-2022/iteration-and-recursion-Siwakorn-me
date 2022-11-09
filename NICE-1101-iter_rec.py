"""
First function
Parameter: base and exponent
define function iterativePower
    set result equal to 1
    for power in range of exponent
        result is equal to result times base
    return result
"""


def iterativePower(base, exp):
    """
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    """

    result = 1
    for power in range(exp):
        result *= base
    return result


# Test case
for i in range(0, 5):
    n = iterativePower(3.3, i)
    print("n", n)

"""
Second function
Parameter: base and exponent
define function iterativePower
    if exponent equal to 0
        return 1
    else
        return base times base power exponent -1
"""


def recursivePower(base, exp):
    """
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    """

    if exp == 0:
        return 1
    else:
        return base * recursivePower(base, exp - 1)

#Test Case
for i in range(0, 5):
    n = recursivePower(3.3, i)
    print("n", n)
