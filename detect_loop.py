def has_loop(d):
    visited = set()
    key = next(iter(d))
    while key in d:
        if key in visited:
            return True
        visited.add(key)
        key = d[key]
    return False

int(has_loop({1:8, 2:7, 3:6, 4:5}))