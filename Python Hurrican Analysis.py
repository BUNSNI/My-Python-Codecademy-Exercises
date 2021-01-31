# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


#function to strip away 'B' and 'M' from damages data
new_damages = []

def updated_damages(data):
    M = 'M'
    B = 'B'
    for x in data:
        if x == 'Damages not recorded':
            new_damages.append(x)
        elif M in x:
            new_text = x.strip('M')
            million = float(new_text) * 1000000
            new_damages.append(million)
        elif B in x:
            new_text = x.strip('B')
            billion = float(new_text) * 1000000000
            new_damages.append(billion)
        
    print(new_damages)
    
updated_damages(damages)


#function that constructs a dictionary made out of the lists above
hurricanes = {}

def dicter(list1):
    for n, m, y, mx, area, damg, dths in zip(names, months, years, max_sustained_winds, areas_affected, new_damages, deaths):
        list_dict = {n: {'Name': n, 'Month': m, 'Year': y, 'Max-Wind': mx, 'Area': area, 'Damage': damg, 'Deaths': dths}}
        hurricanes.update(list_dict)
    
dicter(names)

print(hurricanes)

#function that converts current dictionary of hurricanes to a new dictionary where the keys are years and the values are lists containing a dictionary for each hurricane.

def dictionary_year(dict):
    hurricanes_by_year = {}
    years = []
    for item in dict.values():
        if item['Year'] not in years:
            years.append(item['Year'])
    for x in years:
        hurricane_by_year = {x : []}
        hurricanes_by_year.update(hurricane_by_year)
    for i in hurricanes_by_year:
        for value in dict.values():
            if i == value['Year']:
                hurricanes_by_year[i].append(value)
        
    print("Here is a dictionary of hurricanes by order of year: " + str(hurricanes_by_year))

dictionary_year(hurricanes)

#Function storing in a dictionary areas affected and how many times each one is affected
count_of_areas_affected = {}

def count(dict):
    for list in areas_affected:
        for x in list:
            if x not in count_of_areas_affected:
                count_of_areas_affected[x] = 1
            else:
                count_of_areas_affected[x] += 1
            
    print(count_of_areas_affected)

count(hurricanes)

#function that identifies area affected the most by hurricanes
def most_affected(areas_affected):
    max_count = 0
    area = []
    for i in count_of_areas_affected:
        if count_of_areas_affected[i] > max_count:
            max_count = count_of_areas_affected[i]
            area.append(i)
        
    print("The worst area affected is " + area[0] + " a total of " + str(max_count) + " times.")

most_affected(count_of_areas_affected)

#function to find the hurricane that caused the greatest number of deaths and how many it caused

hurricanes_and_deaths = dict(zip(names, deaths))
def no_deaths(arg):
    most_deaths = 0
    area = []
    for x in arg:
        if arg[x] > most_deaths:
            most_deaths = arg[x]
            area.append(x)
            
    print(x + " caused the most deaths, at: " + str(most_deaths))

no_deaths(hurricanes_and_deaths)


#function that rates hurricanes on a mortality scale

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def decide_scale(arg):
    mortality_dictionary = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5: []}
    for i in arg:
        if arg[i] == 0:
            mortality_dictionary[0].append({i})
        elif arg[i] > 0 and arg[i] <= 100:
            mortality_dictionary[1].append({i})
        elif arg[i] > 100 and arg[i] <= 500:
            mortality_dictionary[2].append({i})
        elif arg[i] > 500 and arg[i] <= 1000:
            mortality_dictionary[3].append({i})
        elif arg[i] > 1000 and arg[i] <= 10000:
            mortality_dictionary[4].append({i})
        else:
            mortality_dictionary[5].append({i})
    
    print("This is the mortality scale: " + str(mortality_dictionary))
        
decide_scale(hurricanes_and_deaths)


#function that finds the hurricane that caused the greatest damage, and how costly it was.

Hurricane_damages = dict(zip(names, new_damages))

def greatest_damage(arg):
    damage_cost = 0
    area = []
    for i in arg:
        if isinstance(arg[i], str):
            arg[i] = 0
        if arg[i] > damage_cost:
                damage_cost = arg[i]
                area.append(i)
            
    print("The hurricane that caused the greatest damage was " + i + ", at a cost of: $" + str(damage_cost))

greatest_damage(Hurricane_damages)


#function that rates hurricanes on a damage scale

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def cost_scale(arg):
    damage_ratings = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : []}
    for i in arg:
        if isinstance(arg[i], str):
            arg[i] = 0
        if arg[i] == 0:
            damage_ratings[0].append({i})
        elif arg[i] > 0 and arg[i] <= 100000000:
            damage_ratings[1].append({i})
        elif arg[i] > 100000000 and arg[i] <= 1000000000:
            damage_ratings[2].append({i})
        elif arg[i] > 1000000000 and arg[i] <= 10000000000:
            damage_ratings[3].append({i})
        elif arg[i] > 10000000000 and arg[i] <= 50000000000:
            damage_ratings[4].append({i})
        else:
            damage_ratings[5].append({i})

    print(damage_ratings)


cost_scale(Hurricane_damages)