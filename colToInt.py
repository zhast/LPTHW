# This program is used to convert the column letter in 
# CSV files into the number column index starting at 
# A = 0 for use in functions such as .iloc[<row>,<column>]


col = input("Enter Column Letter: ")

while(col != '0'):
    first = col[0] 
    first = first.lower() # Convert to lowercase for consistency 
    first = ord(first) - 97 # Convert char to int where A/a = 0

    try:
        second = col[1]
        second = second.lower()
        second = ord(second) - 71
    except: 
        second = 0

    if(second == 0):
        print(f"Column index: {first}")
    else:
        print(f"Column index: {(first * 26) + second}")


    col = input("Enter Column Letter: ")


