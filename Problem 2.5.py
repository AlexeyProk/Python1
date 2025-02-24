



#Implement a recursive function to calculate the factorial of a non-negative integer.
#Instructions:
#Write a recursive function    factorial(n) that returns the factorial of the non-negative integer    n.
#The factorial of    n (denoted as    n!) is defined as:
#n! = n * (n-1)! for n > 0
#0! = 1
#Write test cases to verify the function works correctly for different values of    n.



def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# ✅ Test Cases
print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(7))
