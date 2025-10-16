# YOUR CODE HERE
def max_product(digits):
    product = 1
    min_digit = min(digits)
    min_index = digits.index(min_digit)
    
    for i, digit in enumerate(digits):
        if i == min_index:
            product *= (digit + 1)
        else:
            product *= digit
    
    return product

t = int(input())

for _ in range(t):
    n = int(input())
    digits = list(map(int, input().split()))
    
    if 0 in digits:
        print(max_product(digits))
    else:
        original_product = 1
        for digit in digits:
            original_product *= digit
        
        increased_product = max_product(digits)
        
        print(max(original_product, increased_product))