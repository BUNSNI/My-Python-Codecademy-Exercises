#basic loops
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
  print(game)

for sport in sport_games:
    print(sport)

#using Range in loops
promise = "I will not chew gum in class"

for i in range(5):
  print(promise)

#for loops
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for i in students_period_A:
  students_period_B.append(i)
  print(i)

print(students_period_B)

#using a loop to search through a list
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for x in dog_breeds_available_for_adoption:
  print(x)
  if x == dog_breed_I_want:
    print('They have the dog I want!')
    break

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for x in ages:
  if x < 21:
    continue
  print(x)

#while loops
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

x = 0
while x < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  x += 1

print(students_in_poetry)

#nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0
for location in sales_data:
  print(location)
  for x in location:
    scoops_sold += x
    print(scoops_sold)


heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coasters = []

for x in heights:
  if x > 161:
    can_ride_coasters.append(x)

print(can_ride_coasters)

#list comprehension SHORTHAND
can_ride_coaster = [x for x in heights if x > 161]

print(can_ride_coaster)

#2 shorthand python loops
celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [x * 9/5 + 32 for x in celsius]
print(fahrenheit)

#ways to construct loops

single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

for x in single_digits:
  squares.append(x * x)
  print(squares)

cubes = [x * x * x for x in single_digits]
print(cubes)

#Medical Insurance Porject

names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]
total_cost = 0

for x in actual_insurance_costs:
    total_cost += x
print(total_cost)

average_cost = total_cost / len(actual_insurance_costs)
print('Average insurance cost: $' + str(average_cost) + ' dollars')

for i in range(len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    print('The insurance cost for ' + names[i] + ' is ' + str(actual_insurance_costs[i]) + ' dollars.')
    if actual_insurance_costs[i] > average_cost:
        print('The insurance cost for ' + names[i] + ' is above average.')
    elif actual_insurance_costs[i] < average_cost:
        print('The insurance cost for ' + names[i] + ' is below average.')
    else:
        print('The insurance cost for ' + names[i] + ' is average.')

updated_estimated_costs = [x * 11/10 for x in estimated_insurance_costs]
print(updated_estimated_costs)

