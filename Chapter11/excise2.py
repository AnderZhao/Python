import time
count = int(raw_input("Countdown timer:  How many seconds? "))
for i in range(count, 0, -1):
    print i,
    for j in range(i):
        print "*",
    print
    time.sleep(1)
print "BLAST OFF!"
