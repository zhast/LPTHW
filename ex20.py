from sys import argv

script, input_file = argv

# Takes file f and loops through the bytes. 
# Once read, file must be "seeked"
def print_all(f):
    print(f.read())

# Seeks to the 0th byte (beginning of file)
def rewind(f):
    f.seek(0)

# Prints the line "line_count" using the function readline() on file f
# Readline reads one line, and the moves the cursor to the next line 
def print_a_line(line_count, f):
    print(line_count, f.readline(), end='')

# Temporarily rename the command "open(input_file, 'r')" to "current_file"
with open(input_file, 'r') as current_file:

    print("First let's print the whole file:\n")

    print_all(current_file)

    # Move the cursor back to byte 0
    rewind(current_file)

    print("Let's print three lines:")

    current_line = 1
    print_a_line(current_line, current_file)

    current_line = 1
    print_a_line(current_line, current_file)

    current_line += 67
    print_a_line(current_line, current_file)

