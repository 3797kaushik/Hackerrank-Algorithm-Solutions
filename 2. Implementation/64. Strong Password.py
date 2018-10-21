#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    #Its length is at least 6.
    #It contains at least one digit.
    #It contains at least one lowercase English character.
    #It contains at least one uppercase English character.
    #It contains at least one special character. The special characters are: !@#$%^&*()-+
    hasdigit=0;
    hasLower=0;
    hasUpper=0;
    hasSpecial=0;
    ar='!@#$%^&*()-+'
    for i in range(0,n):
        if password[i].isdigit():
            hasdigit=1
        if password[i].islower():
            hasLower=1
        if password[i].isupper():
            hasUpper=1
        if any([i1.__eq__(j1) for i1 in ar for j1 in password]):
            hasSpecial=1
    #print(str(hasdigit)+"==>"+str(hasLower)+"==>"+str(hasUpper)+"==>"+str(hasSpecial))            
    if  n>= 6:        
        return 4-(hasdigit+hasLower+hasUpper+hasSpecial)
    else :
        t1=4-(hasdigit+hasLower+hasUpper+hasSpecial)
        if n+t1>=6:
            return t1
        else:
            return 6-n
    
    # Return the minimum number of characters to make the password strong
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
