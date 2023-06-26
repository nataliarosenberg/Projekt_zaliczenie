import random


def heapify(tab: list, i: int, n: int) -> list:
    left = 2 * i
    right = 2 * i + 1
    mx = i
    if (left <= n and tab[left] > tab[i]): mx = left
    if (right <= n and tab[right] > tab[mx]): mx = right

    if mx != i:
        tab[i], tab[mx] = tab[mx], tab[i]
        heapify(tab, mx, n)


def buildMaxHeap(tab: list) -> list:
    n = len(tab) - 1
    for i in range(n // 2 + 1, 0, -1):
        heapify(tab, i, n)
    return tab


def heapsort(tab) -> list:
    h = buildMaxHeap([0] + tab)
    n = len(tab)
    while n >= 1:
        h[1], h[n] = h[n], h[1]
        n -= 1
        heapify(h, 1, n)
    return h[1:][::-1]
