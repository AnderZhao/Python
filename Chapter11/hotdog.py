print "\t\tDog \tBun \tKetchup \tMustard \tOnions"
count = 1

for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    print "#", count, "\t",
                    print dog, "\t\t", bun, "\t\t", ketchup, "\t\t\t",
                    print mustard, "\t\t\t", onion
                    count = count + 1
