def persistence(n):
    num = n
    times = 0
    while num > 10:
        new_mul = 1
        for number in str(n):
            new_mul = new_mul * int(number)
        if new_mul < 10:
            return times + 1
        else:
            times += 1
            n = new_mul
    else:
        return times