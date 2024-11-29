'''
script to capitalize string
'''
import string

def cap_text(text):
    '''
    input a string to function cap_text
    output a capitalized string
    '''
    #return text.capitalize()
    print(text.capwords())
    #It turns out that the .capitalize() method only capitalizes the first letter of the first word in a string. 
    #Doing a little research on string methods, we find that .title() might give us what we want.
    #return text.title()

    #In Python, string capwords() method is used to capitalize all the words in the string using split() method.
    return string.capwords(text, sep="'")
cap_text("hello")
