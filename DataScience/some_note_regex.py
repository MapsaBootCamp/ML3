import re


# (*?, +?, ??) Adding ? after the quantifier makes it perform the match in non-greedy or minimal fashion
# (?:...) A non-capturing version of regular parentheses.
# (?=...) Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion. For example, Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.
# (?!...)
# (?(id/name)yes-pattern|no-pattern)

# print(re.findall(r"<.*?>(.*?)<\/.*?>", "<a >asihashfjd</a> <h1>ejgiehgie</h1>"))
# print(re.findall(
#     r"(\w+)@(\w+)\.([a-zA-Z]{2,3})", "ashkan@gmail.cm askjfhekhfekh reza@test.com"))

# print(re.findall(r"(?:\+98|0){1}9\d{9}(?:\b|$)",
#       "lkehkehg09121231234 elkhglkewhgehwl +989111236542"))

pattern = r"(?:(?:(?:\(\+98\))?)|(?:0?))?9\d{2}[- ]?\d{3}[- ]?\d{4}(?=[^\d]+)"
text = "(+98)9123334321 salam 00912 4321234 be man che 09121234543 sjkj 9121234321s"
print(re.findall(pattern, text))
