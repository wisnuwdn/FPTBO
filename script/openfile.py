def open_file(filename):
    # prepare the empty list
    inf = []
    # open txt with read mode
    with open(filename, 'r') as file:
        # read rule line by line
        data = file.readlines()

        # append each rule into data list while remove the new line
        for rule in data:
            inf.append(rule.strip('\n'))

    # return the raw cnf rules
    return inf
