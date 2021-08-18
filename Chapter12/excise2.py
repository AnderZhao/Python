print "Enter 5 names: "
names = []
for i in range(5):
    names.append(raw_input())
sorted_names = sorted(names)
print "The sorted names are",
for name in sorted_names:
    print name,
print
print "The original names are",
for name in names:
    print name,
