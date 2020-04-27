import sys

for inputValue in sys.stdin:
    result = inputValue[::-1].strip()
    print(int(result))

            