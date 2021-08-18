print "Enter 5 names: "
names = []
for i in range(5):
    names.append(raw_input())
print "The names are",
for name in names:
    print name,
print
index = int(raw_input("Replace one name.  Which one? (1-5): "))
name = raw_input("New name: ")
names.insert(index - 1, name)
print "The names are",
for name in names:
    print name,
print