#Brandon Deo
#Project 2
#MWF 2:30-3:20
#December 11, 2013

import turtle
from random import *

#A Class of objects for each letter
class Key(object):
    def __init__(self,letter,top,left,bottom,right):
        self.letter = letter
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
    def __str__(self):
        return(self.letter)

class Board(object):
    def __init__(self,squaresize,fontsize,alphanumeric):
        self.squaresize = squaresize
        self.alphanumeric = alphanumeric
        self.fontsize = fontsize
        self.top = self.gettoploc()
        self.left = self.getleftloc()
        self.keyboard = self.makeboard()
        self.wordtop = self.getwordtop()
        self.wordleft = self.getwordleft()
        self.curtop = self.wordtop
        self.curleft = self.wordleft
        self.senttop = self.wordtop + 3*self.squaresize
        self.sentleft = self.wordleft - 1.5*self.squaresize

    #calculates and returns a number: the left loc(x coord) of where the
    #board will go, calculated  by 0-squaresize*5
    def getleftloc(self):
        return(0-self.squaresize*5)
    
    #calculates and return a number: the top loc (y coord) for where the
    #board will go, calculated by the squaresize * 2
    def gettoploc(self):
        return(self.squaresize*2)
    
    #calculates and returns a number: the top loc (y coord) for where the keys
    #you are typing in will go, calculated by the top property + sqauresize*2
    def getwordtop(self):
        return(self.top + self.squaresize*2)
    
    #calculates and returns a number: the left loc (x coord) for where the keys
    #you are typing in will go calculated by: the left property - squaresize*2
    def getwordleft(self):
        return(self.left - self.squaresize*2)
    
    #draws each individual key in turtle. No loops.
    #input: key object (with letter and all l/r/t/b coords)
    #This function goes to the key's left and bottom coords and then with the
    #pen up goes forward (squaresize - fontsize)/2. Then writes the letter
    #of the key in the fontsize of the board.
    def drawsquare(self,k):
        turtle.penup()
        turtle.goto(k.left,k.bottom)
        turtle.forward((self.squaresize - self.fontsize)/2)
        turtle.pendown()
        turtle.write(str(k.letter), font = self.fontsize)
        turtle.penup()
        return
    
    # This method draws the board in turtle. It is the heart of the Board class. It writes out the keyboard in turtle’s
    # window, while simultaneously creating a list of key objects.  The list of key objects is returned from this method.
    #    
    # It first goes to the top left Board properties for the starting position for the keyboard.  Then, in 4 separate lines,
    # ach squaresize high and 10 square sizes in length (meaning each line displays 10 characters, each spaced squaresize
    # apart. The character being displayed is chosen in order from the alphanumeric keyboard.  
    #   
    # So for each character being displayed, you should make a key object first.  The key object will consist of  the current
    # letter from the alphanumeric list property of the board, the y (top) location of where the letter is being written on
    # the board (where the pen currently is + the squaresize), the x (left) position (the current x coordinate on the board),
    # the bottom position (the current y position on the board) and the rightmost position (the left position + the squaresize).  
    #   
    # Once you have made the key, you should then draw the key on the keyboard using the drawsquare method (above), and 
    # you should append the key to the keyboard list.
    #   
    # When you are done drawing the keyboard, you should return the keyboard list, which should set the keyboard property
    # to be the list you’ve created.  This list is a list of key objects, so now you know where every letter is located on the
    # turtle screen.    
    def makeboard(self):
        ls = []
        turtle.penup()
        z = self.left - self.squaresize
        a = self.top + self.squaresize
        ct = 0
        turtle.goto(z,a)
        for y in range(4):
            a -= self.squaresize
            for x in range(10):
                z += self.squaresize
                turtle.goto(z,a)
                let = Key(self.alphanumeric[ct],(turtle.ycor() + self.squaresize),(turtle.xcor()),(turtle.ycor()),(turtle.xcor()+self.squaresize))
                ls.append(let)
                ct += 1
                self.drawsquare(let)
            z = self.left - self.squaresize
        return(ls)
#Class for word objects.

class Word(object):
    def __init__(self,word,ct):
        self.word = word
        self.ct = ct
        self.x = 0
        self.y = 0
    #Makes a string
    def __str__(self):
        return(self.word+ ": " +str(self.ct))

