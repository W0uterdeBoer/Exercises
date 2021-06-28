from graphics import *
import math

max_i = 100
Graph_sides = int(math.sqrt(max_i))
print("Graphsides= ", Graph_sides)
win = GraphWin("My bar", Graph_sides * 10, Graph_sides * 10)


def main2():
    all_divisors = finddivisors(max_i)[0]
    primes = finddivisors(max_i)[1]
    i = 0
    while i < max_i:
        assigncolor(i, all_divisors, primes)
        i += 1
    win.getMouse()  # pause for click in window
    win.close()


def finddivisors(max_i):
    primes = [2]
    divisors = []
    i = 0
    while i < max_i:
        i_divisors = []
        for k in primes:
            if div(i, k):
                i_divisors.append(k)
        if len(i_divisors) == 0:
            if i != 1:
                primes.append(i)
        divisors.append(i_divisors)
        i += 1
    return divisors, primes


def div(i, j):
    return i % j == 0


def assigncolor(i, all_divisors, primes):
    primecolors = colorscheme(primes)
    if len(all_divisors[i]) > 2:
        draw(i, color_rgb(165, 0, 165))
        print(i, (165, 0, 165))
    elif i in primes:
        red = primecolors[primes.index(i)][0]
        green = primecolors[primes.index(i)][1]
        blue = primecolors[primes.index(i)][2]
        draw(i, color_rgb(red, green, blue))

    else:
        k = 0

        for j in primes:
            if j in all_divisors[i]:
                k += 1
        if i != 1 and i != 0:
            red = primecolors[primes.index(all_divisors[i][0])][0]
            green = min(255, 50 * k)
            blue = primecolors[primes.index(all_divisors[i][0])][2]
            draw(i, color_rgb(red, green, blue))


def draw(i, colour):
    c = Rectangle(Point((i % Graph_sides) * 10, (i // Graph_sides) * 10),
                  Point(((i % Graph_sides) + 1) * 10, ((i // Graph_sides) + 1) * 10))
    c.setFill(colour)
    c.draw(win)


def colorscheme(primes):
    primecolors = []
    k = 0
    while k <= len(primes):
        primecolors.append([255 - int(k * 255 // len(primes)), 0, int(k * 255 // len(primes))])
        k += 1
    return primecolors


main2()
