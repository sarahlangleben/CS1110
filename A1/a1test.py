"""
Test script for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Authors: Sarah Langleben (sml343), Nicole Yatskar (ny73)
Date: 9/30/2020
"""

import introcs
import a1


def testA():
    """
    Test procedure for Part A: tests before_space() and after_space()
    """
    #test case returns word before space

    #testing for one space in between two words
    introcs.assert_equals("3",a1.before_space("3 Euros"))

    #testing for multiple non-adjacent spaces
    introcs.assert_equals("3",a1.before_space("3 Cuban Pesos"))

    #testing for multiple non-adjacent spaces
    introcs.assert_equals("400",a1.before_space("400 Papuan New Guinean Kinas"))

    #testing for multiple adjacent spaces
    introcs.assert_equals('',a1.before_space(' yeehaw'))

    #testing for string with no letters, just spaces
    introcs.assert_equals('',a1.before_space(' '))

    #testing for one space in between two words
    introcs.assert_equals("Euros",a1.after_space("3 Euros"))

    #testing for multiple non-adjacent spaces
    introcs.assert_equals("Cuban Pesos",a1.after_space("3 Cuban Pesos"))

    #testing for multiple non-adjacent spaces
    introcs.assert_equals("Papuan New Guinean Kinas",a1.after_space(
    "400 Papuan New Guinean Kinas"))

    #testing for multiple adjacent spaces
    introcs.assert_equals('yeehaw',a1.after_space(' yeehaw'))

    introcs.assert_equals(' ',a1.after_space('palabra  '))


def testB():
    """
    Test procedure for Part B
    tests first_inside_quotes(),
    get_src(json), get_dst(json), and has_error(json)
    """
    #test case returns characters inside first instance of double quotes
    introcs.assert_equals('new york', a1.first_inside_quotes('"new york" city'))
    introcs.assert_equals('', a1.first_inside_quotes('p""ool'))
    introcs.assert_equals('e', a1.first_inside_quotes('n"e"w"w'))
    #test case returns characters after "src" inside first double quotes
    introcs.assert_equals('1 Bitcoin', a1.get_src
    ('{ "src":"1 Bitcoin", "dst":"9916.0137 Euros", "valid":true, "err":"" }'))

    #test case returns characters after "dst" inside first double quotes
    introcs.assert_equals('9916.0137 Euros', a1.get_dst(
    '{ "src":"1 Bitcoin", "dst":"9916.0137 Euros", "valid":true, "err":"" }'))

    #test case returns True if query has an error. false otherwise.
    introcs.assert_equals(True, a1.has_error(
    '{ "src":"", "dst":"", "valid":false, "err":"Currency amount is invalid." }'))

    introcs.assert_equals(False, a1.has_error(
    '{ "src":"", "dst":"", "valid":true, "err":"Currency amount is invalid." }'))



def testC():
    """
    Test procedure for Part C
    Tests currency_response()
    """

    #Test case returns JSON string that is a response to a currency query
    introcs.assert_equals('{ "src":"2.5 United States Dollars"'+
    ', "dst":"64.375 Cuban Pesos", "valid":true, "err":"" }',
    a1.currency_response('USD', 'CUP', 2.5))

    introcs.assert_equals('{ "src":""'+
    ', "dst":"", "valid":false, "err":"Source currency code is invalid." }',
    a1.currency_response('', '', 2.5))


def testD():
    """
    Test procedure for Part D: tests is_currency(code) and exchange(old,new,amt)
    """
    #test case returns True if code is a valid (3 letter code for a) currency
    introcs.assert_equals(True, a1.is_currency('CUP'))

    #test case returns False if code is an invalid (3 letter code for a) currency
    introcs.assert_equals(False, a1.is_currency('ABC'))

    #test case returns the amount of currency received in the given exchange.
    introcs.assert_floats_equal(64.375, a1.exchange('USD','CUP', 2.5))
    introcs.assert_floats_equal(1.0, a1.exchange('AWG','AWG', 1.0))


#call test procedures
testA()
testB()
testC()
testD()
print('Module a1 passed all tests.')
