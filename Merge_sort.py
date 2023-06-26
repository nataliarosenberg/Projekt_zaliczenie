def merge(l1: list, l2: list) -> list:
    r = []
    while l1 and l2:
        r.append(l1.pop(0) if l1[0] > l2[0] else l2.pop(0))
    r += l1
    r += l2
    return r


def mergesort(tab: list) -> list:
    l = len(tab)
    if l == 1:
        return tab
    return merge(mergesort(tab[:l // 2]), mergesort(tab[l // 2:]))
