from tkinter import *
import math

class MathGeometry() :
    def __init__(self):
        pass
    def sin(self,type, a):
        if type == "deg":
            return math.sin(math.radians(a))
        else:
            return math.sin(a)
    def cos(self,type, a): 
        if type == "deg":
            return math.cos(math.radians(a))
        else:
            return math.cos(a)
    def tan(self,type, a): 
        if type == "deg":
            return math.tan(math.radians(a))
        else:
            return math.tan(a)
    def cotan(self,type, a):
        if type == "deg":
            return 1/math.tan(math.radians(a))
        else:
            return 1/math.tan(a)
    def fact(self, a):
        return math.factorial(a)
    def pi (self):
        return str(math.pi)[0:-7]
    def e(self):
        return str(math.e)[0:-7]
mathgeometry = MathGeometry()
class Main(Frame):
    def __init__(self, root):
        self.deg_or_rad = "deg"
        super(Main, self).__init__(root)
        self.build()
        
    
    def validate(self,event):
        
        keys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "parenleft", "parenright",
                "asterisk", "slash", "minus", "plus", "period", "Shift_R", "Shift_L", "BackSpace", "Return"]
        buttons = ["Shift_R", "Shift_L", "BackSpace", "Return"]
        event.keysym.encode('utf8')
        if event.keysym in keys:
            if event.keysym in buttons:
                if event.keysym == "BackSpace":
                    l = len(self.formula) - len(self.entry.get())
                    self.formula = self.formula[0:-l]
                elif event.keysym == "Return":
                    return self.logic("=")
                else:
                    pass
                
            else:
                result = ""
                if event.keysym == "parenleft":
                    result = "("
                elif event.keysym == "parenright":
                    result = ")"
                elif event.keysym == "slash":
                    result = "/"
                elif event.keysym == "asterisk":
                    result = "*"
                elif event.keysym == "minus":
                    result = "-"
                elif event.keysym == "plus":
                    result = "+"
                elif event.keysym == "period":
                    result = "."
                else:          
                    result = event.keysym
                return self.logic(result)
        else:


            text = self.entry.get()
            new_text = text.replace(event.keysym,"")
            self.entry.delete(0, 'end')
            self.entry.insert(END, new_text)
    def build(self):
        x = 20
        y = 130
        self.formula = "0"
        self.entry = Entry(textvariable=self.formula, font=("Times New Roman", 21, "bold"), bg="#2d2d2d",bd = 1, foreground="#FFF")
        self.preload = Label(text="", font=("Times New Roman", 21, "bold"), bg="#2d2d2d", fg="#8e8e8e")
        self.preload.place(x=x, y=73)
        self.entry.insert(END,self.formula)
        self.entry.bind('<KeyRelease>', self.validate)
        self.entry.place(x=x, y=30, width = 480)
        #САм интерфейс
        interface = [
            "^", "C", "←", ".",  "+",
            "sin(", "7", "8", "9", "-",
            "cos(", "4", "5", "6", "/",
            "tg(", "1", "2", "3", "*",
            "ctg(", "(", "0", ")", "√(",
            "fact(", "π", "e", "deg", "=",
        ]

        
        #Распологаем кнопки по интерфейсу
        for bt in interface:
            
            def com(x=bt): return self.logic(x)
            color_button = "#1a1e2a"
            color_button_active = "#23262f"
            color_fg = "#fff"
            color_fg_active = "#bdbdbd"
            font_size = 18
            if (bt == "="):
                color_button = "#11c202"
                color_button_active = "#00a700"
                color_fg = "#000"
                color_fg_active = "#000"
                font_size = 40
            if bt == "+" or bt == "-" or bt == "/" or bt == "*" or bt == "^" or bt == "√(" or bt == "." or bt == "←" or bt == "C":
                color_fg =  "#f4a900"
                color_fg_active = "#d59300"
                font_size = 24
            if bt == "sin(" or bt == "cos(" or bt == "tg(" or bt == "ctg(" or bt == "fact(":
                color_fg = "#ff5e00"
                color_fg_active = "#dd5100"
            if bt == "π" or bt == "e" or bt == "deg":
                color_fg = "#ecdd00"
                color_fg_active = "#d7d300"
            if bt == "deg" or bt == "rad":
                button = Button(text=bt, fg=color_fg, activeforeground=color_fg_active, activebackground=color_button_active, bg=color_button, bd="0", font=("Times New Roman", font_size))
                button.place(x=x, y=y, width=80, height=64)
                button.bind('<Button-1>', self.logicRadOrDeg)
            else:
                Button(text=bt, fg=color_fg, activeforeground=color_fg_active, activebackground=color_button_active, bg=color_button, bd="0", font=("Times New Roman", font_size), command=com).place(
                    x=x, y=y, width=80, height=64)
            
            x += 100
            if x > 440:
                x = 20
                y += 80
    def logicRadOrDeg(self,event) :
        if event.widget.cget('text') == "deg":  
            self.deg_or_rad = "rad"
            event.widget.config(text="rad")
        elif event.widget.cget('text') == "rad":
            self.deg_or_rad = "deg"
            event.widget.config(text="deg")
        else :
            pass
        self.update()
    def logic(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "←":
            self.formula = self.formula[0:-1]
        elif operation == ".":
            self.formula = str(self.formula + "." )
        elif operation == "^":
            if self.formula == "0":
                self.formula = ""
            self.formula = str(self.formula + "**")
        elif operation == "=":
            self.formula = self.formula.replace('e', 'float(mathgeometry.e())')
            self.formula = self.formula.replace('π', 'float(mathgeometry.pi())')
            self.formula = self.formula.replace('sin(', 'mathgeometry.sin("' + self.deg_or_rad+'",')
            self.formula = self.formula.replace('cos(', 'mathgeometry.cos("' + self.deg_or_rad+'",')
            self.formula = self.formula.replace('tg(', 'mathgeometry.tan("' + self.deg_or_rad+'",')
            self.formula = self.formula.replace('ctg(', 'mathgeometry.cotan("'+ self.deg_or_rad+'",')
            self.formula = self.formula.replace('fact', 'mathgeometry.fact')
            self.formula = self.formula.replace('√', 'math.sqrt')
            try:
                self.formula = str(eval(self.formula))
            except:
                self.formula = 'Error'
            
            
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.preloadUpdate()
        self.entry.delete(0, 'end')
        self.entry.insert(END,self.formula)
    def preloadUpdate(self) :
            preload_text = self.formula
            preload_text = preload_text.replace('e', 'float(mathgeometry.e())')
            preload_text = preload_text.replace('π', 'float(mathgeometry.pi())')
            preload_text = preload_text.replace('sin(', 'mathgeometry.sin("' + self.deg_or_rad+'",')
            preload_text = preload_text.replace('cos(', 'mathgeometry.cos("' + self.deg_or_rad+'",')
            preload_text = preload_text.replace('tg(', 'mathgeometry.tan("' + self.deg_or_rad+'",')
            preload_text = preload_text.replace('ctg(', 'mathgeometry.cotan("' + self.deg_or_rad+'",')
            preload_text = preload_text.replace('fact', 'mathgeometry.fact')
            preload_text = preload_text.replace('√', 'math.sqrt')
            try:
                self.preload.config(text=str(eval(preload_text)))
            except:
                return

if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#2d2d2d"
    root.geometry("520x650+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
