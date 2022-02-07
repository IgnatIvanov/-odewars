def solution(number):
    mul_3_5 = []
    sum = 0
    for i in range(number):
        mul_3_5.append(0)
    i = 1
    while i * 3 < len(mul_3_5):
        mul_3_5[i*3] = 1
        i += 1
    i = 1
    while i * 5 < len(mul_3_5):
        mul_3_5[i*5] = 1
        i += 1
    for i in range(len(mul_3_5)):
        if mul_3_5[i]:
            sum += i
    return sum        
  