from sys import argv

script, filename = argv

# Open reads a file from path "filename" 
txt = open(filename) # Now txt is a "file object"

print(f"Here's your file {filename}: ")
print(txt.read()) # .read() converts file to string

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again).read()
print(txt_again)