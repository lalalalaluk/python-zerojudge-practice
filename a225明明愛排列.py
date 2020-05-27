import sys

for i in sys.stdin:
    totalNumber = i
    dictTotal = {}
    numbers = sys.stdin.readline().strip().split(' ')

    for j in numbers:
        if dictTotal.get(list(j)[-1]):
            dictTotal.get(list(j)[-1]).append(int(j))
            dictTotal.update(
                {list(j)[-1]: dictTotal.get(list(j)[-1])})
        else:
            dictTotal.update({list(j)[-1]: [int(j)]})

    for k in dictTotal.keys():
        dictTotal[k] = sorted(dictTotal.get(k), reverse=True)

    sortKeys = sorted(dictTotal.keys())
    result = []
    for m in sortKeys:
        result += [str(i) for i in dictTotal[m]]

    print(' '.join(result))
