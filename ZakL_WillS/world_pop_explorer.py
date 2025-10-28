#-------------------------------------------------------------------------------
# Name:        world_pop_explorer.py
#
# Purpose:     Provide some functions to analyze the data in
#              world_pop_by_country.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
# Last update: 31/10/2022
#-------------------------------------------------------------------------------

from world_pop_by_country import data as country_pop

# Key = country name and 
# Value = population as a number (i.e. not text containing commas)
#
country_to_pop = dict()


def get_country_count():
    """Return the number of countries in country_pop.
    Assume data (country_pop) always has a header."""
    rows = country_pop.split('\n')
    return len(rows) - 1
    

def conv_num_with_commas(number_text):
    """Convert a number with commas (str) to a number.
       e.g. '1,000' would be converted to 1000"""
    return int(number_text.replace(',', ''))


def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""
    rows = country_pop.strip().split('\n')[1:]  # Skip header
    country_population_list = []
    
    for row in rows:
        columns = row.split('\t')
        country_name = columns[1]
        population = conv_num_with_commas(columns[5])
        country_population_list.append((country_name, population))
    
    # Sort by population in descending order
    country_population_list.sort(key=lambda x: x[1], reverse=True)
    
    top_five_countries = [country_population_list[i][0] for i in range(5)]
    return top_five_countries


def set_country_to_pop():
    """Sets the global country_to_pop dictionary where key is country name
         and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % decrease as a number
    """
    global country_to_pop
    country_to_pop = dict()
    rows = country_pop.split('\n')
    for row in rows[1:]:
        columns = row.split('\t')
        country_name = columns[1].strip()
        population_text = columns[5].strip()
        pct_decrease_text = float(columns[6].strip('+%'))

        pop_num = conv_num_with_commas(population_text)

        country_to_pop[country_name] = (pop_num, pct_decrease_text)
    
    


def get_population(country_name):
    """Given the name of the country, return the population as of 01Jul2017
       from country_to_pop.  If the country_to_pop is
       empty (i.e. no keys or values), then run set_country_to_pop
       to initialize it."""    
    if not country_to_pop:
        rows = country_pop.split('\n')[1:]  # Skip header
        for row in rows:
            columns = row.split('\t')
            name = columns[1]
            population = conv_num_with_commas(columns[5])
            country_to_pop[name] = population
    
    return country_to_pop.get(country_name)


def get_continents():
    """Return the list of continents"""
    rows = country_pop.strip().split('\n')[1:]  # Skip header
    continents = set()
    
    for row in rows:
        columns = row.split('\t')
        continent_name = columns[2]
        continents.add(continent_name)
    
    return sorted(list(continents))


def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
       the value is the total population of all countries on that continent"""

