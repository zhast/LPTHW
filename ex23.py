import sys # Lets you use argv

script, encoding, error = sys.argv

# New function 
def main(language_file, encoding, errors):
    line = language_file.readline() # Read the first line of the language file

    if line: # If line is true, there is content. If no content, line = 0
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip() # Move on to the next line
    raw_bytes = next_lang.encode(encoding, errors = errors) # 
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

    