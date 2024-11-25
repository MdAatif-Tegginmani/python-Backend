def https_error (status):
    match status:
        case 400:
            return 'Bad'
        case 404:
            return 'Not found'
        case 418:
            return 'I am a tea'
        case _ :
            return 'Seomething is wrong'
        



def fib(n):
    a,b = 0,1
    while a<n:
        print(a)
        a,b = b , a+b
        print()



fib(10)


type casting

name = 'Aatif'
age = 25
cgpa = 6.75
is_student = False

# Write a Python script to calculate the factorial of a number (using a loop or recursion).

def facto(n):
    return 1 if(n==1 or n==0) else n * facto(n-1)

print(facto(5))

import math

def fac(n):
    return math.factorial(n)


print(fac(5))

#  using numPy

import numpy


n= 5
x= numpy.prod9([i for i in range(1,n+1)])
print(x)