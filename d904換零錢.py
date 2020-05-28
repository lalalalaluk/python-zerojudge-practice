import sys

for inputValue in sys.stdin:
    totalMoney,totalCoinType = inputValue.split()
    totalMoney = int(totalMoney)
    coinValue = []
    usedCoin = 0

    for i in range(0,int(totalCoinType)):
        row = sys.stdin.readline()
        coinValue.append(int(row.split()[0]))

    coinValue.sort(reverse=True)

    for cv in coinValue:
        if totalMoney > cv and totalMoney >0:
            n = totalMoney // cv
            usedCoin += n
            totalMoney = totalMoney -cv * n

    print(usedCoin)