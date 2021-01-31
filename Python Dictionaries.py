# Add your code here
medical_costs = {"Marina":6607.0, "Vinay":3225.0}
medical_costs.update({"Connie":8886.0, "Isaac":16444.0, "Valentina":6420.0})
medical_costs.update({"Vinay":3325.0})
print(medical_costs)

total_cost = 0
for k, v in medical_costs.items():
  total_cost += v
  average_cost = total_cost / len(medical_costs)
  
print("Average Insurance Cost: " + str(average_cost))

names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]
zipped_ages = zip(names, ages)
#print(list(zipped_ages))

names_to_ages = {k: v for k, v in zipped_ages}
print(names_to_ages)
marina_age = names_to_ages.get("Marina", None)
print("Marina's age is " + str(marina_age))

#Dictionary to create medical database
medical_records = {"Marina": {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}, "Vinay": {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}, "Connie": {"Age": 25.3, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}, "Isaac": {"Age": 35, "Sex": "Male", "BMI": 20.6 , "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}, "Valentina": {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}}
medical_records.pop("Vinay")
print(medical_records)

print("Connie's insurance cost is " + str(medical_records["Connie"]["Insurance_cost"]) + " dollars.")

for k, v in medical_records.items():
  print(k + " is a " + str(v["Age"]) + " year old " + v["Sex"] + " " + v["Smoker"] + " with a BMI of " + str(v["BMI"]) + " and insurance cost of " + str(v["Insurance_cost"]))