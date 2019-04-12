from analyze_text import analyze_text

test_cases = [
    {
        "input": "Eeeee",
        "output": "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
    },
    {
        "input": "Blueberries are tasteee!",
        "output": "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
    },
    {
        "input": "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)",
        "output": "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
    },
]

def test_leap_year_test_cases():
    for test_case in test_cases:
        analyze_text_response = analyze_text(test_cases['input'])
        assert is_leap_year_response == test_case[
            1], f'For Input:\n{test_case["input"]} \mExpected: {test_case["output"]} \nGot: {analyze_text_response}'
