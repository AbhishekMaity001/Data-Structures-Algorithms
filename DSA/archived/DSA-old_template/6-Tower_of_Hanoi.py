def towerofhanoi(n, from_bar, to_bar, aux_bar):
    """
    n-1 from A to B using C
    1 from A to C
    n-1 from B to C using A
    """
    if n == 1:
        print("Move disk 1 from bar ", from_bar, " to bar ", to_bar)
        return
    towerofhanoi(n-1, from_bar, aux_bar, to_bar)
    print("Move disk ", n, " from bar ", from_bar, " to_bar ", to_bar)
    towerofhanoi(n-1, aux_bar, to_bar, from_bar)


if __name__ == '__main__':
    n = 10
    towerofhanoi(n, "A", "C", "B")
