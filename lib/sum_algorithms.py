"""
Algorithms for summing lists with different time complexities.
"""

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def sum_list_nested(numbers):
    total = 0
    inner_iterations = 0
    for num in numbers:
        for _ in numbers:
            inner_iterations += 1
        total += num
    print(f"Total inner loop iterations: {inner_iterations}")
    return total
