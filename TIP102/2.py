# Problem 1: Most Endangered Species

# Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns the species with the highest conservation priority based on its population.

# The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated with a species, including its name, habitat, and wild population. The function should return the name of the species with the lowest population.

# If there are multiple species with the lowest population, return the species with the lowest index.

# def most_endangered(species_list):
#     pass

# Example Usage:

# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 72
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10
#     }
# ]

# print(most_endangered(species_list))

# Example Output:

# Vaquita

def most_endangered(species_list):
    if not species_list:
        return None
    
    most_endangered = species_list[0]
    lowest_pop = species_list[0]["population"]
    
    for species in species_list:
        if species["population"] < lowest_pop:
            most_endangered = species
            lowest_pop = species["population"]

    return(most_endangered["name"])
            


species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

print()

"""
As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, represented by the string observed_species. Each character in observed_species denotes a species observed in the region.

# Your task is to determine how many instances of the observed species are also considered endangered.

# Note: Species are case-sensitive, so "a" is considered a different species from "A".

# Write a function to count the number of endangered species observed.

# def count_endangered_species(endangered_species, observed_species):
#     pass

# Example Usage:

# endangered_species1 = "aA"
# observed_species1 = "aAAbbbb"

# endangered_species2 = "z"
# observed_species2 = "ZZ"

# print(count_endangered_species(endangered_species1, observed_species1)) 
# print(count_endangered_species(endangered_species2, observed_species2))  

# Example Output:

# 3 # `a` and `A` are endangered species. `a` appears once, and `A` twice.
# 0
"""

def count_endangered_species(endangered_species, observed_species):
    species_set = set(endangered_species)
    count = 0

    for species in observed_species:
        if species in species_set:
            count += 1
    
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1))
print(count_endangered_species(endangered_species2, observed_species2))

print()

"""
In a wildlife research station, each letter of the alphabet represents a different observation point laid out in a single row. Given a string station_layout of length 26 indicating the layout of these observation points (indexed from 0 to 25), you start your journey at the first observation point (index 0). To make observations in a specific order represented by a string observations, you need to move from one point to another.

The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|.

Write a function that returns the total time it takes to visit all the required observation points in the given order with one movement.

def navigate_research_station(station_layout, observations):
  pass

Example Usage:

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

Example Output:

45
4
Example 2 explanation: The index moves from 0 to 2 to observe 'c', then to 1 for
'b', then to 0 again for 'a'.
Total time = 2 + 1 + 1 = 4.
"""
new_dict

def navigate_research_station(station_layout, observations):
    for index, station in enumerate(station_layout):
        


station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))