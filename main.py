import random;
import math

# 100 is the best gscu value for testing and etc.
import main

gscu =100
gsc = gscu*gscu
smoothingAmount = 1;#the smaller the number the more smoothing
LakeChance = 1;
cyanchunklist = list();
darkbluechunklist = list();
greenchunklist = list();
yellowchunklist = list()
brownchunklist = list()
bluechunklist = list()
villagechunklist = list()
citychunklist = list()
roadchunklist = list()
donecalculating = False
def Count(i, listToSearch):

    ncount = 0;

    if (i%(gscu)) != 9 and i+1 in listToSearch:
        ncount+=1;
    if (i%(gscu)) != 0 and i-1 in listToSearch:
        ncount+=1;
    if i>=(gscu) and i - (gscu) in listToSearch:
        ncount += 1;
    if  i + (gscu) in listToSearch:
        ncount += 1;

    if (i % (gscu)) != ((gscu)-1) and i >= (gscu) and i - ((gscu)-1) in listToSearch:
        ncount += 1;
    if (i % (gscu)) != 0 and i >= (gscu) and i - ((gscu)+1) in listToSearch:
        ncount += 1;
    if i <= ((gscu)*((gscu)-1)) and (i % (gscu)) != ((gscu)-1) and i + ((gscu)+1) in listToSearch:
        ncount += 1;
    if i <= ((gscu)*((gscu)-1)) and (i % (gscu)) != 0 and i + ((gscu)-1) in listToSearch:
        ncount += 1;

    
    return ncount;




