def descending_order(num):
    in_list = list(str(num))
    in_list.sort(reverse=True)
    return int("".join(in_list))