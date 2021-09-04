travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(new_country, new_visits, new_cities):
	new_dictionary = {}

	new_dictionary["country"] = new_country
	new_dictionary["visits"]  = new_visits
	new_dictionary["cities"]  = new_cities

	travel_log.append(new_dictionary)





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
print("*-*-*-*-*-*-*-\n")
print("You have visited", travel_log[2]["country"])
print("You have visited", travel_log[2]["cities"][1])



