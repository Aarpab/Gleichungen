from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import time

class Testen(Thread) :
    def __init__(self, z, r1, r2, variable, stellen, gewechselt) :
        Thread.__init__(self)
        self.z = z
        self.r1 = r1
        self.r2 = r2
        self.variable = variable
        self.stellen = stellen
        self.gewechselt = gewechselt
        self.plus = 1
        self.status = "hoch"
        self.minus = 0.1

    def run(self) :
        while True :
            neu = []
            alt = self.r1
            for x in self.r1 :
                if x != self.variable :
                    neu.append(x)
                else :
                    neu.append(str(self.z))

            self.r1 = neu
            i = 0 
            while i < len(self.r1) - 1 :
                x = self.r1[i]
                if x == "^" :
                    z1 = self.r1[i - 1]
                    z2 = self.r1[i + 1]
                    
                    ergebnis = float(z1) ** float(z2)

                    l = [*self.r1]

                    l[i - 1] = "löschen"
                    l[i + 1] = "löschen"
                    l[i] = "löschen"

                    for i2 in range(3) :
                        l.remove("löschen")

                    if ergebnis % 1 == 0 :
                        ergebnis = int(ergebnis)

                    l.insert(i - 1, str(ergebnis))

                    self.r1 = []
                    for x in l :
                        self.r1.append(x)

                    i -= 1
                
                i += 1 
            
            i = 0 
            while i < len(self.r1) - 1 :
                x = self.r1[i]
                if x == "*" or x == "/" :
                    z1 = self.r1[i - 1]
                    z2 = self.r1[i + 1]

                    if x == "*" :
                        ergebnis = float(z1) * float(z2)

                    elif x == "/" :
                        ergebnis = float(z1) / float(z2)

                    l = [*self.r1]

                    l[i - 1] = "löschen"
                    l[i + 1] = "löschen"
                    l[i] = "löschen"

                    for i2 in range(3) :
                        l.remove("löschen")

                    if ergebnis % 1 == 0 :
                        ergebnis = int(ergebnis)

                    l.insert(i - 1, str(ergebnis))

                    self.r1 = []
                    for x in l :
                        self.r1.append(x)

                    i -= 1
                
                i += 1 

            i = 0 
            while i < len(self.r1) - 1 :
                x = self.r1[i]
                if x == "+" or x == "-" :
                    z1 = self.r1[i - 1]
                    z2 = self.r1[i + 1]

                    if x == "+" :
                        ergebnis = float(z1) + float(z2)

                    elif x == "-" :
                        ergebnis = float(z1) - float(z2)

                    l = [*self.r1]

                    l[i - 1] = "löschen"
                    l[i + 1] = "löschen"
                    l[i] = "löschen"

                    for i2 in range(3) :
                        l.remove("löschen")

                    if ergebnis % 1 == 0 :
                        ergebnis = int(ergebnis)

                    l.insert(i - 1, str(ergebnis))

                    self.r1 = []
                    for x in l :
                        self.r1.append(x)

                    i -= 1

                i += 1 

            neu = ""
            for x in self.r1 :
                neu += x
            
            self.r1 = neu
            if self.r1 != None :
                if float(self.r1) == float(self.r2) :
                    ui.go = False

                    ui.richtig_button.click()

                    time.sleep(2)

                    stop = True
                    break
                elif float(self.r1) < float(self.r2) and self.status == "hoch" :
                    self.plus = self.minus
                    self.plus *= -1

                    self.status = "runter"

                    self.gewechselt = True
                    l = [*str(self.minus)]
                    
                    x = 1
                    for i in l :
                        if i == "." :
                            l.insert(x, "0")
                            break
                        x += 1 

                    neu = ""
                    for i in l :
                        neu += i

                    self.plus = float(self.plus)

                    self.minus = float(neu)

                    self.stellen += 1 

                    stop = False

                elif float(self.r1) > float(self.r2) and self.gewechselt and self.status == "runter" :
                    self.plus *= -1
                    self.plus = self.minus

                    self.status = "hoch"

                    l = [*str(self.minus)]

                    x = 0
                    for i in l :
                        if i == "." :
                            l.insert(x, "0")
                            break
                        x += 1 

                    neu = ""
                    for i in l :
                        neu += i

                    self.plus = float(self.plus)

                    self.minus = float(neu)

                    self.stellen += 1 
                    
                    stop = False

                else :
                    stop = False
                    
            self.z += self.plus 
            self.z = round(self.z, self.stellen)
            self.r1 = alt

            if stop :
                break
        
