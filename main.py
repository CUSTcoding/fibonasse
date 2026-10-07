def fibonassei(f):
    a, b = 0, 1

    for _ in range(f):
        print(a)
        a,b = b, a +b
        c = b / a
        print(c)


fibonassei(20) 