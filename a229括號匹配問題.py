import sys

result = []
resultStr = ''
n = 0
paran = []


def dfs(open, close, now):
    global paran
    global resultStr

    if open > n or close > open:
        return
    if now == n*2:
        resultStr += (''.join(tuple(paran)) + '\n')
        return

    paran[now] = '('
    dfs(open+1, close, now+1)
    paran[now] = ')'
    dfs(open, close+1, now+1)

def setDfs():
    for i in range(1,12):
        global n
        n = i
        global resultStr
        resultStr = ''
        global paran
        paran = [None]*(n*2)
        dfs(0, 0, 0)
        result.append(resultStr)

setDfs()

for inputValue in sys.stdin:
    print(result[int(inputValue)-1])
    # n = int(inputValue)
    # resultStr = ''
    # paran = [None]*(n*2)
    # dfs(0, 0, 0)
    # print(len(resultStr))
