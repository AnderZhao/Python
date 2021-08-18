dic = {}
while True:
    opt = raw_input("Add or look up a word (a/l)?")
    if opt == 'a':
        key = raw_input("Type the word: ")
        if key in dic.keys():
            print "Keyword Error"
            continue
        definition = raw_input("Type the definition: ")
        dic[key] = definition
        print "Word added!"
    elif opt == 'l':
        key = raw_input("Type the word: ")
        if key in dic.keys():
            print dic[key]
        else:
            print "That word isn't in the dictionary yet."
    else:
        print "Enter correct option!"
