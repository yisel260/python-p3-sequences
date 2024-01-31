#!/usr/bin/env python3



def print_fibonacci(length):
    my_fibonacci = [0, 1]
    a = 0
    b = 1

    if length <=0:
        print([])
        
    
    elif length == 1:
            print([my_fibonacci[0]])

    elif length >= 2:
        for _ in range(length - 2):
            my_fibonacci.append(a + b)
            a, b = b, a + b
        print(my_fibonacci)

    
        
        

    

   