class Ui_Form(object):
    def setupUi(self, Form):
        self.go = True

        Form.setObjectName("Form")
        Form.resize(378, 442)
        self.output_rechenweg = QtWidgets.QTextBrowser(Form)
        self.output_rechenweg.setGeometry(QtCore.QRect(0, 161, 381, 281))
        self.output_rechenweg.setObjectName("output_rechenweg")
        self.input_gleichung = QtWidgets.QLineEdit(Form)
        self.input_gleichung.setGeometry(QtCore.QRect(80, 70, 211, 20))
        self.input_gleichung.setObjectName("input_gleichung")
        self.button = QtWidgets.QPushButton(Form)
        self.button.setGeometry(QtCore.QRect(80, 100, 70, 25))
        self.button.setObjectName("Button")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 30, 161, 16))
        self.label.setObjectName("label")
        self.richtig_button = QtWidgets.QPushButton(Form)
        self.richtig_button.setGeometry(QtCore.QRect(-100, -100, 70, 25))
        self.richtig_button.setObjectName("richtug_Button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.input_gleichung.textChanged.connect(self.schreiben)

        self.button.pressed.connect(self.loesen)

        self.richtig_button.pressed.connect(self.funk_richtig)

    def retranslateUi(self, Form):
        global _translate

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gleichungen"))
        self.label.setText(_translate("Form", "Schreibe die Gleichung in das Feld"))
        self.button.setText("lösen")

    def funk_richtig(self) :
        self.output_rechenweg.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">" + str(variable) + "=" + str(t.z) + "</span></p></body></html>"))

    def schreiben(self) :
        text = self.input_gleichung.text()

        if len(text) > 0 :
            zeichen = [*"1234567890abcdefghijklmnopqrstuvwxyz+-*/=.,^"]
            zahlen = [*"1234567890"]
            buchstaben = [*"abcdefghijklmnopqrstuvwxyz"]
            operatoren = [*"+-*/^.="]
            
            if not text[len(text) - 1] in zeichen :
                neu = ""

                i = 0
                while i < len(text) - 1 :
                    neu += text[i]
                    i += 1 

                self.input_gleichung.setText(neu)

            elif text[len(text) - 1] == "," :
                neu = ""

                for i in text :
                    if not i == "," :
                        neu += i
                    else :
                        neu += "."

                self.input_gleichung.setText(neu)

            elif text[len(text) - 1] in operatoren and text[len(text) - 2] in operatoren and text[len(text) - 1] != "-" :
                neu = ""

                i = 0 
                while i < len(text) - 1 :
                    neu += text[i]
                    i += 1 

                self.input_gleichung.setText(neu)

            elif text[len(text) - 1] == "-" and text[len(text) - 2] == "-" and len(text) > 1 :
                neu = ""

                i = 0 
                while i < len(text) - 1 :
                    neu += text[i]
                    i += 1 

                self.input_gleichung.setText(neu)
            
            elif text[len(text) - 1] in zahlen and text[len(text) - 2] in buchstaben :
                neu = ""

                i = 0 
                while i < len(text) - 1 :
                    neu += text[i]
                    i += 1 

                self.input_gleichung.setText(neu)

    def loesen(self) :
        global variable
        global t

        gleichung = self.input_gleichung.text()
        
        buchstaben = [*"abcdefghijklmnopqrstuvwxyz"]
        zahlen = [*"1234567890"]
        operatoren = [*"+-*/^="]

        i = 0 
        i2 = -1
        for x in gleichung :
            if i2 != -1 :
                if x in buchstaben and gleichung[i2] in buchstaben or x in buchstaben and gleichung[i2] in zahlen :
                    l = [*gleichung]

                    l.insert(i, "*")
                    
                    gleichung = ""

                    for y in l :
                        gleichung += y

                    i += 1 
                    i2 += 1 
            
            i += 1 
            i2 += 1 

        gleichung_l = []
        
        objekt = ""
        for x in gleichung :
            if x in operatoren :
                if x != "-" :
                    gleichung_l.append(objekt)
                    gleichung_l.append(x)
                    objekt = ""
                else :
                    if objekt == "" :
                        objekt += x
                    else :
                        gleichung_l.append(objekt)
                        gleichung_l.append(x)
                        objekt = ""
            else :
                objekt += x

        gleichung_l.append(objekt)

        gleichung = gleichung_l

        r1 = []
        r2 = []
        r = 1

        for i in gleichung :
            if i == "=" :
                r += 1
                continue

            if r == 1 :
                r1.append(i)
            elif r == 2 :
                r2.append(i)
        
        var = 2
        go = True
        for b in buchstaben :
            if b in r1 :
                var = 1
                for b2 in buchstaben :
                    if b2 in r2 :
                        go = False
                        break
            if not go :
                break
        
        if go :
            if var == 2 :
                r12 = r1
                r22 = r2

                r1 = r22
                r2 = r12

            i = 0 
            while i < len(r2) - 1 :
                x = r2[i]
                if x == "^" :
                    z1 = r2[i - 1]
                    z2 = r2[i + 1]
                    
                    ergebnis = float(z1) ** float(z2)

                    l = [*r2]

                    l[i - 1] = "löschen"
                    l[i + 1] = "löschen"
                    l[i] = "löschen"

                    for i2 in range(3) :
                        l.remove("löschen")

                    if ergebnis % 1 == 0 :
                        ergebnis = int(ergebnis)

                    l.insert(i - 1, str(ergebnis))

                    r2 = ""
                    for x in l :
                        r2 += x

                    i -= 1

                elif x == "*" or x == "/" :
                    z1 = r2[i - 1]
                    z2 = r2[i + 1]

                    if x == "*" :
                        ergebnis = float(z1) * float(z2)

                    elif x == "/" :
                        ergebnis = float(z1) / float(z2)

                    l = [*r2]

                    l[i - 1] = "löschen"
                    l[i + 1] = "löschen"
                    l[i] = "löschen"

                    for i2 in range(3) :
                        l.remove("löschen")

                    if ergebnis % 1 == 0 :
                        ergebnis = int(ergebnis)

                    l.insert(i - 1, str(ergebnis))

                    r2 = ""
                    for x in l :
                        r2 += x

                    i -= 1

                elif x == "+" or x == "-" :
                    z1 = r2[i - 1]
                    z2 = r2[i + 1]

                    if x == "+" :
                        ergebnis = float(z1) + float(z2)

                    elif x == "-" :
                        ergebnis = float(z1) - float(z2)

                    l = [*r2]

                    l[i - 1] = "löschen"
                    l[i + 1] = "löschen"
                    l[i] = "löschen"

                    for i2 in range(3) :
                        l.remove("löschen")

                    if ergebnis % 1 == 0 :
                        ergebnis = int(ergebnis)

                    l.insert(i - 1, str(ergebnis))

                    r2 = ""
                    for x in l :
                        r2 += x

                    i -= 1
                
                i += 1

            try :
                int(r2)
            except TypeError :
                r2 = r2[0]

            variablen = 0
            variablen_liste = []
            variable = ""
            status = "hoch"
            gewechselt = False
            plus = 1
            minus = 0.1
            stellen = 0

            for x in r1 :
                if x in buchstaben and not x in variablen_liste :
                    variablen_liste.append(x)
                    variablen += 1 

            if variablen == 1 :
                for x in r1 :
                    if x in buchstaben :
                        variable = x
                        break

            z = 0 
            while self.go :
                neu = []
                alt = r1
                for x in r1 :
                    if x != variable :
                        neu.append(x)
                    else :
                        neu.append(str(z))

                r1 = neu
                i = 0 
                while i < len(r1) - 1 :
                    x = r1[i]
                    if x == "^" :
                        z1 = r1[i - 1]
                        z2 = r1[i + 1]
                        
                        ergebnis = float(z1) ** float(z2)

                        l = [*r1]

                        l[i - 1] = "löschen"
                        l[i + 1] = "löschen"
                        l[i] = "löschen"

                        for i2 in range(3) :
                            l.remove("löschen")

                        if ergebnis % 1 == 0 :
                            ergebnis = int(ergebnis)

                        l.insert(i - 1, str(ergebnis))

                        r1 = []
                        for x in l :
                            r1.append(x)

                        i -= 1
                    
                    i += 1 
                
                i = 0 
                while i < len(r1) - 1 :
                    x = r1[i]
                    if x == "*" or x == "/" :
                        z1 = r1[i - 1]
                        z2 = r1[i + 1]

                        if x == "*" :
                            ergebnis = float(z1) * float(z2)

                        elif x == "/" :
                            ergebnis = float(z1) / float(z2)

                        l = [*r1]

                        l[i - 1] = "löschen"
                        l[i + 1] = "löschen"
                        l[i] = "löschen"

                        for i2 in range(3) :
                            l.remove("löschen")

                        if ergebnis % 1 == 0 :
                            ergebnis = int(ergebnis)

                        l.insert(i - 1, str(ergebnis))

                        r1 = []
                        for x in l :
                            r1.append(x)

                        i -= 1
                    
                    i += 1 

                    #print(r1)

                i = 0 
                while i < len(r1) - 1 :
                    x = r1[i]
                    if x == "+" or x == "-" :
                        z1 = r1[i - 1]
                        z2 = r1[i + 1]

                        if x == "+" :
                            ergebnis = float(z1) + float(z2)

                        elif x == "-" :
                            ergebnis = float(z1) - float(z2)

                        l = [*r1]

                        l[i - 1] = "löschen"
                        l[i + 1] = "löschen"
                        l[i] = "löschen"

                        for i2 in range(3) :
                            l.remove("löschen")

                        if ergebnis % 1 == 0 :
                            ergebnis = int(ergebnis)

                        l.insert(i - 1, str(ergebnis))

                        r1 = []
                        for x in l :
                            r1.append(x)

                        i -= 1

                        #print(r1)

                    i += 1 

                neu = ""
                for x in r1 :
                    neu += x
                
                r1 = neu
                
                if r1 != None :
                    if float(r1) == float(r2) :
                        self.output_rechenweg.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">" + str(variable) + "=" + str(z) + "</span></p></body></html>"))

                        stop = True
                        break
                    elif float(r1) < float(r2) and z == 0 :
                        stop = False
                        for x in alt :
                            if x == "-" :
                                t = Testen(z, alt, r2, variable, stellen, False)
                                t.start()

                    elif float(r1) > float(r2) and status == "hoch" :
                        for x in alt :
                            if x == "-" :
                                t = Testen(z, alt, r2, variable, stellen, False)
                                t.start()

                        plus = minus
                        plus *= -1

                        status = "runter"

                        gewechselt = True
                        l = [*str(minus)]
                        
                        x = 1
                        for i in l :
                            if i == "." :
                                l.insert(x, "0")
                                break
                            x += 1 

                        neu = ""
                        for i in l :
                            neu += i

                        plus = float(plus)

                        minus = float(neu)

                        stellen += 1 

                        stop = False

                    elif float(r1) < float(r2) and gewechselt and status == "runter" :
                        plus *= -1
                        plus = minus

                        status = "hoch"

                        l = [*str(minus)]

                        x = 0
                        for i in l :
                            if i == "." :
                                l.insert(x, "0")
                                break
                            x += 1 

                        neu = ""
                        for i in l :
                            neu += i

                        plus = float(plus)

                        minus = float(neu)

                        stellen += 1 
                        
                        stop = False

                    else :
                        stop = False
                     
                z += plus 
                z = round(z, stellen)
                r1 = alt

                if stop :
                    break
        
        else :
            variablen = 0
            variablen_liste = []
            variable = ""
            status = "hoch"
            gewechselt = False
            plus = 1
            minus = 0.1
            stellen = 0

            for x in r1 :
                if x in buchstaben and not x in variablen_liste :
                    variablen_liste.append(x)
                    variablen += 1 

            if variablen == 1 :
                for x in r1 :
                    if x in buchstaben :
                        variable = x
                        break

            z = 0 
            while self.go :
                neu = []
                alt1 = r1
                for x in r1 :
                    if x != variable :
                        neu.append(x)
                    else :
                        neu.append(str(z))

                r1 = neu

                neu = []
                alt2 = r2
                for x in r2 :
                    if x != variable :
                        neu.append(x)
                    else :
                        neu.append(str(z))

                r2 = neu
                i = 0 
                while i < len(r2) - 1 :
                    x = r2[i]
                    if x == "^" :
                        z1 = r2[i - 1]
                        z2 = r2[i + 1]
                        
                        ergebnis = float(z1) ** float(z2)

                        l = [*r2]

                        l[i - 1] = "löschen"
                        l[i + 1] = "löschen"
                        l[i] = "löschen"

                        for i2 in range(3) :
                            l.remove("löschen")

                        if ergebnis % 1 == 0 :
                            ergebnis = int(ergebnis)

                        l.insert(i - 1, str(ergebnis))

                        r2 = ""
                        for x in l :
                            r2 += x

                        i -= 1

                    i += 1 
                
                i = 0 
                while i < len(r2) - 1 :
                    x = r2[i]
                    if x == "*" or x == "/" :
                        z1 = r2[i - 1]
                        z2 = r2[i + 1]

                        if x == "*" :
                            ergebnis = float(z1) * float(z2)

                        elif x == "/" :
                            ergebnis = float(z1) / float(z2)

                        l = [*r2]

                        l[i - 1] = "löschen"
                        l[i + 1] = "löschen"
                        l[i] = "löschen"

                        for i2 in range(3) :
                            l.remove("löschen")

                        if ergebnis % 1 == 0 :
                            ergebnis = int(ergebnis)

                        l.insert(i - 1, str(ergebnis))

                        r2 = ""
                        for x in l :
                            r2 += x

                        i -= 1

                    i += 1 

                i = 0
                while i < len(r2) - 1 :
                    x = r2[i]
                    if x == "+" or x == "-" :
                        z1 = r2[i - 1]
                        z2 = r2[i + 1]

                        if x == "+" :
                            ergebnis = float(z1) + float(z2)

                        elif x == "-" :
                            ergebnis = float(z1) - float(z2)

                        l = [*r2]

                        l[i - 1] = "löschen"
                        l[i + 1] = "löschen"
                        l[i] = "löschen"

                        for i2 in range(3) :
                            l.remove("löschen")

                        if ergebnis % 1 == 0 :
                            ergebnis = int(ergebnis)

                        l.insert(i - 1, str(ergebnis))

                        r2 = ""
                        for x in l :
                            r2 += x

                        i -= 1
                    
                    i += 1

                if variablen == 1 :
                    for x in r1 :
                        if x in buchstaben :
                            variable = x
                            break

                    i = 0 
                    while i < len(r1) - 1 :
                        x = r1[i]
                        if x == "^" :
                            z1 = r1[i - 1]
                            z2 = r1[i + 1]
                            
                            ergebnis = float(z1) ** float(z2)

                            l = [*r1]

                            l[i - 1] = "löschen"
                            l[i + 1] = "löschen"
                            l[i] = "löschen"

                            for i2 in range(3) :
                                l.remove("löschen")

                            if ergebnis % 1 == 0 :
                                ergebnis = int(ergebnis)

                            l.insert(i - 1, str(ergebnis))

                            r1 = []
                            for x in l :
                                r1.append(x)

                            i -= 1
                        
                        i += 1 
                    
                    i = 0 
                    while i < len(r1) - 1 :
                        x = r1[i]
                        if x == "*" or x == "/" :
                            z1 = r1[i - 1]
                            z2 = r1[i + 1]

                            if x == "*" :
                                ergebnis = float(z1) * float(z2)

                            elif x == "/" :
                                ergebnis = float(z1) / float(z2)

                            l = [*r1]

                            l[i - 1] = "löschen"
                            l[i + 1] = "löschen"
                            l[i] = "löschen"

                            for i2 in range(3) :
                                l.remove("löschen")

                            if ergebnis % 1 == 0 :
                                ergebnis = int(ergebnis)

                            l.insert(i - 1, str(ergebnis))

                            r1 = []
                            for x in l :
                                r1.append(x)

                            i -= 1
                        
                        i += 1 

                    i = 0 
                    while i < len(r1) - 1 :
                        x = r1[i]
                        if x == "+" or x == "-" :
                            z1 = r1[i - 1]
                            z2 = r1[i + 1]

                            if x == "+" :
                                ergebnis = float(z1) + float(z2)

                            elif x == "-" :
                                ergebnis = float(z1) - float(z2)

                            l = [*r1]

                            l[i - 1] = "löschen"
                            l[i + 1] = "löschen"
                            l[i] = "löschen"

                            for i2 in range(3) :
                                l.remove("löschen")

                            if ergebnis % 1 == 0 :
                                ergebnis = int(ergebnis)

                            l.insert(i - 1, str(ergebnis))

                            r1 = []
                            for x in l :
                                r1.append(x)

                            i -= 1

                        i += 1 

                    neu = ""
                    for x in r1 :
                        neu += x
                    
                    r1 = neu
                    
                    if r1 != None :
                        if float(r1) == float(r2) :
                            self.output_rechenweg.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">" + str(variable) + "=" + str(z) + "</span></p></body></html>"))

                            stop = True
                            break
                        elif float(r1) < float(r2) and z == 0 :
                            stop = False
                            for x in alt1 :
                                if x == "-" :
                                    t = Testen(z, alt1, r2, variable, stellen, False)
                                    t.start()

                        elif float(r1) > float(r2) and status == "hoch" :
                            for x in alt1 :
                                if x == "-" :
                                    t = Testen(z, alt1, r2, variable, stellen, False)
                                    t.start()

                            plus = minus
                            plus *= -1

                            status = "runter"

                            gewechselt = True
                            l = [*str(minus)]
                            
                            x = 1
                            for i in l :
                                if i == "." :
                                    l.insert(x, "0")
                                    break
                                x += 1 

                            neu = ""
                            for i in l :
                                neu += i

                            plus = float(plus)

                            minus = float(neu)

                            stellen += 1 

                            stop = False

                        elif float(r1) < float(r2) and gewechselt and status == "runter" :
                            plus *= -1
                            plus = minus

                            status = "hoch"

                            l = [*str(minus)]

                            x = 0
                            for i in l :
                                if i == "." :
                                    l.insert(x, "0")
                                    break
                                x += 1 

                            neu = ""
                            for i in l :
                                neu += i

                            plus = float(plus)

                            minus = float(neu)

                            stellen += 1 
                            
                            stop = False

                        else :
                            stop = False
                        
                    z += plus 
                    z = round(z, stellen)
                    r1 = alt1
                    r2 = alt2

                    if stop :
                        break


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())