#Class for WordPrediction Obj. Handles finding where you clicked on keyboard
#or if you clicked on a predicted word, adding it to the sentence, producing
#the list of prediction words and displaying it, and clearing the screen
#of old word prediction lists and old keys typed in after a word is selected
#or space key is pressed

class WordPredict(object):
    def __init__(self,board,wordlist):
        self.board = board
        self.wordlist = wordlist
        self.currword = ""
        self.predictionls = []
        self.sentence = ""
        self.enterword()
    #Allows user to click on screen and get the x and y coord, the method
    #findletter is called with the x and y coords of where you clicked
    def enterword(self):
        turtle.onscreenclick(self.findletter)

    # This method automatically gets as input parameters (other than self) the x and y coordinates of where you clicked on the
    # screen.  First it checks to see if you clicked on the prediction list (the predictionls property).  Remember, each Word object
    # in the predictionls property has the wordobj.x and  wordobj.y coordinates of where it is placed on the screen. So you should
    # check to seewhether the x and y coordinates the user clicked on are between the wordobj.x and wordobj.y coordinates and
    # the wordobj.x + self.board.squaresize and wordobj.y + 300 (I just made up the length of the word – I was lazy) coordinates.
    # If it is, the function should call the printsent method with the word object’s word property
    #
    # If the x and y coordinates clicked on are not within the boundaries of where the word prediction list was printed on the
    # screen, you then want to check to see which letter in the board the user clicked on.  For this you’ll use the board.keyboard
    # property.  The board.keyboard property is a list of Key objects.  (So you can say
    # for k in self.board.keyboard
    # and this will make k be each key object in the keyboard.  Each Key objects has a top, left, bottom, and right properties.  The
    # function should check to see if the clicked on x and y coordinates are in between the key object’s coordinates.  If so, it
    # should check to see if the letter clicked on was a space (k.letter == “ “) and, if it was, it should call printsent with the
    # curword property.  Otherwise it should call the printletter method with the Key object’s letter property (e.g., k.letter) 

    def findletter(self,x,y):
        for word in self.predictionls:
            if (x > word.x) and (x < (word.x + 300)) and (y > word.y) and (y < (word.y + self.board.squaresize)):
                return(self.printsent(word.word))
        for k in self.board.keyboard:
            if x > k.left and x < k.right and y > k.bottom and y < k.top:
                if k.letter == " ":
                    return(self.printsent(self.currword))
                else:
                    return(self.printletter(k.letter))
                    
        return
    #input: Letter
    #Prints letter on the board in appropriate space, adds letter to curword property, adjusts the current position
    #of where the next letter should be printed on the board, changes the predictionls property to hold the words
    #from the text that match the current word being typed in by calling the gettopwords method, sorts that predictionls
    #by calling sortlist method. Calls the writeprediction method to write out the new predictionls propery
    def printletter(self,letter):
        turtle.penup()
        turtle.goto(self.board.curleft,self.board.curtop)
        turtle.pendown()
        self.currword += letter
        turtle.write(letter,font = ("Arial",self.board.fontsize))
        self.board.curleft = self.board.curleft + self.board.squaresize
        self.predictionls = self.gettopwords()
        self.sortlist()
        self.writeprediction()
        return
    #input: string(word) self
    #adds the string to the current sentence then clears out the area where the letters the user was clicking on
    #showing up and it clears out the area where the prediction words were printed out on the screen.
    #prints out the sentence, and clears out the curword property.
    def printsent(self,word):
        self.sentence += " " + word
        self.board.curtop = self.board.wordtop
        self.board.curleft = self.board.wordleft
        self.clearlist(-317, 206, 273, 138)
        x = self.board.left
        y = self.board.top - self.board.squaresize*4
        x2 = x+300
        y2 = y-self.board.squaresize*6
        self.clearlist(x-1,y,x2,y2)
        turtle.penup()
        turtle.goto(self.board.sentleft,self.board.senttop)
        turtle.write(self.sentence,font=("Arial",self.board.fontsize))
        turtle.penup()
        self.currword = ""
        return
    #input: 4 ints (x,y coords of top left corner) (x2,y2 coords of the bottom right corner to be cleared
    #This function sets the turtle.color('white','white') it then starts with turtle.begin_fill() then draws
    #a large rect using the coordinates and then ends with turtle.endfill() and sets the turtle.pencolor('black')
    def clearlist(self,x,y,x2,y2):
        turtle.color('white','white')
        turtle.goto(x,y)
        turtle.begin_fill()
        turtle.goto(x2,y)
        turtle.goto(x2,y2)
        turtle.goto(x,y2)
        turtle.goto(x,y)
        turtle.end_fill()
        turtle.pencolor('black')
        return
    #Writes out the predictionls property on the board. Clears off the old predictionls and then it writes
    #the new one onto the board. For each word obj in the list, it sets the x and y coords of where the
    #word is being predicted on the board.
    def writeprediction(self):
        x = self.board.left
        y = self.board.top - self.board.squaresize*4
        x2 = x+300
        y2 = y-self.board.squaresize*6
        self.clearlist(x-1,y,x2,y2)
        lstop = self.board.top - self.board.squaresize*5
        if len(self.predictionls)<5:
            y = len(self.predictionls)
        else:
            y = 5
        for x in range(y):
            turtle.penup()
            turtle.goto(self.board.left,lstop)
            self.predictionls[x].x = self.board.left
            self.predictionls[x].y = lstop
            turtle.pendown()
            turtle.write(self.predictionls[x],font = ("Arial",self.board.fontsize))
            turtle.penup()
            lstop -= self.board.squaresize
        return
    #no input but self
    #output: list of words from the wordlist property that match the curword property, which is letters clicked so far
    def gettopwords(self):
        ls = []
        for x in self.wordlist:
            ct = 0
            for y in range(len(self.currword)):
                if len(x.word)>= (y+1):
                    if self.currword[y] == x.word[y]:
                        ct += 1
            if ct == len(self.currword):
                    ls.append(x)
        return(ls)
    #no input but self
    #returns nothing
    #Takes the predictionls property of the class and sorts it in order of the word counts of the Words in the predictionls
    #list. It sorts from high-> low. Sets the predictionls property to the sorted version of the list.
    def sortlist(self):
        self.predictionls.sort(key=lambda x: x.ct, reverse=True)
        return
    #Diagnostic/Debugging Method
    def printout(self,k,x,y):
        print("Letter is: " + k.letter)
        print("Letter x is: " +str(k.left))
        print("Letter y is: " +str(k.top))
        print("Click x is: " +str(x))
        print("Click y is: " +str(y))
        return

