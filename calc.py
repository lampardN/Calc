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


def progress(stroka):
    try:
        a = []
        number = ''
        for symbol in stroka:
            if '0' <= symbol <= '9' or symbol == '.':
                number += symbol
            else:
                if number != '':
                    if '.' in number:
                        a.append(float(number))
                    else:
                        a.append(int(number))
                    number = ''
            if not('0' <= symbol <= '9') and symbol != '.':
                a.append(symbol)
        try:
            if '.' in number:
                a.append(float(number))
            else:
                a.append(int(number))
        except:
            pass

        if a[0] == '-' and type(a[1]) == type(1):
            a[1] = -a[1]
            del a[0]

        for i in range(1, len(a)):
            if a[i] == '-':
                if type(a[i-1]) != type(1) and type(a[i+1]) == type(1):
                    a[i+1] = -a[i+1]
                    a[i] = '@'
        while a.count('@') != 0:
            del a[a.index('@')]


        pfx = []
        stack = []

        for element in a:
            if isinstance(element, int) or isinstance(element, float):
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
            if len(pfx) == 2:
                if pfx[1] == '+':
                    del pfx[1]
                    continue
                elif pfx[1] == '-':
                    pfx[0] = -pfx[0]
                    del pfx[1]
                    continue
        print(pfx[0])
        return str(pfx[0])
    except:
        return 'Error'

progress('-(3/2)*(2/3)')