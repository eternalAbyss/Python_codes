import time
import numpy as np
from typing import Callable, Any

num1 = 11
num2 = num1 

print(num2)

num1 = 22
print(num2)

num2 = 33 
print(num1)

def find_big_o_notation(function_name: Callable, *args, **kwargs) -> str:
    """
    Estimates the Big O Notation of a function by measuring execution time across different input sizes.
    
    Args:
        function_name: The function to analyze
        *args, **kwargs: Arguments to pass to the function
        
    Returns:
        str: The estimated Big O notation
    """
    # Define different input sizes to test
    sizes = [1000, 2000, 4000, 8000, 16000]
    times = []
    
    for size in sizes:
        # Generate appropriate input based on the size
        # This is a simplified approach - you might need to adapt for your specific function
        inputs = kwargs.copy()
        inputs['n'] = size  # Assuming the function accepts an 'n' parameter
        
        # Measure execution time
        start_time = time.time()
        function_name(*args, **inputs)
        end_time = time.time()
        
        times.append(end_time - start_time)
    
    # Analyze time complexity based on growth patterns
    # Calculate ratios between consecutive measurements
    ratios = [times[i+1]/times[i] for i in range(len(times)-1)]
    avg_ratio = sum(ratios) / len(ratios)
    
    # Determine the complexity based on the average ratio
    if avg_ratio <= 1.2:
        return "O(1) - Constant time"
    elif avg_ratio <= 1.7:
        return "O(log n) - Logarithmic time"
    elif avg_ratio <= 2.1:
        return "O(n) - Linear time"
    elif avg_ratio <= 2.5:
        return "O(n log n) - Linearithmic time"
    elif avg_ratio <= 4.1:
        return "O(n²) - Quadratic time"
    elif avg_ratio <= 8.1:
        return "O(n³) - Cubic time"
    else:
        return "O(2^n) - Exponential time or worse"
    
