def steps(number):
    
    if number <= 0:
        raise ValueError('Only positive numbers are allowed')
    else:
        zaehler = 0
        while (number !=1):
            if((number%2)==0):
                number = number//2
                zaehler +=1
            else:
                number = (number*3)+1
                zaehler +=1
        return zaehler
