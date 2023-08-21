import random;
import math

# 100 is the best gscu value for testing and etc.
import main

gscu =100
gsc = gscu*gscu
redchunklist = list();
blackchunklist = list();
greenchunklist = list();
yellowchunklist = list()
donecalculating = False
def Count(i):

    ncount = 0;

    if (i%(gscu)) != 9 and i+1 in redchunklist:
        ncount+=1;
    if (i%(gscu)) != 0 and i-1 in redchunklist:
        ncount+=1;
    if i>=(gscu) and i - (gscu) in redchunklist:
        ncount += 1;
    if i<=(9*gscu)  and i + (gscu) in redchunklist:
        ncount += 1;

    if (i % (gscu)) != ((gscu)-1) and i >= (gscu) and i - ((gscu)-1) in redchunklist:
        ncount += 1;
    if (i % (gscu)) != 0 and i >= (gscu) and i - ((gscu)+1) in redchunklist:
        ncount += 1;
    if i <= ((gscu)*((gscu)-1)) and (i % (gscu)) != ((gscu)-1) and i + ((gscu)+1) in redchunklist:
        ncount += 1;
    if i <= ((gscu)*((gscu)-1)) and (i % (gscu)) != 0 and i + ((gscu)-1) in redchunklist:
        ncount += 1;

    
    return ncount;


def CountSob(i):
    ncount = 0;

    if (i % (gscu)) != 9 and i + 1 in greenchunklist:
        ncount += 1;
    if (i % (gscu)) != 0 and i - 1 in greenchunklist:
        ncount += 1;
    if i >= (gscu) and i - (gscu) in greenchunklist:
        ncount += 1;
    if i<=(9*gscu)  and i + (gscu) in greenchunklist:
        ncount += 1;

    if (i % (gscu)) != ((gscu) - 1) and i >= (gscu) and i - ((gscu) - 1) in greenchunklist:
        ncount += 1;
    if (i % (gscu)) != 0 and i >= (gscu) and i - ((gscu) + 1) in greenchunklist:
        ncount += 1;
    if i <= ((gscu) * ((gscu) - 1)) and (i % (gscu)) != ((gscu) - 1) and i + ((gscu) + 1) in greenchunklist:
        ncount += 1;
    if i <= ((gscu) * ((gscu) - 1)) and (i % (gscu)) != 0 and i + ((gscu) - 1) in greenchunklist:
        ncount += 1;

    return ncount;

