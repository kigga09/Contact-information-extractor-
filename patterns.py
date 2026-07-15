import re
#we ll store in this folder all the necessary patterns

email = re.compile(r'''
(
    [a-zA-Z0-9._%+-]+      # Local part
    @                      # @ symbol
    [a-zA-Z0-9-]+          # First domain label
    (?:\.[a-zA-Z0-9-]+)*   # Optional subdomains
    \.[a-zA-Z]{2,}         # Top-level domain (com, org, co, uk, ...)
)
''', re.X)


phone_number = re.compile(r'''
(
\d{3}
[-. ]
\d{3}
[-. ]
\d{4}
)
''', re.X)

url = re.compile(r'''
(
(?:https?://|www\.)
[\w.-]+\.[a-zA-Z]{2,}
(?:/\S*)?
)
''', re.X)


month = [
    'january', 'february', 'march', 'april', 'may', 'june',
    'july', 'august', 'september', 'october', 'november', 'december',
    'jan', 'feb', 'mar', 'apr', 'may', 'jun',
    'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
]

date = re.compile(rf'''
(
    \d{{1,2}}/\d{{1,2}}/\d{{4}}
    |
    \d{{4}}/\d{{1,2}}/\d{{1,2}}
    |
    \d{{1,2}}\s(?:{"|".join(month)})\s\d{{4}}
    |
    \d{{4}}\s(?:{"|".join(month)})\s\d{{1,2}}
)
''', re.X | re.I)

time = re.compile(r'''
(
(?:[01]?\d|2[0-3]):(?:[0-5]\d)
|
(?:0?[1-9]|1[0-2]):(?:[0-5]\d)\s?(?:AM|PM)
)
''', re.X | re.I)
