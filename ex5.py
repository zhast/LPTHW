name = 'Steven Z. Zhang'
age = 18
height = 180 # Centimeters 
weight = 175 # Pounds
eyes = 'Dark Brown'
teeth = 'White'
hair = 'Brown'

# The f character in the function lets you plug in a variable with curly brackets 
print(f"Let's talk about {name}.") # In this case, its name
print(f"He's {height} centimeters tall")
print(f"He's {height/2.54} inches tall")
print(f"He's {weight} pounds heavy")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")