def Calculate():
    # loadperchunk = gsc / 100
    # loadper = 0;
    # loadpertd = 1;
    # loadperfs = 0;

    colorlist = list();
    i = 0;
    while i < gsc:
        rv = random.randint(1, 7)
        if rv <= 2:

            cyanchunklist.append(i)
            i+=1;
        else:

            darkbluechunklist.append(i)
            i += 1


        # if loadper == loadperchunk * loadpertd:
        #     loadpertd += 1
        #     loadperfs += 1
        #     print(loadperfs)
    r = 0
    while len(greenchunklist) < ((gsc / 10) * 3):
        rv = random.randint(1, 5)
        r+=1
        t = random.randint(1, gsc)
        if t in cyanchunklist:
            if Count(t, cyanchunklist) >= 6:

                cyanchunklist.remove(t);

                greenchunklist.append(t)
                if rv == 1:
                    if (t % (gscu)) != 9 and t + 1 in cyanchunklist:
                        cyanchunklist.remove(t + 1);
                    greenchunklist.append(t + 1)
                elif rv == 2:
                    if (t % (gscu)) != 0 and t - 1 in cyanchunklist:
                        cyanchunklist.remove(t - 1);
                    greenchunklist.append(t - 1)
                elif rv == 3:
                    if t <= (9 * gscu) and t + (gscu) in cyanchunklist:
                        cyanchunklist.remove(t + gscu);
                    greenchunklist.append(t + gscu)
                else:
                    if t >= (gscu) and t - (gscu) in cyanchunklist:
                        cyanchunklist.remove(t - gscu);
                    greenchunklist.append(t - gscu)

            elif Count(t, greenchunklist) >= 1:
                
               
                
                


                cyanchunklist.remove(t);

                greenchunklist.append(t)
                if rv == 1:
                    if (t % (gscu)) != 9 and t + 1 in cyanchunklist:
                        cyanchunklist.remove(t + 1);
                    greenchunklist.append(t+1)
                elif rv == 2:
                    if (t % (gscu)) != 0 and t - 1 in cyanchunklist:
                        cyanchunklist.remove(t - 1);
                    greenchunklist.append(t - 1)
                elif rv == 3:
                    if t<=(9*gscu)  and t + (gscu) in cyanchunklist:
                        cyanchunklist.remove(t + gscu);
                    greenchunklist.append(t + gscu)
                else:
                    if t >= (gscu) and t - (gscu) in cyanchunklist:
                        cyanchunklist.remove(t - gscu);
                    greenchunklist.append(t - gscu)
                
        elif t in darkbluechunklist:
            if Count(t, cyanchunklist) >= 6:

                darkbluechunklist.remove(t);

                greenchunklist.append(t)
                if rv == 1:
                    if (t % (gscu)) != 9 and t + 1 in darkbluechunklist:
                        darkbluechunklist.remove(t + 1);
                    greenchunklist.append(t + 1)
                elif rv == 2:
                    if (t % (gscu)) != 0 and t - 1 in darkbluechunklist:
                        darkbluechunklist.remove(t - 1);
                    greenchunklist.append(t - 1)
                elif rv == 3:
                    if t <= (9 * gscu) and t + (gscu) in darkbluechunklist:
                        darkbluechunklist.remove(t + gscu);
                    greenchunklist.append(t + gscu)
                else:
                    if t >= (gscu) and t - (gscu) in darkbluechunklist:
                        darkbluechunklist.remove(t - gscu);
                    greenchunklist.append(t - gscu)

            elif Count(t, greenchunklist) >= 1:


                darkbluechunklist.remove(t);

                greenchunklist.append(t)
                if rv == 1:
                    if (t % (gscu)) != 9 and t + 1 in darkbluechunklist:
                        darkbluechunklist.remove(t + 1);
                    greenchunklist.append(t + 1)
                elif rv == 2:
                    if (t % (gscu)) != 0 and t - 1 in darkbluechunklist:
                        darkbluechunklist.remove(t - 1);
                    greenchunklist.append(t - 1)
                elif rv == 3:
                    if t <= (9 * gscu) and t + (gscu) in darkbluechunklist:
                        darkbluechunklist.remove(t + gscu);
                    greenchunklist.append(t + gscu)
                else:
                    if t >= (gscu) and t - (gscu) in darkbluechunklist:
                        darkbluechunklist.remove(t - gscu);
                    greenchunklist.append(t - gscu)
    #smoothing
    o = 0
    smoothinglist = list()
    while o < gsc:
        if o in cyanchunklist:
            if Count(o, greenchunklist) >= smoothingAmount:
                cyanchunklist.remove(o);
                smoothinglist.append(o)

        elif o in darkbluechunklist:
            if Count(o, greenchunklist) >= smoothingAmount:
                darkbluechunklist.remove(o);
                smoothinglist.append(o)
        o+=1
    greenchunklist.extend(smoothinglist)
    #lonely sea tiles removal
    s = 0
    while s < len(cyanchunklist):
        if Count(cyanchunklist[s], darkbluechunklist) >= 4 and Count(cyanchunklist[s], cyanchunklist) <= 2 and Count(cyanchunklist[s], greenchunklist) < 1:
            darkbluechunklist.append(cyanchunklist[s])

        s += 1
    s = 0
    cyanchunkcount = len(cyanchunklist)
    for _ in (1, cyanchunkcount + 1):
        if cyanchunklist[s] in darkbluechunklist:
            cyanchunklist.pop(s)
        else:
            s += 1
    #fresh water calculator
    s = 0
    while s < len(cyanchunklist):
        if Count(cyanchunklist[s], greenchunklist) >= 5 and Count(cyanchunklist[s], darkbluechunklist) < 1:
            bluechunklist.append(cyanchunklist[s])

        s += 1
    s = 0
    cyanchunkcount = len(cyanchunklist)
    for _ in (1, cyanchunkcount + 1):
        if cyanchunklist[s] in bluechunklist:
            cyanchunklist.pop(s)
        else:
            s += 1
    #fresh water expanding
    s = 0
    while s < len(greenchunklist):
        r = random.randint(1,2)
        if Count(greenchunklist[s], bluechunklist) >= 1 and r == 2 and Count(greenchunklist[s], darkbluechunklist) < 1 and Count(greenchunklist[s], cyanchunklist) < 1:
            bluechunklist.append(greenchunklist[s])

        s += 1
    s = 0
    greenchunkcount = len(greenchunklist)
    for _ in (1, greenchunkcount + 1):
        if greenchunklist[s] in bluechunklist:
            greenchunklist.pop(s)
        else:
            s += 1
    # fresh water expanding2
    # s = 0
    # while s < len(cyanchunklist):
    #     r = random.randint(1, 2)
    #     if Count(cyanchunklist[s], bluechunklist) >= 1:
    #         bluechunklist.append(cyanchunklist[s])
    #
    #     s += 1
    # s = 0
    # cyanchunkcount = len(cyanchunklist)
    # for _ in (1, cyanchunkcount + 1):
    #     if cyanchunklist[s] in bluechunklist:
    #         cyanchunklist.pop(s)
    #     else:
    #         s += 1
    # fresh water expanding3
    # s = 0
    # while s < len(darkbluechunklist):
    #     r = random.randint(1, 2)
    #     if Count(darkbluechunklist[s], bluechunklist) >= 1:
    #         bluechunklist.append(darkbluechunklist[s])
    #
    #     s += 1
    # s = 0
    # cyanchunkcount = len(cyanchunklist)
    # for _ in (1, cyanchunkcount + 1):
    #     if darkbluechunklist[s] in bluechunklist:
    #         darkbluechunklist.pop(s)
    #     else:
    #         s += 1
    #fertile land calculator
    s=0
    while s < len(greenchunklist):
        r = random.randint(1,2)
        if Count(greenchunklist[s], bluechunklist) >= 1 and r == 2:
            brownchunklist.append(greenchunklist[s])

        s += 1
    s = 0
    greenchunkcount = len(greenchunklist)
    for _ in (1, greenchunkcount + 1):
        if greenchunklist[s] in brownchunklist:
            greenchunklist.pop(s)
        else:
            s += 1
    #village generation
    s = 0
    while s < len(greenchunklist):
        r = random.randint(1, 6)
        if Count(greenchunklist[s], brownchunklist) >= 3 and r >= 2:
            villagechunklist.append(greenchunklist[s])

        s += 1
    s = 0
    greenchunkcount = len(greenchunklist)
    for _ in (1, greenchunkcount + 1):
        if greenchunklist[s] in villagechunklist:
            greenchunklist.pop(s)
        else:
            s += 1
    #city generation + tutorial if i forgor
    s = 0
    while s < len(greenchunklist):#greenchunklist is the slots it can use Ex: Cities can be only on green land
        r = random.randint(1, 10)#Random
        if Count(greenchunklist[s], villagechunklist) >= 2 and r >= 2 and Count(greenchunklist[s], cyanchunklist) < 1:#requirements for the city Ex.Near 2 Villages & Near 0 Sea
            citychunklist.append(greenchunklist[s])

        s += 1
    s = 0
    greenchunkcount = len(greenchunklist)#removal of the replaced green chunks
    for _ in (1, greenchunkcount + 1):
        if greenchunklist[s] in citychunklist:
            greenchunklist.pop(s)
        else:
            s += 1
    s = 0
    #Road gen
    while s < len(greenchunklist):
        r = random.randint(1, 8)
        if (Count(greenchunklist[s], citychunklist) >= 1 and r == 5 and Count(greenchunklist[s], roadchunklist) < 1) or Count(greenchunklist[s], roadchunklist) == 1:

            roadchunklist.append(greenchunklist[s])

        s += 1
    s = 0
    greenchunkcount = len(greenchunklist)  # removal of the replaced green chunks
    for _ in (1, greenchunkcount + 1):
        if greenchunklist[s] in citychunklist:
            greenchunklist.pop(s)
        else:
            s += 1
    #sand generation
    l = 0
    while l < len(greenchunklist):
        r = random.randint(1, 7)
        if Count(greenchunklist[l], cyanchunklist) >= 1 or Count(greenchunklist[l], darkbluechunklist) >= 1:
            if Count(greenchunklist[l], bluechunklist) < 1:
                if r < 7:
                    yellowchunklist.append(greenchunklist[l])


        l+=1
    l = 0
    greenchunkcount = len(greenchunklist)
    for _ in (1, greenchunkcount + 1):
        if greenchunklist[l] in yellowchunklist:
            greenchunklist.pop(l)
        else:
            l+=1



    main.donecalculating = True
Calculate()
