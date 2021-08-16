mul = int(raw_input("Which multiplication table would you like?"))
count = int(raw_input("How high do you want to go?"))
print "Here's your table:"
for i in range(count):
    print mul, "x", i + 1, "=", mul * (i + 1)
