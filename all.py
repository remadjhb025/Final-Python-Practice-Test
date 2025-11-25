import sys
import math

#Question 1
def get_date_of_birth(id_number:str): 

    day = id_number[4,6]
    month = id_number[2,4]
    year = id_number[0,2]

    dob = day + "/" + month + "/" + year

    print(dob) 
    print("\n") 


#Question 2    
def get_gender(id_number):

    if id_number[6:11] < '5000':
       return "female"
    
    if id_number[7:11] > '4999':
       return "male"

print(get_gender())
   

#Question 3
# TODO: return shape from user input (it can't be blank and must be a valid shape!)     
def get_shape()-> str:
    # drawing different typees of shapes
    pass

#Question 4
def draw_triangle_multiplication(n: int):

    for i in range(n, n+1):
        i == n*i


    """
    STEP 10: Draw a triangle of multiplication table up to n
    Example for n = 5:
    1 
    2 4 
    3 6 9 
    4 8 12 16 
    5 10 15 20 25 
    """
    pass

#Question 5
def draw_pyramid(n: int):

    for i in range(n, n+1):
        return "*" * 2*n -1 
print("\n" + draw_pyramid(5) + "\n")
    # """
    # STEP 12: Draw a pyramid of height n using '*'
    # Example for n = 4:
    #    *
    #   ***
    #  *****
    # *******
    # """
    # pass

#Question 6
def fibonacci(n: int) -> int:

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5))

    # """
    # STEP 13: Return the nth Fibonacci number using recursion
    # The Fibonacci sequence is defined as follows:
    # F(0) = 0
    # F(1) = 1
    # F(n) = F(n-1) + F(n-2) for n > 1
    # """
    # pass

#Question 7
def fizz_buzz(n: int):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n
    
print(fizz_buzz()) 
   

#Question 8
def is_prime(n: int) -> bool:

    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):   #factors from 2 until the square root of n
        if n % i == 0:
            return False
    return True
    
print(is_prime())      
    # """
    # STEP 15: Return True if n is a prime number, False otherwise.
    # A prime number is a natural number greater than 1 that cannot be formed by
    # multiplying two smaller natural numbers.
    # """
    # pass

#Question 9
def factorial(n: int) -> int:

    return factorial(n)
print(factorial())

    # """
    # STEP 16: Return the factorial of n using recursion.
    # The factorial of a non-negative integer n is the product of all positive
    # integers less than or equal to n.
    # """
    # pass

#Question 10
def prime_triangle(n: int):

    
    """
    STEP 17: Draw a triangle of prime numbers up to n rows.
    Example for n = 5:
    2 
    3 5 
    7 11 13 
    17 19 23 29 
    31 37 41 43 47 
    """
    pass

#Question 11
def pascal_triangle(n: int):
    """
    STEP 19: Draw Pascal's triangle up to n rows.
    Example for n = 5:
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    """
    pass