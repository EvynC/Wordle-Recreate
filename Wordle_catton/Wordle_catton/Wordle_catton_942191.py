import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

list = []
word_num = []
yesno = []
with open('five_letter_words_500.txt') as file: 
    for word in file: 
        list.append((word.strip().upper()))
global selectedword
selectedword = (list[random.randint(0, 499)]).upper()
global win 
win = False
global holder 
holder = 0
box_list = []
global b 
b = 0
alpha_list = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L', 'Enter','Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Delete']
def makeWidget():
    app = QApplication(sys.argv) 
    QFontDatabase.addApplicationFont("Roboto-BlackItalic.ttf")
    widget = QWidget()
    widget.setWindowTitle('Wordle - Catton')
    widget.setFixedSize(600, 900)
    widget.setStyleSheet(
        'background-color: white;'
        'color: black;'
    )
    wordle = QLabel('Wordle', widget)
    wordle.setWindowTitle('Wordle - Catton')
    wordle.setFont(QFont('Roboto'))
    wordle.setGeometry(0, 0, 600, 50)
    wordle.setAlignment(Qt.AlignCenter)
    wordle.setStyleSheet(
        'background-color: white;'
        'color: black;'
        'font-size: 30px;'
    )

    wordoutput = QLabel('That is not a word... Try again.', widget)
    wordoutput.setAlignment(Qt.AlignCenter)
    wordoutput.setFont(QFont('Roboto'))
    wordoutput.setStyleSheet(
        'font-size: 35px;'
    )
    wordoutput.setGeometry(0, 500, 600, 200)
    wordoutput.hide()

    text_box = QLabel(str(selectedword), widget)
    text_box.setGeometry(0, 700, 600, 100)
    text_box.setFont(QFont('Roboto'))
    text_box.setAlignment(Qt.AlignCenter)
    text_box.setStyleSheet(
        'font-size: 32px'
    )
    text_box.hide()

    checkbutton = QPushButton( 'Answer:' , widget)
    checkbutton.setGeometry(140, 700, 100, 100)
    checkbutton.setFont(QFont('Roboto'))
    checkbutton.setStyleSheet(
        'font-size: 28px'
    )
    checkbutton.mousePressEvent = lambda event: text_box.show()

    make_grid(widget, box_list)
    make_keys(widget, alpha_list, box_list, wordoutput)

    widget.show()
    sys.exit(app.exec_())

def make_grid(parent, box_list):
    offsetY = 55
    for x in range(6): 
        offsetX= 165
        for y in range(5): 
            label = QLabel(parent)
            label.setGeometry(offsetX, offsetY, 50, 50)
            label.setAlignment(Qt.AlignCenter)
            label.setFont(QFont('Roboto'))
            label.setStyleSheet(
                'border: 1px solid black;'
                'font-size: 35px;'
            )
            box_list.append(label)
            offsetX += 55
        offsetY += 55

def delete(text, wordoutput):
    global b  
    global win
    if text == 'Delete':
        if len(word_num) != 0:
            
            if len(word_num) <= 5 and len(word_num) <= 5 and holder == 0 and win == False: 
                b -= 1
                box_list[b].setText('')
                word_num.remove(word_num[len(word_num)-1])
                wordoutput.hide()

            if len(word_num) > 5 and len(word_num) <= 10 and holder == 1: 
                b -= 1
                box_list[b].setText('')
                word_num.remove(word_num[len(word_num)-1])
                wordoutput.hide()

            if len(word_num) > 10 and len(word_num) <= 15 and holder == 2:
                b -= 1
                box_list[b].setText('')
                word_num.remove(word_num[len(word_num)-1])
                wordoutput.hide()

            if len(word_num) > 15 and len(word_num) <= 20 and holder == 3: 
                b -= 1
                box_list[b].setText('')
                word_num.remove(word_num[len(word_num)-1])
                wordoutput.hide()

            if len(word_num) > 20 and len(word_num) <= 25 and holder == 4: 
                b -= 1
                box_list[b].setText('')
                word_num.remove(word_num[len(word_num)-1])
                wordoutput.hide()


            if len(word_num) > 25 and len(word_num) <= 30 and holder == 5:
                b -= 1
                box_list[b].setText('')
                word_num.remove(word_num[len(word_num)-1])
                wordoutput.hide()

          

