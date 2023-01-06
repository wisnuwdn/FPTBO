import init

grammar = init.init_grammar('cnf.txt')


def find_rule(exp):
    global grammar
    if exp == []:
        return []

    tmp = []
    for item in exp:
        for key in grammar:
            if item in grammar.get(key):
                tmp.append(key)

    return tmp


def concat(s1, s2):
    if s1 == [] or s2 == []:
        return []

    tmp = []
    for i in s1:
        for j in s2:
            tmp.append(i + ' ' + j)

    return tmp


def cyk_alg(s):
    s = s.split(" ") # pecah string menjadi list berdasarkan kata
    n = len(s) # jumlah kata
    table = [[[] for i in range(n)] for j in range(n)] # buat tabel

    # loop untuk row 1
    for i in range(n):
        table[i][i] = find_rule([s[i]])

    # rumus cyk: V(i,j) = V(i-k[-(x)],j) * V(i, j+k[x-1])
    # where k = range(1,loop)
    # where x = range(loop)

    # n = 5
    for loop in range(2, n+1): # 2, 3, 4, 5
        k = range(1, loop) # [1]
        for i in range(loop-1, n): # 1, 2, 3, 4
            for j in range(n - loop+1): # 0, 1, 2, 3
                for x in range(1, loop):
                    table[i][j] += find_rule(concat(table[i-k[-x]][j], table[i][j+k[x-1]]))
                    # cetak tabel masing-masing sel
        #print(table)
        # cetak tabel per row

    # cetak tabel setelah selesai
    for row in table:
        print(row)

    if table[n-1][0] == []:
        print("\nstring not valid")
    else:
        print("\nstring is valid")

    return table
