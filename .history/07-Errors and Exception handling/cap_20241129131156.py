'''
script to capitalize string
'''
def cap_text(str1):
    '''
    input a string to function cap_text
    output a capitalized string
    '''
    #print(str1.capitalize())
    #return str1.capitalize()
    #It turns out that the .capitalize() method only capitalizes the first letter of the first word in a string. Doing a little research on string methods, we find that .title() might give us what we want.
    return str1.title()
cap_text("hello")