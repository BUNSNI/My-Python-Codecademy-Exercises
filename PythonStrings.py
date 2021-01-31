company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]


first_name = "Bob"
last_name = "Daily"

fixed_first_name = 'R' + first_name[-2:]

#for loop through string searching for element
def letter_check(word, letter):
  for x in word:
    if x == letter:
      return True
  return False

print(letter_check('apple', 'l'))



#Python Strings: Medical Insurance Project

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

#print(medical_data)
def update_data(data):
  list_d = list(data)
  for i in range(len(list_d)):
    if list_d[i] == '#':
      list_d[i] = '$'
  return ''.join(list_d)

updated_medical_records = update_data(medical_data)
print(updated_medical_records)


def count(data):
  num_records = 0
  list_updated_data = list(updated_medical_records)
  for x in range(len(list_updated_data)):
    if list_updated_data[x] == '$':
      num_records += 1

  return num_records

print("There are " + str(count(updated_medical_records)) + " medical records in the data.")

medical_data_split = updated_medical_records.split(';')
print(medical_data_split)

medical_records = []
for x in medical_data_split:
  medical_records.append(x.split(','))
    
#print(medical_records)

medical_records_clean = []
for x in medical_records:
  record_clean = []
  for y in x:
    record_clean.append(y.strip())
  medical_records_clean.append(record_clean)

print(medical_records_clean)
for x in medical_records_clean:
  x[0] = x[0].upper()
  print(x[0])

names = []
ages = []
bmis = []
insurance_costs = []

for x in medical_records_clean:
  names.append(x[0])
  ages.append(x[1])
  bmis.append(x[2])
  insurance_costs.append(x[3])

print(names)
print(ages)
print(bmis)
print(insurance_costs)

total_bmi = 0
for x in bmis:
  total_bmi += float(bmis[x])
  average_bmi = total_bmis / len(bmis)
  print(average_bmi)

