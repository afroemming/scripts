from sys import argv

def primeFactor(n):
    factor = 2
    factorList = []

    # Two is the only even prime, so we should treat it seperately and skip
    # even numbers in the next sections
    if n % factor == 0:
            # Divide n by factor once
            n = n / factor
            factorList.append(factor)
            # Divide n by 'factor' until it can't be done evenly anymore
            while n % factor == 0:
                factorList.append(factor)
                n = n /factor
    factor=factor + 1
   
    while n>1:
        # If 'factor' is a divisor of n...
        if n % factor == 0:
            # Divide n by factor once
            n = n / factor
            factorList.append(factor)
            # Divide n by 'factor' until it can't be done evenly anymore
            while n % factor == 0:
                factorList.append(factor)
                n = n /factor
        factor=factor + 2
    return factorList
    
if __name__ == "__main__":    
    script, n = argv
    print(primeFactor(int(n)))
