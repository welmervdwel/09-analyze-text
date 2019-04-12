from analyze_text import analyze_text

test_cases = [
    {
        "input": "Eeeee",
        "output": "The text contains 5 alphabetic characters, of which 5 (100.00%) are 'e'."
    },
    {
        "input": "Blueberries are tasteee!",
        "output": "The text contains 21 alphabetic characters, of which 7 (33.33%) are 'e'."
    },
    {
        "input": "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)",
        "output": "The text contains 55 alphabetic characters, of which 0 (0.00%) are 'e'."
    },
]

def test_analyze_text():
    for test_case in test_cases:
        analyze_text_response = analyze_text(test_case['input'])
        assert analyze_text_response == test_case[
            'output'], f"\nFor Input: {test_case['input']} \nExpected: {test_case['output']} \nGot:      {analyze_text_response}"
