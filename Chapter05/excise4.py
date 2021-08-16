length = float(raw_input("Enter length of room"))
width = float(raw_input("Enter width of room"))
cost = float(raw_input("Enter cost per square yard of carpet"))
print "We need", length * width, "square yard"
print "We need", length * width * 9, "square feet"
print "We need", length * width * 9 * cost, "cost"
