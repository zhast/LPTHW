# Variable cars has value of 100
cars = 100

# Space in car has value of 4.0 floating point 
space_in_car = 4.0

# There are 30 whole drivers
drivers = 30

# There are 90 whole passengers
passengers = 90

# Free cars are cars that do not have drivers. Assumed 1 driver per car
cars_not_driven = cars - drivers

# Every car driven has the same amout of drivers 
cars_driven = drivers

# The total capacity of the cars driven is the number multiplied by the volume in each car
carpool_capacity = cars_driven * space_in_car

# The average passengers in a car is the number of passsengers per car split among the cars driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars availalbe.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "Empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, 'to carpool today.')
print("We need to put about", average_passengers_per_car, "in each car.")