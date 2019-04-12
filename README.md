# analyze_text
:heavy_exclamation_mark: :heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark:
## HOMEWORK HERE A LITTLE DIFFERENT THAN IN THE TEXT BOOK.
### PLEASE ROUND RESULTS TO 2 DECIMAL PLACES
#### see example/info below
:heavy_exclamation_mark: :heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark::heavy_exclamation_mark:
> In order to avoid test-result errors depending on how rounding occurrs, please round to two decimal places like `0.2f` ... You can use str.format(), f-strings, or other, just know that if your submission fails and the decimals are off, this is likely the issue!

Write a function analyze_text that receives a string as input. Your function should count the number of alphabetic characters (a through z, or A through Z) in the text and also keep track of how many are the letter 'e' (upper or lowercase).

Your function should return an analysis of the text in the form of a string phrased exactly like this:

“The text contains 240 alphabetic characters, of which 105 (43.75%) are ‘e’.”

You will need to make use of the isalpha function, which can be used like this

```python
    "a".isalpha() # => evaluates to True
    "3".isalpha() # => evaluates to False
    "&".isalpha() # => False
    " ".isalpha() # => False

    mystr = "Q"
    mystr.isalpha() # => True
```
