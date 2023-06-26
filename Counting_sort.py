def map_value(v, mn, mx):
    return v - mn


def countingsort(tab: list) -> list:
    r = [0] * len(tab)
    mn, mx = min(tab), max(tab)
    countarray = [0] * (mx - mn + 1)

    for e in tab:  # count occurences of each num
        countarray[map_value(e, mn, mx)] += 1

    for i in range(len(countarray) - 2, -1, -1):
        countarray[i] += countarray[i + 1]

    for e in tab[::-1]:
        countarray[map_value(e, mn, mx)] -= 1
        r[countarray[map_value(e, mn, mx)]] = e

    return r
