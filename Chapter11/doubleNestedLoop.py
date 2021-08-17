numBlocks = int(raw_input ('How many blocks of stars do you want? '))
numLines = int(raw_input ('How many lines in each block? '))
numStars = int(raw_input ('How many stars per line? '))

for block in range(numBlocks):
    for line in range(numLines):
        for star in range(numStars):
            print "*",
        print
    print
