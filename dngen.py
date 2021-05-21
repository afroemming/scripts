from random import choice
from string import ascii_lowercase
from sys import argv

for i in range(int(argv[1])):
    print(choice('qx')+ choice(ascii_lowercase)+choice(ascii_lowercase)+choice(ascii_lowercase))
