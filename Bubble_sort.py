def Bubble_sort(tab):
    n = len(tab)
    while n > 1:
        change = False
        for i in range(0, n - 1):
            if tab[i] > tab[i+1]:
                tab[i], tab[i+1] = tab[i+1], tab[i]
                change = True

        n -= 1
        print(tab)
        if change == False:
            break

    return tab

