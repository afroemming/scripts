def permute(lst):
    k, l = 0, 0
    perms = [lst[:]]
    while any([lst[i] < lst[i+1] for i, x in enumerate(lst[:-1])]):
        for i, e in enumerate(lst[:-1]):
            if lst[i] < lst[i+1]:
                k = i
        for i, e in enumerate(lst):
            if lst[k] < lst[i]:
                l = i
        lst[k], lst[l] = lst[l], lst[k]
        lst = lst[:k+1] + list(reversed(lst[k+1:]))
        perms.append(lst[:])
    return perms


