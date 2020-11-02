# Prints a list of dictionaries in tabular format

def printListOfDictToTable(listOfDicts):

    headers = list(listOfDicts[0].keys())

    values = []
    for i in listOfDicts:
        values.append(list(i.values()))

    headersValues = values.copy()
    headersValues.insert(0, headers)

    colWidth = [0] * len(list(listOfDicts[0].keys()))

    for curList in headersValues:
        for item in curList:
            if len(item) > colWidth[curList.index(item)]:
                colWidth[curList.index(item)] = len(item)

    tableWidth = 0
    for column in colWidth:
        tableWidth += column
    tableWidth += 3 * len(colWidth)

    for header in headers:
        print(header.title().ljust(colWidth[headers.index(header)]), end=' '*3)

    print('\n' + '-'*tableWidth)

    for curList in values:
        for curValue in curList:
            print(curValue.ljust(colWidth[curList.index(curValue)]), end=' '*3)
        print()
