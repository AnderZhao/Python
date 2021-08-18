print "Enter 5 names: "
names = []
for i in range(5):
    names.append(raw_input())
print "The names are",
for name in names:
    print name,
