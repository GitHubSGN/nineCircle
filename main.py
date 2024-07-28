from matplotlib import pyplot as plt

CASE = 2

def n_circles(n):
    n_steps = [0] * (n+1)
    if CASE == 1:
        # case 1: 0, 1, 2, 5, 10, 21, 42, 85, 170, 341, ...
        n_steps[1] = 1
        i_start = 2
    elif CASE == 2:
        # case 2: 0, 1, 1, 4, 7, 16, 31, 64, 127, 256, ...
        n_steps[1] = 1
        n_steps[2] = 1
        i_start = 3
    else:
        raise ValueError("CASE Error: only be 1 or 2.")
    for i in range(n+1):
        if i>=i_start:
            n_steps[i] = 2 * n_steps[i-2] + n_steps[i-1] + 1
        print( f"f({i}) = {n_steps[i]}" )

    plt.title("n circles")
    plt.plot(n_steps, '--ro')
    plt.ylabel("steps")
    plt.xlabel("n")
    plt.show()


if __name__ == '__main__':
    n_circles(9)
