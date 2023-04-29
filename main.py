a = 0
b = 0
c = 0

list = []
listVerif = []

for i in range(0, 8):
    a = i
    for i in range(0, 9):
        b = i
        for i in range(0, 10):
            c = i
            if b != a :
                if c!= a :
                    if c!= b :
                        list.append(a)
                        list.append(b)
                        list.append(c)
                        list.sort()
                        trio = ""
                        for i in list :
                            trio = trio+str(i)
                        if trio in listVerif :
                            list.clear()
                            continue
                        else :

                            list.clear()
                            print(a,end='')
                            print(b,end='')
                            print(c,end=' ')
                            list.append(a)
                            list.append(b)
                            list.append(c)
                            list.sort()
                            trio =""
                            for i in list :
                                trio = trio+str(i)
                            listVerif.append(trio)
                            list.clear()