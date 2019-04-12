# Remember to reach out for help after your own due diligence

def analyze_text(text):
    # Your code here
    charCount = 0
    eCount = 0
    text = text.lower()
    for char in text:
        if char.isalpha():
            charCount+=1
            if char == 'e':
                eCount+=1
    return f"The text contains {charCount} alphabetic characters, of which {eCount} ({100*eCount/charCount:0.2f}%) are 'e'."
