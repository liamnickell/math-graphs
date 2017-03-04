__author__ = 'github.com/liamnickell'

import math
from sys import argv 
import matplotlib.pyplot as plt


def main():
    theta_step = 0.01
    points = 10000

    thetas = []
    for i in range(points):
        thetas.append(i * theta_step)

    fig = plt.figure()
    ax = fig.gca(polar=True)

    if len(argv) > 1 and argv[1] == 'cos':
        if len(argv) == 2:
            ax.plot(thetas, rose_curve_cos(thetas))
        else:
            ax.plot(thetas, rose_curve_cos(thetas, n=float(argv[2])))
    elif len(argv) > 1 and argv[1] == 'sin':
        if len(argv) == 2:
            ax.plot(thetas, rose_curve_sin(thetas))
        else:
            ax.plot(thetas, rose_curve_sin(thetas, n=float(argv[2])))
    else:
        ax.plot(thetas, rose_curve_cos(thetas))

    ax.set_rlabel_position(0)
    plt.title("Rose Curve")

    plt.show()


def rose_curve_sin(thetas, a=10, n=3):
    r_vals = []
    for theta in thetas:
        # Not sure why, but for some reason even n values are not
        # graphed correctly in matplotlib unless negative r values
        # are eliminated.
        if n % 2 == 0:
            r = abs(a * math.sin(n * theta))
        else:
            r = a * math.sin(n * theta)

        r_vals.append(r)

    return r_vals


def rose_curve_cos(thetas, a=10, n=3):
    r_vals = []
    for theta in thetas:
        # Not sure why, but for some reason even n values are not
        # graphed correctly in matplotlib unless negative r values
        # are eliminated.
        if n % 2 == 0:
            r = abs(a * math.cos(n * theta))
        else:
            r = a * math.cos(n * theta)

        r_vals.append(r)

    return r_vals


if __name__ == '__main__':
    main()
