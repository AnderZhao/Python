import time
count = int(raw_input("Countdown timer:  How many seconds? "))
for i in range(count, 0, -1):
    print i
    time.sleep(1)
print "BLAST OFF!"
