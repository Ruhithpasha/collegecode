import sys
sum = 0
for arg in range (1, len(sys.argv)):
    sum = sum+ int(sys.argv[arg])

print(f"The sum  is: {sum}")