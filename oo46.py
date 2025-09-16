# Write a program that displays a countdown for fireworks from 10 to 0, with a 1-second pause between each number.

from time import sleep
for c in range(11, -1, -1): # isso o ultimo não é contado e eu quero ate o 0
    print(c)
    sleep(1)
print('CONSEGUIUU!!!')