#-------------------------------------------------------------------------------
# Name:        world_pop_explorer_tests.py
#
# Purpose:     Test functions for functions in world_pop_explorer.py
#
# Author:      David Viljoen
#
# Created:     30/10/2021
# Last update: 31/10/2022
#-------------------------------------------------------------------------------

import world_pop_explorer as wpe

def test_get_country_count():
    expected = 233
    actual = wpe.get_country_count()
    assert expected == actual

def test_conv_num_with_commas_1000():
    expected = 1000
    number_text = "1,000"
    actual = wpe.conv_num_with_commas(number_text)
    assert expected == actual

def test_get_top_five_countries():
    expected = ['China', 'India', 'United States', 'Indonesia', 'Brazil']
    actual = wpe.get_top_five_countries()
    assert expected == actual

def test_set_country_to_pop():
    expected = (876562, 0.8)
    wpe.set_country_to_pop()
    actual = wpe.country_to_pop["Réunion"]
    assert expected == actual

def test_get_population_reunion():
    expected = 876562
    actual = wpe.get_population("Réunion")
    assert expected == actual

def test_get_continents():
    expected = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    actual = wpe.get_continents()
    assert expected == actual

def test_get_continent_populations():
    expected = True
    wpe.set_country_to_pop()
    actual = wpe.get_continent_populations()['Asia'] > 4.5 * (10 ** 9)
    assert expected == actual
