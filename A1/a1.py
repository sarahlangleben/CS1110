"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Authors: Sarah Langleben (sml343), Nicole Yatskar (ny73)
Date: 9/30/2020
"""
import introcs


def before_space(s):

    """Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    This is in testA
    """
    return s[:s.find(" ")]


def after_space(s):

    """Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    This is in testA
    """

    return s[s.find(" ")+1:]


def first_inside_quotes(s):

    """first_inside_quotes(s)
    Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it.  We typically use single quotes (') to delimit a
    string if want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C',
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes"""

    start = s.find('"')
    tail = s[start+1:]
    end = tail.find('"')
    value = tail[:end]
    return value


def get_src(json):

    """"
    Returns the src value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "src". For example, if the JSON is

    '{ "src":"1 Bitcoin", "dst":"9916.0137 Euros", "valid":true, "err":"" }'

    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """

    start = json.index('c":')
    substring = json[start+2:]
    return first_inside_quotes(substring)


def get_dst(json):

    """"Returns the dst value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "dst". For example, if the JSON is

    '{ "src":"1 Bitcoin", "dst":"9916.0137 Euros", "valid":true, "err":"" }'

    then this function returns '9916.0137 Euros' (not
    '"9916.0137 Euros"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """

    start = json.index('t":"')
    substring1 = json[start+2:]
    return first_inside_quotes(substring1)


def has_error(json):

    """
    Returns True if the query has an error; False otherwise.

    Given a JSON response to a currency query, this returns the
    opposite of the value following the keyword "valid". For example,
    if the JSON is

    '{ "src":"", "dst":"", "valid":false, "err":"Currency amount is invalid." }'

    then the query is not valid, so this function returns True (It
    does NOT return the message 'Source currency code is invalid').

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """

    return json.find('false') != -1


def currency_response(old, new, amt):

    """Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the
    currency dst. The response should be a string of the form

    '{ "src":"<old-amt>", "dst":"<new-amt>", "valid":true, "err":"" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "valid" will be followed by the value false (and "err" will have
    an error message).

    Parameter old: the currency on hand (the SRC)
    Precondition: old is a string with no spaces or non-letters

    Parameter new: the currency to convert to (the DST)
    Precondition: new is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float"""
    base = 'http://cs1110.cs.cornell.edu/2020fa/a1/?'
    url = base + 'from='+ old + '&to=' + new + '&amt=' + str(amt)
    return introcs.urlread(url)


def is_currency(code):

    """
    Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters.
    """

    return has_error(currency_response(code, 'USD', 1.0)) != True


def exchange(old, new, amt):

    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to
    the currency dst. The value returned represents the amount
    in currency dst.

    The value returned has type float.

    Parameter old: the currency on hand (the SRC)
    Precondition: old is a string for a valid currency code

    Parameter new: the currency to convert to (the DST)
    Precondition: new is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """

    x = currency_response(old, new, amt)
    value = get_dst(x)
    y = before_space(value)
    return float(y)
