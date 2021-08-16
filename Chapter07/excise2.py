age = int(raw_input("How old are you?"))
if 10 <= age <= 20:
    print "Your age is right, please next."
    sex = raw_input("What's your sex?")
    if sex == 'f':
        print "Your can enter team."
    else:
        print "Your can't enter team."
else:
    print "Your can't enter team."