def select_letter(widget, text, box_list, wordoutput):
    global b
    global holder
    global win
    if b < 0: 
        b = 0
    if box_list != 0 and win == False: 
        if text != 'Delete' and text != 'Enter':
            if text != '':
                
                if len(word_num) <= 5 and len(word_num) < 5 and holder == 0:   
                    box_list[b].setText(text)
                    b += 1
                    word_num.append(text)
                
                if len(word_num) >= 5 and len(word_num) < 10 and holder == 1: 
                    box_list[b].setText(text)
                    b += 1
                    word_num.append(text)

                if len(word_num) >= 10 and len(word_num) < 15 and holder == 2: 
                    box_list[b].setText(text)
                    b += 1
                    word_num.append(text)

                if len(word_num) >= 15 and len(word_num) < 20 and holder == 3: 
                    box_list[b].setText(text)
                    b += 1
                    word_num.append(text)
                
                if len(word_num) >= 20 and len(word_num) < 25 and holder == 4: 
                    box_list[b].setText(text)
                    b += 1
                    word_num.append(text)

                if len(word_num) >= 25 and len(word_num) <= 30 and holder == 5: 
                    box_list[b].setText(text)
                    b += 1
                    word_num.append(text)
                    

        elif text == 'Enter': 
            if len(word_num) == 5: 
                check(text, 0, wordoutput)
            if len(word_num) == 10: 
                check(text, 5, wordoutput)
            if len(word_num) == 15: 
                check(text, 10, wordoutput)
            if len(word_num) == 20: 
                check(text, 15, wordoutput)
            if len(word_num) == 25: 
                check(text, 20, wordoutput)
            if len(word_num) == 30: 
                check(text, 25, wordoutput)
            
               
def check(text, x, wordoutput):
    
    global selectedword
    guessword = ''
    global isword 
    isword = False
     # if it is green or yellow
    for l in range(x, x+5, 1):
        guessword += word_num[l]
        if len(guessword) == 5:
            if guessword in list:
                isword = True
            else:
                isword = False
                wordoutput.show()

                

        
    if text == 'Enter' and isword == True: 
        global win 
        global holder
        if len(word_num) != 0: 
            correctvar = 0 
            holder += 1             
            b = x 
            if word_num[x] == selectedword[0]: 
                box_list[x].setStyleSheet(
                    'background-color: Green;'
                    'font-size: 35px;'
                    )
                correctvar += 1
                yesno.append('yes')
            else: yesno.append('no')
            x += 1
            if word_num[x] == selectedword[1]: 
                box_list[x].setStyleSheet(
                    'background-color: Green;'
                    'font-size: 35px;'
                    )
                correctvar += 1
                yesno.append('yes')
            else: yesno.append('no')
            x+= 1
            if word_num[x] == selectedword[2]: 
                box_list[x].setStyleSheet(
                    'background-color: Green;'
                    'font-size: 35px;'
                    )
                correctvar += 1
                yesno.append('yes')
            else: yesno.append('no')
            x += 1
            if word_num[x] == selectedword[3]: 
                box_list[x].setStyleSheet(
                    'background-color: Green;'
                    'font-size: 35px;'
                    )
                correctvar += 1
                yesno.append('yes')
            else: yesno.append('no')
            x += 1
            if word_num[x] == selectedword[4]: 
                box_list[x].setStyleSheet(
                    'background-color: Green;'
                    'font-size: 35px;'
                    )
                correctvar += 1
                yesno.append('yes')
            else: yesno.append('no')

            if correctvar == 5: 
                wordoutput.setText('You Won')
                wordoutput.show()
                win = True
            elif len(word_num) == 30: 
                win = True
                wordoutput.setText('You Lost')
                wordoutput.show()        
            for l in range(b, b+5, 1):
                if selectedword.find(word_num[l]) !=  -1 and yesno[l] == 'no': 
                    box_list[l].setStyleSheet(
                    'background-color: Yellow;'
                    'font-size: 35px;'
                    )           
def make_keys(parent, alpha_list, box_list, wordoutput):
    offsetX = 50
    offsetY = 400
    for x in range(len(alpha_list)):
        button = QPushButton(parent)
        button.setText(alpha_list[x])
        button.setFont(QFont('Roboto'))
        button.setGeometry(offsetX, offsetY, 45, 45)
        button.setStyleSheet('font-size: 18px;')
        text = alpha_list[x]
        button.clicked.connect(lambda checked, text = alpha_list[x]: select_letter(parent, text, box_list, wordoutput))       
        button.clicked.connect(lambda checked, text = alpha_list[x]: delete(text, wordoutput))       
               



        if x == 9: 
            offsetX = 75
            offsetY += 55
        elif x == 18: 
            offsetX = 50    
            offsetY += 55
        else: 
            if x == 19 or x == 27: 
                button.setGeometry(offsetX, offsetY, 70, 45)
                offsetX += 25
            offsetX += 50 
if __name__ == '__main__':
    makeWidget()