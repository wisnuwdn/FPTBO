# note, when passing parameter to this func. find_rule("word") without end space. Not find_rule("word ")
def find_rule(word):
    # initialize rules
    grammar = {}
    file = 'grammar.txt'
    with open(file, 'r') as a_file:
        for line in a_file:
            if len(line) > 3:
                # create empty list for each key
                if line.split(" -> ")[0] not in grammar.keys():
                    grammar[line.split(" -> ")[0]] = []

                line = line.replace("\n", "")
                grammar[line.split(" -> ")[0]].append(line.split(" -> ")[1])

    #initialize words
    # file = "words.txt"
    # with open(file, 'r') as a_file:
    #     for line in a_file:
    #         line = line.replace("\n", "")
    #         if "NP" in line.split(" -> "):
    #             kata = line.split(" -> ")[1]
    #             for words in kata:
    #                 grammar["NP"].append(words)
    #
    #         if len(line) > 3 and line.split(" -> ")[0] not in grammar.keys():
    #             grammar[line.split(" -> ")[0]] = []
    #             tmp = line.split(" -> ")[1].split(" ")
    #             for words in tmp:
    #                 grammar[line.split(" -> ")[0]].append(words)






    # find which rule this belongs to
    exp = []
    for key in grammar:
        rules = grammar.get(key)
        for rule in rules:
            if word in rule:
                exp.append(key)
                break

    # #to check twice
    # l = word.split(" ")
    # new_word = ''
    # if exp == []:
    #     for i in l:
    #         for key in grammar:
    #             rules = grammar.get(key)
    #             for rule in rules:
    #                 if i == rule:
    #                     new_word += i + ' '
    #
    #     for key in grammar:
    #         rules = grammar.get(key)
    #         for rule in rules:
    #             if word in rule:
    #                 exp.append(key)
    #                 break
    #
    # l = new_word.split(" ")
    # word = ''
    # if exp == []:
    #     for i in l:
    #         for key in grammar:
    #             rules = grammar.get(key)
    #             for rule in rules:
    #                 if i == rule:
    #                     word += i + ' '
    #
    #     for key in grammar:
    #         rules = grammar.get(key)
    #         for rule in rules:
    #             if new_word in rule:
    #                 exp.append(key)
    #                 break


    return exp


# concatenates two phrases. l1 dan l2 adalah list dari string
def join(l1, l2):
    # if one of the phrases are an impossible string, skip
    s = ''
    if l1 == []:
        for i in l2:
            s += i + " "
        return [s]
    elif l2 == []:
        for i in l1:
            s += i + " "
        return [s]

    #print(l1)
    l1 = l1[0].split(' ')
    l2 = l2[0].split(' ')
    tmp = []
    for i in l1:
        for j in l2:
            #if i != j:
            if i == j:
                tmp.append(i)
            else:
                tmp.append(i + " " + j)
    return tmp

#['VP PP'] ['NP']
#['VP NP', 'PP NP']

def cyk(string):
    # separate strings word by word
    sentence = string.split(" ")

    m = len(sentence)
    table = [[[] for i in range(m)] for j in range(m)]

    #loop for row 1
    for i in range(len(sentence)):
        table[0][i] = find_rule(sentence[i])
    #print("start", table)

    #loop for row > 1
    #to find the valye of V-ij, use formula V-ij = V-ik V-(i+k)(j-k)
    #where k varies from 1 to j-1

    #k is the number of iteration before this
    for j in range(1, m):
        k = range(1,j+1)
        #print("j", j)
        for i in range(m-j):
            exp = []
            for seq in k:
                exp.append(join(table[seq-1][i],table[j-seq][i+seq]))

            print("To join: ", exp)
            for item in range(len(exp)-1):
                exp[item+1] = join(exp[item], exp[item+1])
                print("Joined: ", join(exp[item], exp[item+1]))
                exp[item] = 'x'

            #print(exp[-1][0])
            table[j][i] = find_rule(exp[-1][0])
            #print(table)

    #now table is completed
    structure = table[m-1][0]
    print(structure)
    final = ''
    for i in structure:
        final += find_rule(i)[0]

    if find_rule(final) == []:
        print(f"kalimat tidak baku")
    else:
        print(f"kalimat ada dalam bahasa indonesia. Struktur: {final}")
    return final

kalimat = input("Masukkan kalimat yang ingin diparsing: ")
cyk(kalimat)
