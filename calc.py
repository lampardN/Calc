def priority(symbol):

    if symbol == '+' \
            or symbol == '-':
        return 1

    if symbol == '*' \
            or symbol == '/':
        return 2

    if symbol == ')':
        return 3

    if symbol == '(':
        return 0

'''
def test(str):
    a = str
    t = []
    if a.count('(') > 0:
        for i in range(len(a)):
            if a[i] == '(' or a[i] == ')':
                t.append(a[i])
    e = -1
    for s in range(len(t)):
        if t[s] == '(' and t[e] == ')':
            t[s] = '@'
            t[e] = '@'
            e -= 1
        if t[s] == '(' and t[s+1] == ')':
            t[s] == '@'
            t[s+1] == '@'
    while t.count('@') != 0:
        del t[t.index('@')]
    if len(t) != 0:
       return input('Error')
    else:
        return 0
'''

def progress(stroka):
    try:
        a = []
        number = ''
        for symbol in stroka:
            if '0' <= symbol <= '9':
                number += symbol
            else:
                if number != '':
                    a.append(int(number))
                    number = ''
            if not('0' <= symbol <= '9'):
                a.append(symbol)
        try:
            a.append(int(number))
        except:
            pass

        pfx = []
        stack = []

        for element in a:
            if isinstance(element, int):
                pfx.append(element)

            if priority(element) == 0:
                stack.append(element)

            elif priority(element) == 1:
                if len(stack) != 0 :
                    if stack[-1] != ('*' or '/'):
                        stack.append(element)
                    else:
                        while len(stack) != 0:
                            if stack[-1] == '(':
                                break
                            pfx.append(stack.pop())
                        stack.append(element)
                else:
                    stack.append(element)

            elif priority(element) == 2:
                stack.append(element)

            elif priority(element) == 3:
                while stack[-1] != '(':
                    pfx.append(stack.pop())
                del stack[-1]
        while len(stack) != 0:
            pfx.append(stack.pop())

        i = 0

        while len(pfx) != 1:
            if pfx[i] == '+':
                pfx[i] = pfx[i - 1] + pfx[i - 2]
                del pfx[i - 1]
                del pfx[i - 2]
                i = 0
                continue
            if pfx[i] == '-':
                pfx[i] = pfx[i - 2] - pfx[i - 1]
                del pfx[i - 1]
                del pfx[i - 2]
                i = 0
                continue
            if pfx[i] == '/':
                pfx[i] = pfx[i - 2] / pfx[i - 1]
                del pfx[i - 1]
                del pfx[i - 2]
                i = 0
                continue
            if pfx[i] == '*':
                pfx[i] = pfx[i - 1] * pfx[i - 2]
                del pfx[i - 1]
                del pfx[i - 2]
                i = 0
                continue
            i += 1
        return str(pfx[0])
    except:
        return 'Error'