from sys import argv
from os.path import exists # returns a boolean to see if file exists or not

# Takes two command line arguemnts 
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# indata a string that has the contents of the from_file

# print(f"The input file is {len(indata)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input("RETURN / CTRL-C")

open(to_file, 'w').write(open(from_file).read())

print("File copied")

# Saves both files, no more changes being made
# out_file.close()
