# This exercises teaches command line argument variables, or argv

from sys import argv

script, first, second, third = argv

print("This program is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)