number = int(raw_input("Which multiplication table would you like?"))
count = 1
print "Here's your table:"
while count <= 10:
    print number, "x", count, "=", number * count
    count = count + 1
