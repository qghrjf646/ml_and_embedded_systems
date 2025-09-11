def compute_mean(l):
    r = 0
    s = len(l)
    if s == 0:
        return 0
    for i in l:
        r += i
    return r/4 # r/s
