import sys

for row_column in sys.stdin:
    row, column = row_column.split()

    row = int(row)
    column = int(column)

    element = []
    resultArray = []

    for i in range(0, int(row)):
        row = sys.stdin.readline()
        element.append(row.split())

    for j in range(0, int(column)):
        for row in element:
            if len(resultArray) > j:
                resultArray[j].append(row[j])
            else:
                resultArray.append([row[j]])

    for k in resultArray:
        resultText = ''
        for v in k:
            resultText += v + ' '
        print(resultText)


# import sys

# for row_column in sys.stdin:
#     row, column = row_column.split()

#     row = int(row)
#     column = int(column)

#     element = []
#     resultArray = []

#     for i in range(0, int(row)):
#         row = sys.stdin.readline()
#         element.append(row.split())

#     resultArray = [j for j in list(map(list, zip(*element)))]
#     for k in resultArray:
#         resultText = ''
#         for v in k:
#             resultText += v + ' '
#         print(resultText)
