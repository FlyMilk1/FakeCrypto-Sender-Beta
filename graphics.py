import random

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QPainterPath, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
import math
from main import cyanchunklist
from main import darkbluechunklist
from main import greenchunklist
from main import yellowchunklist
from main import brownchunklist
from main import bluechunklist
from main import villagechunklist
from main import citychunklist
from main import Count
from main import gsc
from main import gscu
from main import donecalculating
import sys;
import time
#gkdpv needs to be a divisible on gsc value
gkdpv = 1000
namesyllables = ["ber", "ko", "vi", "ca", "mon", "ta", "na", "var", "shec", "bur", "gas", "na", "so", "fi", "ya", "psa", "ku", "di", "ya", "so", "lun"]
i = 0;
optimizedscrsize = True;
showneighborcount = False;
MakeCityNames = False
isreallydone = False
# def GrassChunk():
class MainApplication(QWidget):
    stoploadfs = False
    p = 0
    def __init__(self):
        super().__init__()
        if optimizedscrsize == True:
            self.setGeometry(gkdpv, gkdpv, gkdpv, gkdpv)
            self.show()
        else:
            self.setGeometry(1000, 1000, 1000, 1000)
        self.setWindowTitle("Generated Terrain")
    def paintEvent(self, event):
        loadperchunk = gsc / 100
        loadper = 0;
        loadpertd = 1;
        loadperfs = 0;
        
        i=0
        y=0
        kdp = gkdpv
        gss = int(gkdpv // gscu)
        pen = QPen()
        pen.setStyle(Qt.SolidLine)
        pen.setWidth(7)
        pen.setColor(Qt.white)
        draw = QPainter(self)
        draw.setPen(pen)

        for _ in range(1, len(cyanchunklist) + 1):
            cyanchunkcoord = cyanchunklist[i] * gss


            if cyanchunkcoord >= kdp:
                while cyanchunkcoord - kdp >= (gkdpv):
                    kdp += (gkdpv)

                y += (gss * kdp) // (gkdpv)
                cyanchunkcoord -= kdp



            draw.fillRect(cyanchunkcoord,y,gss,gss, QColor(0, 255, 187))
            #draw.drawText(cyanchunkcoord+50, y+50, 1200, 1200, 0, str(cyanchunklist[i]))
            #
            # loadper+=1;
            # if loadper == loadperchunk * loadpertd and MainApplication.stoploadfs == False:
            #     loadpertd+=1
            #     loadperfs+=1
            #     print(loadperfs)

            kdp=gkdpv
            i += 1
            y=0

        i = 0
        y = 0
        kdp = gkdpv
        gss = int(gkdpv // gscu)
        for _ in range(1, len(darkbluechunklist) + 1):

            darkbluechunkcoord = darkbluechunklist[i] * gss




            if darkbluechunkcoord >= kdp:

                while darkbluechunkcoord - kdp >= (gkdpv):
                    kdp += (gkdpv)

                y += (gss * kdp) // (gkdpv)
                darkbluechunkcoord -= kdp


            draw.fillRect(darkbluechunkcoord, y, gss, gss, Qt.darkBlue)
            # loadper += 1;
            # if loadper == loadperchunk * loadpertd and MainApplication.stoploadfs == False:
            #     loadpertd += 1
            #     loadperfs +=1
            #     print(loadperfs)
            kdp = gkdpv
            i += 1
            y=0
        i = 0
        y = 0
        kdp = gkdpv
        gss = int(gkdpv // gscu)
        for _ in range(1, len(greenchunklist) + 1):

            greenchunkcoord = greenchunklist[i] * gss

            if greenchunkcoord >= kdp:

                while greenchunkcoord - kdp >= (gkdpv):
                    kdp += (gkdpv)

                y += (gss * kdp) // (gkdpv)
                greenchunkcoord -= kdp

            draw.fillRect(greenchunkcoord, y, gss, gss, QColor(34, 186, 34))
            if showneighborcount == True:
                draw.drawText(greenchunkcoord + (gss//2), y + (gss//2), 1200, 1200, 0, str(Count(greenchunklist[i])))
            loadper += 1;
            # if loadper == loadperchunk * loadpertd and MainApplication.stoploadfs == False:
            #     loadpertd += 1
            #     loadperfs +=1
            #     print(loadperfs)

            kdp = gkdpv
            i += 1
            y = 0
        i = 0
        y = 0
        kdp = gkdpv
        gss = int(gkdpv // gscu)
        for _ in range(1, len(yellowchunklist) + 1):

            yellowchunkcoord = yellowchunklist[i] * gss

            if yellowchunkcoord >= kdp:

                while yellowchunkcoord - kdp >= (gkdpv):
                    kdp += (gkdpv)

                y += (gss * kdp) // (gkdpv)
                yellowchunkcoord -= kdp

            draw.fillRect(yellowchunkcoord, y, gss, gss, QColor(255, 230, 117))
            # loadper += 1;
            # if loadper == loadperchunk * loadpertd and MainApplication.stoploadfs == False:
            #     loadpertd += 1
            #     loadperfs +=1
            #     print(loadperfs)
            kdp = gkdpv
            i += 1
            y = 0
        i = 0
        y = 0
        kdp = gkdpv
        gss = int(gkdpv // gscu)
        for _ in range(1, len(brownchunklist) + 1):

            brownchunkcoord = brownchunklist[i] * gss

            if brownchunkcoord >= kdp:

                while brownchunkcoord - kdp >= (gkdpv):
                    kdp += (gkdpv)

                y += (gss * kdp) // (gkdpv)
                brownchunkcoord -= kdp

            draw.fillRect(brownchunkcoord, y, gss, gss, QColor(181, 133, 0))
            # loadper += 1;
            # if loadper == loadperchunk * loadpertd and MainApplication.stoploadfs == False:
            #     loadpertd += 1
            #     loadperfs +=1
            #     print(loadperfs)
            kdp = gkdpv
            i += 1
            y = 0
        i = 0
        y = 0
        kdp = gkdpv
        gss = int(gkdpv // gscu)
        for _ in range(1, len(bluechunklist) + 1):

            bluechunkcoord = bluechunklist[i] * gss

            if bluechunkcoord >= kdp:

                while bluechunkcoord - kdp >= (gkdpv):
                    kdp += (gkdpv)

                y += (gss * kdp) // (gkdpv)
                bluechunkcoord -= kdp

            draw.fillRect(bluechunkcoord, y, gss, gss, Qt.blue)
            # loadper += 1;
            # if loadper == loadperchunk * loadpertd and MainApplication.stoploadfs == False:
            #     loadpertd += 1
            #     loadperfs +=1
            #     print(loadperfs)
            kdp = gkdpv
            i += 1
            y = 0
        i = 0
        y = 0
        kdp = gkdpv
        gss = int(gkdpv // gscu)
        for _ in range(1, len(villagechunklist) + 1):

            villagechunkcoord = villagechunklist[i] * gss

            if villagechunkcoord >= kdp:

                while villagechunkcoord - kdp >= (gkdpv):
                    kdp += (gkdpv)

                y += (gss * kdp) // (gkdpv)
                villagechunkcoord -= kdp

            draw.fillRect(villagechunkcoord, y, gss, gss, QColor(34, 186, 34))
            draw.fillRect(villagechunkcoord+(gss // 5), y+(gss // 5), gss-((gss // 5) * 2), gss-(gss//5), Qt.white)
            painter = QPainter()
            path = QPainterPath()
            painter.begin(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setBrush(QColor(255, 38, 67))
            path.moveTo(villagechunkcoord, y+(2*(gss // 5)))
            path.lineTo(villagechunkcoord+gss, y+(2*(gss // 5)))
            path.lineTo(villagechunkcoord+(gss//2), y)
            path.lineTo(villagechunkcoord, y+(2*(gss // 5)))
            painter.drawPath(path)

            # loadper += 1;
            # if loadper == loadperchunk * loadpertd and MainApplication.stoploadfs == False:
            #     loadpertd += 1
            #     loadperfs +=1
            #     print(loadperfs)
            kdp = gkdpv
            i += 1
            y = 0
        i = 0
        y = 0
        kdp = gkdpv
        gss = int(gkdpv // gscu)
        for _ in range(1, len(citychunklist) + 1):

            citychunkcoord = citychunklist[i] * gss

            if citychunkcoord >= kdp:

                while citychunkcoord - kdp >= (gkdpv):
                    kdp += (gkdpv)

                y += (gss * kdp) // (gkdpv)
                citychunkcoord -= kdp
            draw.fillRect(citychunkcoord, y, gss, gss, QColor(34, 186, 34))
            draw.fillRect(citychunkcoord, y+(2*(gss//5)), gss, gss-(2*(gss//5)), Qt.gray)
            draw.fillRect(citychunkcoord, y, gss-(4*(gss//5)), gss - (3 * (gss // 5)), Qt.gray)
            draw.fillRect(citychunkcoord+(2*(gss//5)), y, gss - (4*(gss//5)), gss - (3 * (gss // 5)), Qt.gray)
            draw.fillRect(citychunkcoord + (4 * (gss // 5)), y, gss-(4*(gss//5)), gss - (3 * (gss // 5)), Qt.gray)
            draw.fillRect(citychunkcoord + (2 * (gss // 5)), y+(4*(gss//5)), gss - (4 * (gss // 5)), gss - (4 * (gss // 5)), Qt.darkGray)
            if MakeCityNames == True:
                r = random.randint(2, 4)
                if r == 2:
                    draw.drawText(citychunkcoord-(2*gss), y-gss, gss+(2*gss), 5*gss, 5, namesyllables[random.randint(0, len(namesyllables)-1)]+namesyllables[random.randint(0, len(namesyllables)-1)])
                elif r==3:
                    draw.drawText(citychunkcoord - (2 * gss), y-gss, gss + (2 *gss), 5*gss, 5, namesyllables[random.randint(0, len(namesyllables)-1)] + namesyllables[random.randint(0, len(namesyllables)-1)]+namesyllables[random.randint(0, len(namesyllables)-1)])
                elif r==4:
                    draw.drawText(citychunkcoord - (2 * gss), y-gss, gss + (2 * gss), 5*gss, 5,namesyllables[random.randint(0, len(namesyllables)-1)] + namesyllables[random.randint(0, len(namesyllables)-1)] + namesyllables[random.randint(0, len(namesyllables)-1)] + namesyllables[random.randint(0, len(namesyllables)-1)])
            # loadper += 1;
            # if loadper == loadperchunk * loadpertd and MainApplication.stoploadfs == False:
            #     loadpertd += 1
            #     loadperfs +=1
            #     print(loadperfs)
            kdp = gkdpv
            i += 1
            y = 0
        MainApplication.p +=1
        MainApplication.stoploadfs = True
        #print(MainApplication.p)


def RenderMap():

    app = QtWidgets.QApplication(sys.argv)

    w = MainApplication()


    sys.exit(app.exec_())







while isreallydone == False:
    if donecalculating == True:
        RenderMap();
        isreallydone = True

