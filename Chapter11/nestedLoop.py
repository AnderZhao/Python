numberLines = int(raw_input('How many lines of stars do you want? '))
numberStars = int(raw_input('How many stars per line? '))
for line in range(numberLines):
    for star in range(numberStars):
        print "*",
    print
