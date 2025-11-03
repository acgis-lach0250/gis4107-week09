#-------------------------------------------------------------------------------
# Name:        test_dict_list_utils.py
#
# Purpose:     Test functions for functions in dict_list_utils.py
#
# Author:      David Viljoen
#
# Created:     20/10/2021
# Last update: 31/10/2022
#-------------------------------------------------------------------------------

import dict_list_utils as dlu


def test_get_missing_keys():
    dict_ref = {1: 1, 2: 2, 3: 3}
    dict_to_compare = {2: 2}
    expected = [1, 3]
    actual = dlu.get_missing_keys(dict_ref, dict_to_compare)
    assert expected == actual


def test_get_missing_keys_with_count():
    dict_ref = {1:1, 2:2, 3:3}
    dict_to_compare = {1:1, 2:2, 3:3}
    expected = (0, [])  
    actual = dlu.get_missing_keys_with_count(dict_ref, dict_to_compare)
    assert expected == actual


def test_get_unique():
    in_list = [1, 2, 2, 3]  
    expected = [1, 2, 3]   
    actual = dlu.get_unique(in_list)
    assert expected == actual


def test_flatten_list():
    in_list = [1, (2, 3), [4, 5]]  
    expected = [1, 2, 3, 4, 5]     
    actual = dlu.flatten_list(in_list)
    assert expected == actual
