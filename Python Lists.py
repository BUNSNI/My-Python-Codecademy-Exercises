# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
names = ['Maria', 'Rohan', 'Valentina']
insurance_costs = [4150, 5320, 35210]
insurance_data = list(zip(names, insurance_costs))
estimated_insurance_data= []
estimated_insurance_data.append(('Maria', maria_insurance_cost))
estimated_insurance_data.append(('Rohan', rohan_insurance_cost))
estimated_insurance_data.append(('Valentina', valentina_insurance_cost))
print('Here is the actual insurance cost data: ' + str(insurance_data))
print('Here is the estimated insurance cost data: ' + str(estimated_insurance_data))

#codecademy Lists practise
#1
def append_sum(lst):
    sum = lst[-1] + lst[-2]
    lst.append(sum)
    sum = lst[-1] + lst[-2]
    lst.append(sum)
    sum = lst[-1] + lst[-2]
    lst.append(sum)
    return lst

print(append_sum([1,1,2]))

#2
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#3
def more_than_n(lst, item, n):
  times = lst.count(item)
  if times > n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#4
def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([23, 42, 108]))

#5
def combine_sort(lst1, lst2):
  lst3 = lst1 + lst2
  lst3.sort()
  return lst3

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#Advanced Lists exercises
#1
def every_three_nums(start):
  if start < 100:
    jump3 = list(range(start, 101, 3))
    return jump3
  elif start == 100:
    return [start]
  else:
    return []

print(every_three_nums(91))

#2
def remove_middle(lst, start, end):
    x = end + 1
    lst[start:x] = []
    return lst
    
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#3
def more_frequent_item(lst, item1, item2):
    x = lst.count(item1)
    y = lst.count(item2)
    if x >= y:
        return item1
    else:
        return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#4
def double_index(lst, index):
  list_length = len(lst) - 1
  if list_length >= index:
      replacement_value = lst[index] * 2
      lst[index] = replacement_value
      return lst
  else:
      return lst

print(double_index([3, 8, -10, 12], 5))

#5
def middle_element(lst):
    list_length = len(lst)
    if list_length % 2 == 0:
        x = list_length / 2
        y = x - 1
        sum = lst[int(x)] + lst[int(y)]
        return sum / 2
    else:
        x = list_length - 1
        return lst[int(x/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))