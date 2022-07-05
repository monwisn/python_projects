# Binary numbers task

# Binary number can be represented by 0 or 1.
# Representation of binary numbers:

# 2^7  2^6 2^5 2^4 2^3 2^2 2^1 2^0
# 128 64  32  16  8  4  2  1
#  0   0   0   1  0  0  0  0 = 16
#  0   1   0   1  0  1  0  0 = 84

#  0   1   1   0  0  1  0  0 = 100 should be divided by 10

# Write a program that determines if any given binary number is divisible by 10

num = int(input('Enter your binary number (consisting of 0 and/or 1): '), 2)

if not num % 10:
    print(f"{num} is divided by 10")
else:
    print(f"{num} is not divided by 10")