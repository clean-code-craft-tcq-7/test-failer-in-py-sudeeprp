
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


assert(size(5) == 'error')
assert(size(37) == 'S')
assert(size(38) == 'M')  # we are asserting that our customer prefers a relaxed fit
assert(size(40) == 'M')
assert(size(43) == 'L')
print("All is well (maybe!)")
