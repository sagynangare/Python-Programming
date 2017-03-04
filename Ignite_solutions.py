"""To Map A -> D, m ->p likewise
    String is string parameter
    String parameter can be string or para or word
"""
import string
def String_Amaze(String):
    NewString = ' '
    for word in String:
        if word == ' ':
            Ascii = ord(word)
        else:
            for pun in string.punctuation:
                if word == pun:
                    Ascii = ord(word)
                    break
                """To read each character of string then convert it into ASCII value
                with a function ord of python and subtract 3 from it and again
                convert it to character using chr function"""
            Ascii =(ord(word) - 3)
        """If there's paragraph to convert which consists of numbers then we do
        have isdigit() function of python and isalpha() as well."""
        if word.isdigit():
            Ascii = ord(word)
        if word.isspace():
            Ascii = ord(word)
            """string consists of Capital and small letters the solution is to
            compare ASCII value of each character is in range of capital letters
            i.e. 65 - 90 and lower characters range i.e. 97 - 122.
                To check character is upper or lower case python come with isupper() and
                islower() function"""
        if word.isalpha():
            if ((word.isupper() and Ascii > 90) or (word.islower() and Ascii > 122)):
                Ascii = Ascii - 26
                if ((word.isupper() and Ascii < 65) or (word.islower() and Ascii < 97)):
                    Ascii = Ascii + 26
        NewString = NewString + chr(Ascii)
    print ("Output=> ", NewString)
                                
String = raw_input('Enter the String = ')
String_Amaze(String)
