#!/usr/bin/python3
import random
numberOriginal = random.randint(-10000, 10000)

if (numberOriginal < 0):
	number = abs(numberOriginal)
else:
	number = numberOriginal

last_digit = number % 10

print("Last digit of {} is {}".format(numberOriginal, last_digit), end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")

