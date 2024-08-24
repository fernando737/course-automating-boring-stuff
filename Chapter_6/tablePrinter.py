tableData = [['apples', 'oranges', 'cherriessss', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'gooseS'],]


def printTable(table):
    numColumns = len(table)
    numRows = len(table[0])

    colWidths = []

    for row in table:
        max_width = 0
        for column in row:
            if max_width < len(column): max_width = len(column)
        colWidths.append(max_width)   
         
    for x in range(numRows):
        for y in range(numColumns):
            print(table[y][x].rjust(colWidths[y]), end=' ')
        print('')
    
printTable(tableData)

