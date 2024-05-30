import time

#Calculating the time of the code using for loop
start_time = time.time()

for i in range(101):
    print(i)

print(time.time() - start_time)


#Calculating the time of the same code using while loop
start_time = time.time()

i = 1
while i<101:
    print(i)
    i+=1

print(time.time() - start_time)