types_of_people = 10
x = "There are {} types of people."

binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}."

print(x.format(types_of_people))
print(y)

print(f"I said: {x.format(types_of_people)}")
print(f"I also said: '{y}'")

# Python recognizes that the variable is of type boolean
hilarious = False

# A string with a format box inside it. 
joke_evaluation = "Isnt' that joke so funny?! {}"
print(joke_evaluation.format(hilarious)) # No longer possible to use f to format. Must use "".format"

L = "This is the left side of..."
R = "a string with a right side."

# Must print without brackets 
print(L + R)



