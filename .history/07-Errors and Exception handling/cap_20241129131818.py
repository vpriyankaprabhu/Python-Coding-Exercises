'''
script to capitalize string
'''
def cap_text(text):
    '''
    input a string to function cap_text
    output a capitalized string
    '''
    #return text.capitalize()
    print(text.title())
    #It turns out that the .capitalize() method only capitalizes the first letter of the first word in a string. 
    #Doing a little research on string methods, we find that .title() might give us what we want.
    #return text.title()

    return text.capwords()
cap_text("hello")
