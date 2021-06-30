"""
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

Sarah Langleben sml343, Nicole Yatskar ny73
10/16/2020
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.

    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # 255-rgb.red instead of rgb.red... rgb.red is the RGB color
    #the 255- makes it the complementary
    
    return introcs.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.

    The decimal point counts as one of the five characters.

    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.

    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending
    # on how big value is. Look at the examples in the specification.

    newvalue = 1.0

    if value < 10:
        newvalue = round(value, 3)
    elif value < 100:
        newvalue = round(value, 2)
    elif value >= 100:
        newvalue = round(value, 1)

    if value == 100:
        newvalue = format(newvalue,'.1f')
    if float(newvalue) < 100 and float(newvalue) >= 10:
        newvalue = format(newvalue, '.2f')
    if float(newvalue) < 10:
        newvalue = format(newvalue, '.3f')

    return str(newvalue)


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".

    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)

    Example: if str(cmyk) is

          '(0.0,31.3725490196,31.3725490196,0.0)'

    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.

    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    c = cmyk.cyan
    m = cmyk.magenta
    y = cmyk.yellow
    k = cmyk.black
    return('('+str5(c)+', '+str5(m)+', '+str5(y)+', '+str5(k)+')')


def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".

    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)

    Example: if str(hsv) is

          '(0.0,0.313725490196,1.0)'

    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.

    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value

    return('(' + str5(h) + ', ' + str5(s)+ ', ' + str5(v) + ')')


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.

    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """

    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.

    r = (rgb.red/255.0)
    g = (rgb.green/255.0)
    b = (rgb.blue/255.0)
    rgb = (r,g,b)

    k = 1-max(r,g,b)

    if k == 1:
        c = 0
        m = 0
        y = 0
    if k != 1:
        c = (1-r-k)/(1-k)
        m = (1-g-k)/(1-k)
        y = (1-b-k)/(1-k)

    cmyk = introcs.CMYK(c*100,m*100,y*100,k*100)

    return(cmyk)


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk

    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html

    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0.
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()

    cyan = cmyk.cyan / 100
    magenta = cmyk.magenta / 100
    yellow = cmyk.yellow / 100
    black = cmyk.black / 100

    r = (1 - cyan)*(1-black)
    g = (1-magenta)*(1-black)
    b = (1-yellow)*(1-black)

    r = r*255
    g = g*255
    b = b*255

    r = round(r)
    g = round(g)
    b = round(b)
    rgb = introcs.RGB(r,g,b)

    return(rgb)


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.


    r = rgb.red/255.0
    g = rgb.green/255.0
    b = rgb.blue/255.0

    M = max(r,g,b)
    m = min(r,g,b)

    if M == m:
        h = 0
    elif M == r and g>=b:
        h = 60.0*(g-b)/(M-m)
    elif M == r and g<b:
        h = 60.0*(g-b)/(M-m)+360.0
    elif M == g:
        h = 60.0*(b-r)/(M-m)+120.0
    elif M == b:
        h = 60.0*(r-g)/(M-m)+240.0

    if M == 0:
        s = 0
    else:
        s = 1-m/M

    v = M

    hsv = introcs.HSV(h,s,v)
    return(hsv)


def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value
    hsv = (h,s,v)

    H = math.floor(h/60)
    f = h/60-H
    p = v*(1-s)
    q = v*(1-f*s)
    t = v*(1-(1-f)*s)

    if H == 0 or H == 5:
        r = v
    elif H == 1:
        r = q
    elif H == 2 or H == 3:
        r = p
    elif H ==4:
        r = t

    if H == 0:
        g = t
    elif H == 1 or H == 2:
        g = v
    elif H == 3:
        g = q
    elif H == 4 or H ==5:
        g = p

    if H==0 or H ==1:
        b = p
    elif H == 2:
        b = t
    elif H == 3 or H == 4:
        b = v
    elif H == 5:
        b = q

    rgb = introcs.RGB(round(r*255), round(g*255), round(b*255))
    return(rgb)


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast

    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart,
    with all values becoming 0 or 1 when contrast = 1.

    Parameter value: the value to adjust
    Precondition: value is a float in 0..1

    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    x = value
    c = contrast

    if x < 0.25 + 0.25*c:
        y = ((1-c)/(1+c)) * x

    elif x > 0.75 - 0.25*c:
        y = ((1-c)/(1+c))*(x - ((3-c)/4)) + ((3+c)/4)

    else:
        y = (1+c)/(1-c) * (x - (1+c)/4) + (1-c)/4

    if c == 1 and x >= 0.5:
        y = 1

    return(y)


def contrast_rgb(rgb,contrast):

    """
    Applies the given contrast to the RGB object rgb

    This function is a PROCEDURE.  It modifies rgb and has no return value.
    It should apply contrast_value to the red, blue, and green values.

    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object

    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    r = contrast_value((rgb.red/255),contrast)
    g = contrast_value((rgb.green/255),contrast)
    b = contrast_value((rgb.blue/255),contrast)

    rgb.red = round(r*255)
    rgb.green = round(g*255)
    rgb.blue = round(b*255)

    rgb = rgb.red,rgb.green,rgb.blue
