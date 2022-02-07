def count_bits(n):
    result = 0
    in_n = n
    for i in reversed(range(40)):
        if 2 ** i <= in_n:
            result += 1
            in_n -= 2 ** i
    return result