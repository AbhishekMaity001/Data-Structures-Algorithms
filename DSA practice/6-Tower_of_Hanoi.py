def towerofhanoi(n, from_bar, aux_bar, to_bar):
    if n ==1:
        print("Move disk 1 from bar ", from_bar, " to bar ", to_bar)
        return
    towerofhanoi(n-1, from_bar, to_bar, aux_bar)
    print("Move disk ", n, " from bar ", from_bar, " to_bar ", to_bar)
    towerofhanoi(n-1, aux_bar, to_bar, from_bar)


if __name__ == '__main__':
    n=5
    towerofhanoi(n, "A", "B", "C")