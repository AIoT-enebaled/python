# Define the population of each country as a string with "M" for million
Uganda_pop = "40M"
Kenya_pop = "50M"
Nigeria_pop = "200M"
Tanzania_pop = "60M"
USA_pop = "300M"
Japan_pop = "126M"
Philippines_pop = "100M"
Brazil_pop = "200M"
Mexico_pop = "130M"
Rwanda_pop = "12M"

# Convert each population value to an integer in millions and add them up to get the total population
total_pop = (int(Uganda_pop[:-1]) + int(Kenya_pop[:-1]) + int(Nigeria_pop[:-1]) + int(Tanzania_pop[:-1]) + int(USA_pop[:-1]) + int(Japan_pop[:-1]) + int(Philippines_pop[:-1]) + int(Brazil_pop[:-1]) + int(Mexico_pop[:-1]) + int(Rwanda_pop[:-1])) * 1000000

# Print the total population of the world as a string
print("The total population of the world (excluding China and India) is " + str(total_pop) + " people.")
