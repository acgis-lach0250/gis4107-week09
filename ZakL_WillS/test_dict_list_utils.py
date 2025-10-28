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
    dict_ref = ''
    dict_to_compare = ''
    expected = ''
    actual = dlu.get_missing_keys(dict_ref, dict_to_compare)
    assert expected == actual


def test_get_missing_keys_with_count():
    dict_ref = ''
    dict_to_compare = ''
    expected = ''
    actual = dlu.get_missing_keys_with_count(dict_ref, dict_to_compare)
    assert expected == actual


def test_get_unique():
    in_list = ''
    expected = ''
    actual = dlu.get_unique(in_list)
    assert expected == actual


def test_flatten_list():
    in_list = ''
    expected = ''
    actual = dlu.flatten_list(in_list)
    assert expected == actual
