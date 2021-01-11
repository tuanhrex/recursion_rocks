# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
    # Write code here
    

    # Compute the nth term
    if n == 1:
        return n
    else: 
        return (factorial(n-1) * n)
    
    
    # cache the value and return it
    

print(factorial(5))
# => 120