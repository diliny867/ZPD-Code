import math, os
import time
from prime import *
from memory_profiler import profile
def asciiToString(string, length):
    num = 0
    res = ""
    for i in range(length):
        num = num * 10 + (ord(string[i]) - ord('0'))
        if (num >= 32 and num <= 122):
            res += chr(num)
            num = 0
    return res


# Generate the public and the private keys based on the 2 primes input by the user
def generateKeys(p,q):
    # Take 2 primes from the user, which we'll use to generate the keys
    n = p * q
    N = (p - 1) * (q - 1)

    # Generate an exponent e, so that 1 < e < N, gcd(e, N) = 1
    while (True):
        e = random.randrange(2, N)
        if (math.gcd(e, N) == 1):
            break

    # Public key = [n, e] ; Private key = [n, d]
    d = pow(e, -1, N)

    return [n, e, d]

@profile
def encrypt(msg, n, e):
    # Get the message for encryption from the user, encrypt it
    ordMsg = ""
    for i in msg:
        ordMsg += str(ord(i))
    # Encrypt the message using the public key
    c = pow(int(ordMsg), e, n)
    return c

@profile
def decrypt(c, n, d):
    # Decrypt the input data using the private key
    z = str(pow(c, int(d), n))
    return (asciiToString(z, len(z)))


# Driver code
def main(n, e, d, msg, w_iterations):

    encTotal = 0
    decTotal = 0

    for i in range(w_iterations):

        # Encryption process, calculate the time
        encStart = time.perf_counter()
        c = encrypt(msg, n, e)
        encEnd = time.perf_counter()
        # Decryption process
        decStart = time.perf_counter()
        z = decrypt(c, n, d)
        decEnd = time.perf_counter()

        encTotal += (encEnd - encStart) * 1000
        decTotal += (decEnd - decStart) * 1000

    print(f"{'encrypt':^16s}/ {w_iterations:^12d}/ {len(msg):^12d}/ {encTotal:^14.5f}/ {encTotal / w_iterations:^14.5f}")
    print(f"{'decrypt':^16s}/ {w_iterations:^12d}/ {len(msg):^12d}/ {decTotal:^14.5f}/ {decTotal / w_iterations:^14.5f}")
    print()


    #with open("avgTime.txt", "a") as f:
    #    f.write("Encryption " + str(avgEncTime) + " | Decryption " + str(avgDecTime) + "\n")



if __name__ == "__main__":
    p = generatePrime()
    q = generatePrime()
    n, e, d = generateKeys(p,q)

    print(f"{'operation':^16s}/ {'count':^12s}/ {'data size':^12s}/ {'total time ms':^14s}/ {'avg time ms':^14s}")
    iterations = 1

    main(n, e, d, str(os.urandom(5)), iterations)
    main(n, e, d, str(os.urandom(10)), iterations)
    main(n, e, d, str(os.urandom(25)), iterations)
    main(n, e, d, str(os.urandom(100)), iterations)
    main(n, e, d, str(os.urandom(200)), iterations)
    main(n, e, d, str(os.urandom(500)), iterations)
    main(n, e, d, str(os.urandom(1000)), iterations)
    main(n, e, d, str(os.urandom(10000)), iterations)
    main(n, e, d, str(os.urandom(100000)), iterations)
