# Remember to reach out for help after your own due diligence

def analyze_text(text):
    # Your code here
    count_char = 0
    count_e = 0

    for i in text:
        if i.isalpha() == True: # the following statements can be nested, because 'e'/'E' are in alphabet
            count_char += 1
            if i == "e" or i == "E":
                count_e += 1

    percent_e = float((count_e / count_char) * 100) # compute percent after obtaining the responses
    
    return ("The text contains " + str(count_char) + " alphabetic characters, of which " + str(count_e) + " (" + str(percent_e) + str("%) are 'e'."))

# Note that depending on whether you use str.format or string concatenation
# your code will pass different tests. As long as your code passes either
# tests 1-3 OR tests 4-6, yo'll be okay. See below for more details.
from test import testEqual

# Tests 1-3: solutions using string concatenation should pass these
text1 = "Eeeee"
answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
testEqual(analyze_text(text1), answer1)

text2 = "Blueberries are tasteee!"
answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
testEqual(analyze_text(text2), answer2)

text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
testEqual(analyze_text(text3), answer3)

# Tests 4-6: solutions using str.format should pass these
text4 = "Eeeee"
answer4 = "The text contains 5 alphabetic characters, of which 5 (100%) are 'e'."
testEqual(analyze_text(text4), answer4)

text5 = "Blueberries are tasteee!"
answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."
testEqual(analyze_text(text5), answer5)

text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer6 = "The text contains 55 alphabetic characters, of which 0 (0%) are 'e'."
testEqual(analyze_text(text6), answer6)
