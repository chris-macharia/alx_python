def pow(a, b):
    # Base case: anything raised to the power of 0 is 1
    if b == 0:
        return 1

    # Initialize the result to 1
    result = 1

    # If b is negative, calculate the reciprocal of a
    if b < 0:
        a = 1 / a
        b = -b

    # Multiply a to the result b times
    for _ in range(b):
        result *= a

    return result

