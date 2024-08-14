
spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'rats']

def function2(lst):
    result = ', '.join(lst[:-1]) + ', and ' + lst[-1]

def function1(list):
    result = ""
    list.insert(-1, 'and')
    for x, y in enumerate(list):
        if x<(len(list)-2):
            result += y + ", "
        else:
            result += y + " "
    print(result)

function1(spam)
function2(spam)