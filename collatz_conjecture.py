def steps(number):
    """ Calculates Collatz Conjecture """
    
    if number <= 0:
        raise ValueError('Only positive numbers are allowed')
   
    cnt = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            cnt += 1
        else:
            number = number * 3 + 1
            cnt += 1
    return cnt
