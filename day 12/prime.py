def is_prime(num):
    if num <= 1:
        return False  # 1 and below are not prime
    if num == 2:
        return True   # 2 is prime
    
    
    for i in range(2, num):
        if num % i == 0:      
# Step-by-Step Explanation:
# for i in range(2, num):
# This creates a loop where i takes all integer values from 2 up to num-1.
# Why start at 2? Because 1 divides every number, so we don’t need to check 1.
# Why go up to num-1? Because a number is divisible by itself, and we don’t need to check num.
# Example: If num = 7, i will be: 2, 3, 4, 5, 6
# if num % i == 0:
# % is the modulus operator, it gives the remainder of division.
# num % i == 0 means num is divisible by i with no remainder.
# If this is True → num is not a prime number, because prime numbers can only be divided by 1 and itself.
# Example:
# num = 4
# Loop runs: i = 2 → 4 % 2 == 0 → True → 4 is not prime
# Loop stops here because we already found a divisor.
# Summary:
# This loop checks every number between 2 and num-1 to see if num has a divisor.
# If it finds any divisor, the number is not prime.
# If it finishes the loop without finding a divisor, the number is prime.

            return False  # divisible by a number other than 1 and itself
    return True  # no divisors found, so it's prime

# Examples:
print(is_prime(73))  # True
print(is_prime(75))  # False
