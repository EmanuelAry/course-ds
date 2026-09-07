import sys

def fibonati(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        temp = a + b
        a = b
        b = temp

fibonati(int(sys.argv[1]))