#Class to make the list of word objects
class WList(object):
    def __init__(self,alpha,doc):
        self.alpha = alpha
        self.list = self.readfile(doc)
        self.wordlist = self.makewordlist()
    #Input: list of strings
    #This function strips all punctuation other than ', and then returns the list of strings
    def stripchar(self,ls):
        newls = []
        for x in ls:
            z = ""
            for y in x:
                if y.lower() in self.alpha:
                    if y != " ":
                        z+=y.lower()
                    elif len(z)>0:
                        newls.append(z)
                        z = ""
        return(newls)

    #Input: Document name
    #Opens the file, reads it into a list and then calls the stripchar method with the list to strip out the characters
    #and create a list of lower case words with no punctuation and returns the list.
    def readfile(self,doc):
        f = open(doc,'r')
        ls = []
        for line in f:
            ls.append(line.strip())
        f.close()
        ls = self.stripchar(ls)
        return(ls)
    #no input
    #Goes through the list of words and creats a list of Word Objects. Each word object should have both its word
    #and the count of how many times it occured in the Wlist list property. Each word should occur once in this new list and
    #it should be sorted in order of the word (Alphabetized). The alphabetized list of Word Objects is returned and becomes the
    #wordlist property
    def makewordlist(self):
        wordobjs = []
        words = []
        for x in self.list:
            if x not in words:
                word = Word(x,self.list.count(x))
                wordobjs.append(word)
                words.append(x)
        wordobjs.sort(key=lambda x: x.word)
        return(wordobjs)
def main():
    alpha = ['1','2','3','4','5','6','7','8','9','0',
             'q','w','e','r','t','y','u','i','o','p',
             'a','s','d','f','g','h','j','k','l',' ',
             'z','x','c','v','b','n','m','\'',' ',' ']
    turtle.setup(700,640,600,0)
    turtle.speed(0)
    turtle.hideturtle()
    keyboard = Board(40,18,alpha)
    wordlist = WList(alpha,"GEChap1.txt")
    word = WordPredict(keyboard,wordlist.wordlist)

main()
