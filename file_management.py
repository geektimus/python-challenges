def read_n_lines(path, n):
    with open(path) as f:
        for i in range(n):
            print(f.readline().strip())
