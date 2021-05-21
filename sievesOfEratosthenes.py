# "Make a list of all the integers less than or equal to n (greater than one) and strike out the multiples of all primes
# less than or equal to the square root of n, then the numbers that are left are the primes. (Finding primes & proving
# primality, UTM)"


from sys import argv

def sievesOfEratosthenes(bound):
    # We will find primes up to, and not including, the following upper bound

    # Make a list of booleans as large as 'bound'
    boolList = [True] * (bound)

    # 0,1 are not prime
    boolList[1] = False
    boolList[0] = False

    # Starting at 2,set the prime flag to false for the multiples of all primes less than or equal to the square root of n
    for i in range(2,int(bound**(1/2))):
        if boolList[i] == True:
            j = 0
            while i**2 +i*j < bound:
                boolList[i**2 +i*j] = False
                j+=1

    # Make a list to hold all of the prime numbers
    primes = []

    for i in range(0, len(boolList)):
        if boolList[i] == True:
            primes.append(i)

    return primes

if __name__=="__main__":
    script, bound = argv
    primeList = sievesOfEratosthenes(int(bound))
    print(primeList)
    print("%d" % len(primeList))

