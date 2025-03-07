#UNWSP Programming PythonCos2005DEsp25
#Week#7_Program#3 US Population
#03/7/2025
#Abraham. N. Andersen

#Have the user input (using a loop) various information that contains three pieces of data: year,
#name of state, and population.  Store all of this information in a list of lists.
# For example it might be stored like this:
#[[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
#Now have the user enter a year.  The program will add the populations from all states in the list
#of list for that year only.

# Initialize an empty list to store the data
data = []

# Loop to get user input
while True:
    year = input("Enter year (or type 'done' to finish): ")
    if year.lower() == 'done':
        break
    state = input("Enter state name: ")
    population = int(input("Enter population: "))  # Convert input to an integer
    data.append([int(year), state, population])  # Add the data as a list

# Get the year to calculate the total population
target_year = int(input("Enter the year to calculate total population: "))

# Calculate the total population for the target year
total_population = 0
for entry in data:
    if entry[0] == target_year:
        total_population += entry[2]

# Print the total population
print(f"Total population in {target_year}: {total_population}")