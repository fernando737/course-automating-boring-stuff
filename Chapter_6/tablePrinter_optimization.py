tableData = [['apples', 'oranges', 'cherriessss', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'gooseS']]

def printTable(table):
    colWidths = [max(len(item) for item in col) for col in table]
    
    for row in zip(*table):
        for col, width in zip(row, colWidths):
            print(col.rjust(width), end=' ')
        print()

printTable(tableData)
