
def counter(a,b):
    set_a = set(str(a))
    set_b = set(str(b))
    return len(set_a&set_b)
