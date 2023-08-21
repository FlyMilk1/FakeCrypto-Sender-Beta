from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QPainterPath, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
import math
from main import redchunklist
from main import blackchunklist
from main import greenchunklist
from main import yellowchunklist
from main import Count
from main import gsc
from main import gscu
from main import donecalculating
import sys;
import time
#gkdpv needs to be a divisible on gsc value
gkdpv = 1000

i = 0;
optimizedscrsize = True;
showneighborcount = False;
isreallydone = False
# def GrassChunk():
class MainApplication(QWidget):
    stoploadfs = False
    p = 0
    def __init__(self):
        super().__init__()
        if optimizedscrsize == True:
            self.setGeometry(gkdpv, gkdpv, gkdpv, gkdpv)
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

        for _ in range(1, len(redchunklist) + 1):
            redchunkcoord = redchunklist[i]*gss


            if redchunkcoord >= kdp:
                while redchunkcoord - kdp >= (gkdpv):
                    kdp += (gkdpv)

                y += (gss * kdp) // (gkdpv)
                redchunkcoord -= kdp



            draw.fillRect(redchunkcoord,y,gss,gss, Qt.blue)
            #draw.drawText(redchunkcoord+50, y+50, 1200, 1200, 0, str(redchunklist[i]))
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
        for _ in range(1, len(blackchunklist) + 1):

            blackchunkcoord = blackchunklist[i] * gss




            if blackchunkcoord >= kdp:

                while blackchunkcoord - kdp >= (gkdpv):
                    kdp += (gkdpv)

                y += (gss * kdp) // (gkdpv)
                blackchunkcoord -= kdp


            draw.fillRect(blackchunkcoord, y, gss, gss, Qt.darkBlue)
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
        MainApplication.p +=1
        MainApplication.stoploadfs = True
        #print(MainApplication.p)


def RenderMap():

    app = QtWidgets.QApplication(sys.argv)

    w = MainApplication()
    w.show()

    sys.exit(app.exec_())







while isreallydone == False:
    if donecalculating == True:
        RenderMap();
        isreallydone = True

