def first_non_repeat(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c in s:
        if freq[c] == 1:
            return c
    return None

print(first_non_repeat("aannvesshhaajjaaiinn")) 