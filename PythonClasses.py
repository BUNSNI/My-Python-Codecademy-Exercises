#Python Classes

class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print(self.name + "'s estimated insurance cost is $" + str(estimated_cost))

  def update_age(self, new_age):
    self.age = new_age
    print(self.name + " is now " + str(self.age) + " years old.")
    self.estimated_insurance_cost()
  
  def update_num_of_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children > 1 or self.num_of_children < 1:
      print(self.name + " has " + str(self.num_of_children) + " children.")
    else:
      print(self.name + " has " + str(self.num_of_children) + " child.")
    self.estimated_insurance_cost()
  
  def patient_profile(self):
    patient_information = {}
    patient_information['Name'] = self.name
    patient_information['Age'] = self.age
    patient_information['Sex'] = self.sex
    patient_information['BMI'] = self.bmi
    patient_information['No. of Children'] = self.num_of_children
    patient_information['Smoker'] = self.smoker
    return patient_information
  
  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    print("Looks like you, " + self.name + ", have a new BMI of: " + str(self.bmi))
    self.estimated_insurance_cost()


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_of_children(1)
patient1.update_bmi(24.5)
print(patient1.patient_profile())