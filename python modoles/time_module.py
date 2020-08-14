import time

initial = time.time()
# print(initial)

k = 0
while(k < 45):
    print("This is Anurag Mukherjee")
    k = k + 1

print("While loop ran in", time.time() - initial, "Seconds")

initial2 = time.time()

for i in range(45):
    print("This is Anurag Mukherjee")

print("For loop ran in", time.time() - initial2, "Seconds")    

# returns original time

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

time.sleep(2)       # Makes the program sleep for the give time in seconds.