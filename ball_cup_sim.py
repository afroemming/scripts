from random import randrange
from sys import exit

vruns = []
nruns = 0
while True:
    try:
        nruns += 1
        run = ['E', 'E', 'E', 'E', 'E', 'E']
        bp1, bp2, rp = randrange(6), randrange(6), randrange(6)
        run[bp1], run[bp2], run[rp] = 'B', 'B', 'R'
        if bp1 == rp or bp2 == rp:
            run[rp] = 'E'
        run = ''.join(run)
        if not (bp1 == bp2 or run in vruns):
            vruns.append(run)

    except KeyboardInterrupt:
        print (f"Found {len(vruns)} arrangements in {nruns} runs")
        print(vruns)
        exit()