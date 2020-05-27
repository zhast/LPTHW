from sys import argv

script, filename = argv

txt = open(filename) # Opens file, now txt is a "file object"

print(f"Here's your file {filename}: ")
print(txt.read()) # .read() converts file to string?

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again).read()
print(txt_again)