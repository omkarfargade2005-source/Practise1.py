"""
for i in range(1, 6):
    print(i)
"""

"""
for i in range(1, 11):
    print(i) 
"""

"""
for i in range(5, 0, -1):
    print(i)
    """

"""
for i in range(2, 21, 2):
    print(i)
    """

"""
for i in range(1, 20, 2):
    print(i)
    """

"""
for i in range(1, 11):
    print(2 * i)
    """

"""
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)
    """

"""
for ch in "Python":
    print(ch)
    """

"""
fruits = ["apple", "mango", "banana"]

for fruit in fruits:
    print(fruit)
    """

"""
for i in range(1, 6):
    print(i ** 2)
    """

"""
i = 1
while i <= 5:
    print(i)
    i += 1
    """

"""
i = 10
while i >= 1:
    print(i)
    i -= 1
    """

"""
i = 2
while i <= 10:
    print(i)
    i += 2
    """

"""
i = 1
while i < 10:
    print(i)
    i += 2
    """

"""
i = 1
while i <= 5:
    print("Hello")
    i += 1
    """

"""
i = 3
while i <= 30:
    print(i)
    i += 3
"""

"""
i = 1
while i <= 10:
    print(i, i ** 2)
    i += 1
    """

"""
i = 1
while i <= 5:
    print(i ** 3)
    i += 1
    """

"""
i = 1
while i <= 5:
    print(i)
    i += 1
    """

"""
i = 1
while i <= 20:
    print(i)
    i += 4
    """

"""
total = 0
for i in range(1, 11):
    total += i
print(total)
"""

"""
total = 0
for i in range(2, 21, 2):
    total += i
print(total)
"""

"""
total = 0
for i in range(1, 11, 2):
    total += i
print(total)
"""

"""
fact = 1
for i in range(1, 6):
    fact *= i
print(fact)
"""

"""
for i in range(1, 11):
    print(7 * i)
    """

"""
n = 12345
count = 0

while n > 0:
    count += 1
    n //= 10

print(count)
"""

"""
n = 1234
total = 0

while n > 0:
    total += n % 10
    n //= 10

print(total)
"""

"""
n = 1234
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print(rev)
"""

"""
for i in range(1, 11):
    print(4 * i)
    """


"""
result = 1

for i in range(3):
    result *= 2

print(result)
"""

"""
for i in range(1, 31):
    if i % 3 == 0:
        print(i)
        """

"""
for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        print(i)
        """

"""
count = 0

for i in range(1, 51):
    if i % 2 == 0:
        count += 1

print(count)
"""

"""
nums = [-2, 5, 0, 8, -1]

for n in nums:
    if n > 0:
        print(n)
        """

"""
nums = [4, 9, 2, 15, 6]
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print(largest)
"""

"""
word = "education"
count = 0

for ch in word:
    if ch in "aeiou":
        count += 1

print(count)
"""

"""
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
        """

"""
for i in range(1, 11):
    if i == 5:
        break
    print(i)
    """

"""
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
    """

"""
n = 7
prime = True

if n < 2:
    prime = False

for i in range(2, n):
    if n % i == 0:
        prime = False
        break

print(prime)"""

"""
for i in range(1, 6):
    print("*" * i)
    """

"""
for i in range(5, 0, -1):
    print("*" * i)
    """
'''
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    '''

"""
for i in range(1, 6):
    print(str(i) * i)
    """

"""
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()"""

"""
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
        """

"""
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()
    """

"""
for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)
    """

"""
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
    """