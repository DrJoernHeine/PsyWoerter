import time
import os
import sys
import random



CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'
colors = [CRED, CYELLOW, CGREEN, CBLUE]



def setWindowScheme():
    os.system('color f0')
    os.system('mode con: cols=60 lines=20')

def resetWindowScheme():
    os.system("color 07")



class Screen():

    def __init__(self, nRows):
        self.rows = []
        self.nRows= nRows
        for row in range(self.nRows):
            self.rows.append("")

    def showString(self, row, string):
        self.rows[row] = string
        self.clearScreen()
        for row in range(self.nRows):
            if row > 0:
                print(CBLACK + self.rows[row])
            else:
                print(self.rows[row])

    def clearRows(self):
        for row in range(self.nRows):
            self.rows[row] = ""

    def clearScreen(self):
        try:
            os.system('cls')
        except:
            try:
                os.system('clear')
            except NotImplementedError:
                print("Reset of screen for operating system not supported.")




class UserInput():

    def __init__(self, screen):
        self.screen = screen

    def breakApp(self, string=""):
        self.screen.clearRows()
        for t in range(5, 0, -1):
            self.screen.showString(0, string+"Programm wird in "+str(t)+" Sekunden geschlossen.")
            time.sleep(1)
        resetWindowScheme()
        sys.exit()

    def getInput(self):
        i = 0
        while i<50:
            self.screen.showString(1, "Wähle ein Wort mit '1', '2' oder '3' und drücke Enter:")
            inp = input()
            if inp =="Exit":
                self.breakApp()
            try:
                inp = int(inp)
            except:
                inp = -1
            if 1<=inp<=3:
                return str(inp)
            time.sleep(0.001)
            i+=1
        self.breakApp("Keine gültige Eingabe. ")



class Words():

    def __init__(self, path):
        self.words = []
        self.path = path
        try:
            with open(self.path, 'r') as file:
                   for word in file:
                       word = word.strip()
                       if word == ';':
                           break
                       self.words.append(word)
        except:
            print("Wörter.txt Datei nicht gefunden!")
            input("Drücke Enter um Programm zu schließen.")
            sys.exit()
        self.nWords = len(self.words)


    def getRndWord(self):
        posWord = random.randint(0, self.nWords - 1)
        return self.words[posWord]


    def getNRndWords(self, nWords):
        out = []
        for _ in range(nWords):
            out.append(self.getRndWord())
        return out


    def strNRndWords(self, nWords):
        words = self.getNRndWords(nWords)
        string = ""
        for i in range(nWords):
            string += colors[random.randint(0, len(colors)-1)] + "Wort " +str(i + 1)+": " + words[i] + "  "
        return string



if __name__ == "__main__":
    path = "C:/Users/Jörn/Desktop/PsyWords/Woerter.txt"
    setWindowScheme()

    scr = Screen(10)
    uIn = UserInput(scr)
    wrds= Words(path)


    stop = False
    while not stop:
        scr.showString(0, wrds.strNRndWords(3))
        inp = uIn.getInput()
        scr.showString(2,inp)


