def zfig(z):
    print(".     " + str(z[0]) + " ------------------  " + str(z[1]) + " ------------------ " + str(z[2]))
    print('.     |                     |                    |')
    print(".     .       " + str(z[3]) + " ----------- " + str(z[4]) + " -----------" + str(z[5]) + "      .")
    print(".     |       |             |             |      |")
    print(".     .       .      " + str(z[6]) + " ----" + str(z[7]) + " -----" + str(z[8]) + "     .      .")
    print(".     |       |      |            |       |      |")
    print(
        ".    " + str(z[9]) + "-----" + str(z[10]) + " ----" + str(z[11]) + "           " + str(z[12]) + " -----" + str(
            z[13]) + " ----" + str(
            z[14]) + "")
    print(".     |       |      |           |       |      |")
    print(".     .       .    " + str(z[15]) + " --- " + str(z[16]) + " --- " + str(z[17]) + "      .      .")
    print(".     |       |            |             |      |")
    print(".     .     " + str(z[18]) + " ---------- " + str(z[19]) + " --------- " + str(z[20]) + "       .")
    print(".     |                    |                    |")
    print(".    " + str(z[21]) + " ----------------- " + str(z[22]) + " -----------------" + str(z[23]) + " ")


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

print()
print("welcome to the game of nine men's checker")
print()
a = []
b = []
moves = [[10, 2], [1, 5, 3], [2, 15], [11, 5], [2, 4, 8, 6], [5, 14], [12, 8], [7, 5, 9], [8, 13], [1, 22, 11],
         [4, 10, 19, 12],
         [7, 11, 16],
         [9, 14, 18], [6, 13, 15, 21], [3, 14, 24], [12, 17], [16, 18, 20], [13, 17], [11, 20], [17, 19, 21, 23],
         [14, 20],
         [10, 23], [20, 22, 24], [15, 23], []
         ]

jumps = [[1, 2, 3], [4, 5, 6], [7, 8, 9]
    , [16, 17, 18], [19, 20, 21], [22, 23, 24]
    , [1, 10, 22], [4, 11, 19], [7, 12, 16],
        [9, 13, 18], [6, 14, 21], [3, 15, 24],
        [2, 5, 8], [10, 11, 12], [17, 20, 23], [13, 14, 15]
        ]

zfig(z)

for i in range(9):
    print("*pawn" + str(i + 1) + "*")
    x = int(input("user1 :  "))
    while x not in n or x in a or x in b:
        print("enter correct input")
        x = int(input("user1 :  "))
    a.append(x)
    z[x - 1] = str(n[x - 1]) + "a"
    zfig(z)


    y = int(input("user2 :  "))
    while y not in n or y in a or y in b:
        print("enter correct input")
        y = int(input("user2 :  "))
    b.append(y)
    z[y - 1] = str(n[y - 1]) + "b"
    zfig(z)


    print("user1:" + str(a) + "   user2 :" + str(b))
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")


def move(x,y,opp,jumps):
    flag=True
    for i in jumps:
        if x in i and y in i and ((x==i[0] and i[1] in opp) or (x==i[1] and (y==i[0] or y==i[-1] and y not in opp)) or (x==i[-1] and i[1] in opp) or ((x==i[0] or x==i[-1]) and (y==i[1] and y not in opp ))):
            flag=False
    return flag

while (len(a) != 0 or len(b) != 0):
    x, y = list(map(int, input("Enter the positions to move the pawn\nuser 1: ").split()))
    while move(x,y,b,jumps) or x not in a or y in a or y in b:
        x, y = list(map(int, input("enter correct pawn address to move :").split()))
    for _ in jumps:
        if x in _ and y in _ and _[1] in b:
            z[_[1]-1]=str(z[_[1]-1])[:-1]
            b.remove(_[1])

    a.remove(x)
    z[x - 1] = str(z[x - 1])[:-1]
    a.append(y)
    z[y - 1] = str(z[y - 1]) +"a"
    print("a:",a,"\n","b:",b)
    zfig(z)

    x, y = list(map(int, input("Enter the positions to move the pawn\nuser 2: ").split()))
    while move(x,y,a,jumps) or x not in b or y in a or y in b:
        x, y = list(map(int, input("enter correct pawn address to move :").split()))
    #flag=True
    for _ in jumps:
        if x in _ and y in _ and _[1] in a:
            #flag=False
            z[_[1] - 1] = str(z[_[1] - 1])[:-1]
            a.remove(_[1])

    b.remove(x)
    z[x - 1] = str(z[x - 1])[:-1]
    b.append(y)
    z[y - 1] = str(z[y - 1]) + "b"

    print(a, "\n", b)
    zfig(z)
