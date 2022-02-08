# return masked string
def maskify(cc):
    if len(cc) < 5:
        return cc
    else:
        return '#' * (len(cc) - 4) + cc[-4:]
    pass