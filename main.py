import random;
import math
# 100 is the best gscu value for testing and etc.
gscu =100
gsc = gscu*gscu
def Count(i):
    ncount = 0;

    if (i%(gscu)) != 9 and i+1 in redchunklist:
        ncount+=1;
    if (i%(gscu)) != 0 and i-1 in redchunklist:
        ncount+=1;
    if i>=(gscu) and i - (gscu) in redchunklist:
        ncount += 1;
    if i<=90  and i + 10 in redchunklist:
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
    if i <= 90 and i + 10 in greenchunklist:
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




answer = input("Start TG? y/n?")
while answer != ("stop"):
    if answer == ("y"):

        redchunklist = list();
        blackchunklist = list();
        greenchunklist = list();
        colorlist = list();
        i = 0;
        while i < gsc:
            rv = random.randint(1, 7)
            if rv <= 2:

                redchunklist.append(i)
                i+=1;

            elif CountSob(i) >= 3 and len(greenchunklist) < (gsc//5) and CountSob(i) < 5:
                greenchunklist.append(i)

                i+=1;
            elif CountSob(i) >= 2:
                greenchunklist.append(i)
                i+=1;
            elif rv >= 5:

                blackchunklist.append(i)
                i+=1
            elif Count(i) >= 3:
                greenchunklist.append(i)
                i+=1;
            elif random.randint(1, 2) == 2:
                redchunklist.append(i)
                i+=1
            else:
                blackchunklist.append(i)
                i+=1

        break;
    if answer == ("n"):
        break;
