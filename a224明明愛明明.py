import sys

for i in sys.stdin:
    iArray = list(i.strip())
    filteredi = [a.lower() for a in iArray if a !=
                 ',' and a != '_' and a != '.' and a != ':']
    result = 0
    for j in set(filteredi):
        if filteredi.count(j) % 2 == 1:
            result += 1
    if result < 2:
        print('yes !')
    else:
        print('no...')
