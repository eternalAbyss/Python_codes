def factorial(n):
    if n== 0:
        return 1
    return n * factorial(n -1)

def factorial_with_logging(n, level=0):
    indent = "  " * level
    print(f"{indent}Calculate factorial({n})")
    
    if n == 0:
        print(f"{indent}Base case: factorial(0) = 1")
        return 1
    
    result = n * factorial_with_logging(n - 1, level + 1)
    print(f"{indent}Return: factorial({n}) = {n} × {result // n} = {result}")
    return result

# Test the function
print("Factorial with logging:", factorial_with_logging(5))