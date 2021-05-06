from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN")

input("? ")

print("Opening the file...")
target = open(filename, 'w') # Open the file in write (w) mode
print("Truncating the file. Goodbye!")
target.truncate() # Delete the contents of the file

print("Now I'm going to ask you for three lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

# The .write class function writes a string to the file object
print("I'm going to write these lines to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() # Close saves changes to the files



print("The file says: \n{}".format(open(filename, 'r').read()))