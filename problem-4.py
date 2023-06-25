# https://projecteuler.net/problem=4
# Largest Palindrome Product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two
# 2-digit numbers is 9009 = 91 x 99
#
# Find the largest palindrome made from the product of two 3-digit numbers.

# get all the palindromes, sort them, and return the last value
palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if product == int(str(product)[::-1]):
            palindromes.append(product)
maxPalindrome = sorted(palindromes)[-1]

print(maxPalindrome)  # 906609

# in a list comprehension
maxPalindrome =\
    sorted([i * j for i in range(100, 1000) for j in range(100, 1000) if i * j == int(str(i * j)[::-1])])[-1]

print(maxPalindrome)  # 906609

# probably a bit faster
maxPalindrome = 0
for i in reversed(range(100, 1000)):
    for j in reversed(range(100, 1000)):
        product = i * j
        if product < maxPalindrome:
            break
        if product == int(str(product)[::-1]):
            maxPalindrome = product

print(maxPalindrome)  # 906609

# if we also want to know which numbers form the palindrome, we need to keep them around, could be in a data class
from dataclasses import dataclass, field


@dataclass(order=True)
class Palindrome:
    product: int = field(init=False, repr=False)
    i: int
    j: int

    def __post_init__(self):
        self.product = self.i * self.j

    def __str__(self):
        return f"""{self.i} * {self.j} = {self.product}"""


palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if product == int(str(product)[::-1]):
            palindromes.append(Palindrome(i, j))
maxPalindrome = sorted(palindromes)[-1]

print(maxPalindrome)  # 993 * 913 = 906609

# or in a tuple
palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if product == int(str(product)[::-1]):
            palindromes.append((i, j, product))
maxPalindrome = sorted(palindromes, key=lambda a: a[2])[-1]

print(f"{maxPalindrome[0]} * {maxPalindrome[1]} = {maxPalindrome[2]}")  # 993 * 913 = 906609
