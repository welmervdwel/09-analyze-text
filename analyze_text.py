# Remember to reach out for help after your own due diligence
# Remember to reach out for help after your own due diligence

def analyze_text(text):
    # Your code here
    count_char = 0
    count_e = 0

    for i in text:
        if i.isalpha() == True: # The following statements can be nested, because 'e'/'E' are in alphabet
            count_char += 1
            if i == "e" or i == "E": # use "or" statement, because they return the same
                count_e += 1

    percent_e = "%.2f" % ((count_e / count_char) * 100) # compute percent and cut at 2 decimals
    
    # Concatenate to get rid of ' and then use str() to avoid str/int error
    return ("The text contains " + str(count_char) + " alphabetic characters, of which " + str(count_e) + " (" + str(percent_e) + str("%) are 'e'."))
