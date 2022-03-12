import sys

stdin = sys.stdin

n = int(stdin.readline())
for i in range(2*n-1):
    d = n-1-abs(n-1-i)
    for j in range(4*n-3):
        if j % 2 == 0 and abs((j-(2*n-2))//2) <= d:
            sys.stdout.write(chr(97+n-1-(d-abs((j-(2*n-2))//2))))
        else:
            sys.stdout.write("-")
    sys.stdout.write("\n")