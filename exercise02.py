# Exercise Two
# Write a simple program that finds the value at the nth position in the Fibonacci sequence

print("The value at the 6th postion in the Fibonacci sequence is 8")

def fibonacci(n): 
    if n == 0: 
        return 0
    if n == 1: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6))