def CountDeep(i):
    ncount = 0;

    if (i % (gscu)) != 9 and i + 1 in blackchunklist:
        ncount += 1;
    if (i % (gscu)) != 0 and i - 1 in blackchunklist:
        ncount += 1;
    if i >= (gscu) and i - (gscu) in blackchunklist:
        ncount += 1;
    if i<=(9*gscu)  and i + (gscu) in blackchunklist:
        ncount += 1;

    if (i % (gscu)) != ((gscu) - 1) and i >= (gscu) and i - ((gscu) - 1) in blackchunklist:
        ncount += 1;
    if (i % (gscu)) != 0 and i >= (gscu) and i - ((gscu) + 1) in blackchunklist:
        ncount += 1;
    if i <= ((gscu) * ((gscu) - 1)) and (i % (gscu)) != ((gscu) - 1) and i + ((gscu) + 1) in blackchunklist:
        ncount += 1;
    if i <= ((gscu) * ((gscu) - 1)) and (i % (gscu)) != 0 and i + ((gscu) - 1) in blackchunklist:
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

            redchunklist.append(i)
            i+=1;
        else:

            blackchunklist.append(i)
            i += 1


        # if loadper == loadperchunk * loadpertd:
        #     loadpertd += 1
        #     loadperfs += 1
        #     print(loadperfs)
    r = 0
    while len(greenchunklist) < ((gsc / 10) * 3):
        rv = random.randint(1, 4)
        r+=1
        t = random.randint(1, gsc)
        if t in redchunklist:
            if Count(t) >= 6:

                redchunklist.remove(t);

                greenchunklist.append(t)
                if rv == 1:
                    if (t % (gscu)) != 9 and t + 1 in redchunklist:
                        redchunklist.remove(t + 1);
                    greenchunklist.append(t + 1)
                elif rv == 2:
                    if (t % (gscu)) != 0 and t - 1 in redchunklist:
                        redchunklist.remove(t - 1);
                    greenchunklist.append(t - 1)
                elif rv == 3:
                    if t <= (9 * gscu) and t + (gscu) in redchunklist:
                        redchunklist.remove(t + gscu);
                    greenchunklist.append(t + gscu)
                else:
                    if t >= (gscu) and t - (gscu) in redchunklist:
                        redchunklist.remove(t - gscu);
                    greenchunklist.append(t - gscu)

            elif CountSob(t) >= 1:
                
               
                
                


                redchunklist.remove(t);

                greenchunklist.append(t)
                if rv == 1:
                    if (t % (gscu)) != 9 and t + 1 in redchunklist:
                        redchunklist.remove(t+1);
                    greenchunklist.append(t+1)
                elif rv == 2:
                    if (t % (gscu)) != 0 and t - 1 in redchunklist:
                        redchunklist.remove(t-1);
                    greenchunklist.append(t - 1)
                elif rv == 3:
                    if t<=(9*gscu)  and t + (gscu) in redchunklist:
                        redchunklist.remove(t+gscu);
                    greenchunklist.append(t + gscu)
                else:
                    if t >= (gscu) and t - (gscu) in redchunklist:
                        redchunklist.remove(t - gscu);
                    greenchunklist.append(t - gscu)
                
        elif t in blackchunklist:
            if Count(t) >= 6:

                blackchunklist.remove(t);

                greenchunklist.append(t)
                if rv == 1:
                    if (t % (gscu)) != 9 and t + 1 in blackchunklist:
                        blackchunklist.remove(t + 1);
                    greenchunklist.append(t + 1)
                elif rv == 2:
                    if (t % (gscu)) != 0 and t - 1 in blackchunklist:
                        blackchunklist.remove(t - 1);
                    greenchunklist.append(t - 1)
                elif rv == 3:
                    if t <= (9 * gscu) and t + (gscu) in blackchunklist:
                        blackchunklist.remove(t + gscu);
                    greenchunklist.append(t + gscu)
                else:
                    if t >= (gscu) and t - (gscu) in blackchunklist:
                        blackchunklist.remove(t - gscu);
                    greenchunklist.append(t - gscu)

            elif CountSob(t) >= 1:


                blackchunklist.remove(t);

                greenchunklist.append(t)
                if rv == 1:
                    if (t % (gscu)) != 9 and t + 1 in blackchunklist:
                        blackchunklist.remove(t + 1);
                    greenchunklist.append(t + 1)
                elif rv == 2:
                    if (t % (gscu)) != 0 and t - 1 in blackchunklist:
                        blackchunklist.remove(t - 1);
                    greenchunklist.append(t - 1)
                elif rv == 3:
                    if t <= (9 * gscu) and t + (gscu) in blackchunklist:
                        blackchunklist.remove(t + gscu);
                    greenchunklist.append(t + gscu)
                else:
                    if t >= (gscu) and t - (gscu) in blackchunklist:
                        blackchunklist.remove(t - gscu);
                    greenchunklist.append(t - gscu)
    o = 0
    smoothinglist = list()
    while o < gsc:
        if o in redchunklist:
            if CountSob(o) >= 4:
                redchunklist.remove(o);
                smoothinglist.append(o)

        elif o in blackchunklist:
            if CountSob(o) >= 4:
                blackchunklist.remove(o);
                smoothinglist.append(o)
        o+=1
    greenchunklist.extend(smoothinglist)
    l = 0

    while l < len(greenchunklist):
        if Count(greenchunklist[l]) >= 1 or CountDeep(greenchunklist[l]) >= 1:
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
