for i in range(1, 10):
    for j in range(i + 1, 10):
        print("{:02d}, {:02d}".format(i, j), end=", " if (i * 10 + j) < 89 else "\n")

