import sys

result = []
paran = []
n = 0


def dfs(open, close, now):
    if open > n or close > open:
        return
    if now == n*2:
        result.append(paran)
        return

    paran[now] = '('
    dfs(open+1, close, now+1)
    paran[now] = ')'
    dfs(open, close+1, now+1)


for inputValue in sys.stdin:
    n = int(inputValue)
    paran = ['']*(n*2)
    dfs(0, 0, 0)

    print(result)
