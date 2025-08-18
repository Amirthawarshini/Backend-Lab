import re
def reverse_vowels(s): return re.sub(
    r'([aeiouAEIOU])',
    lambda m, it=iter(re.findall(r'[aeiouAEIOU]', s)[::-1]): next(it),
    s
)