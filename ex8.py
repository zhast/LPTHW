# Formatter is an empty string with four inputs 
formatter =  "{} {} {} {}"

# Formats the string formatter with integer inputs 1 2 3 and 4 
print(formatter.format(1, 2, 3, 4))

# The inputs for formatter are now the strings one two three four 
print(formatter.format("one", "two", "three", "four"))

# Booleans can also go into the formatter
print(formatter.format(True, False, False, True))

# You can put an empty formatter into the formatter
# In which case it'll just print empty format brackets
print(formatter.format(formatter, formatter, formatter, formatter))







