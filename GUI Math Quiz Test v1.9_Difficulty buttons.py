#Matthew Lee
#GUI Math Quiz Test v1.8 - 23/02/2021

#IMPORTS
import random
from tkinter import *
from tkinter import Tk


#FUNCTIONS
class Math():
    def __init__(self, parent):
        
        """Welcome"""
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        
        #title
        self.TitleLabel = Label(self.Welcome, text = "Welcome", 
                                bg = "light blue", fg = "white", width = 20, padx = 30, 
                                pady = 10, font = ("comic sans ms", "14", "bold italic"))
        self.TitleLabel.grid(row = 0, columnspan = 2)
        
        #Enter name - Label and Enter
        self.LabelName = Label(self.Welcome, text = "Enter Name: ", 
                               fg = "black", padx = 5, pady = 5, 
                               font = ("comic sans ms", "10", "bold italic"))
        self.LabelName.grid(row = 1, column = 0)
        
        self.EnterName = Entry(self.Welcome)
        self.EnterName.grid(row = 1, column = 1)
        
        #Enter age - Label and Enter
        self.LabelAge = Label(self.Welcome, text = "Enter Age: ", 
                               fg = "black", padx = 5, pady = 5,
                               font = ("comic sans ms", "10", "bold italic"))
        self.LabelAge.grid(row = 2, column = 0)
        
        self.EnterAge = Entry(self.Welcome)
        self.EnterAge.grid(row = 2, column = 1)
        
        #Return
        self.Return = Label(self.Welcome, fg = "red",
                            font = ("comic sans ms", "10", "italic"))
        self.Return.grid(row = 3, column = 1)
        self.Return.configure(text = "")     
        
        #Difficulty Buttons
        self.EasyButton = Radiobutton(self.Welcome)
        self.EasyButton.grid(row = 4, column = 0)
        
        self.MedButton = Radiobutton(self.Welcome)
        self.MedButton.grid(row = 5, column = 0)
        
        self.HardButton = Radiobutton(self.Welcome)
        self.HardButton.grid(row = 6, column = 0)
        
        
        #Difficulty Labels
        self.EasyLabel = Label(self.Welcome, text = "Easy", font = ("comic sans ms", "10"))
        self.EasyLabel.grid(row = 4, column = 1)
        
        self.MedLabel = Label(self.Welcome, text = "Medium", font = ("comic sans ms", "10"))
        self.MedLabel.grid(row = 5, column = 1)
        
        self.HardLabel = Label(self.Welcome, text = "Hard", font = ("comic sans ms", "10"))
        self.HardLabel.grid(row = 6, column = 1)
        
        
        #Bootun
        self.Toquiz = Button(self.Welcome, text = "Next", 
                             activebackground = "yellow",
                             command = lambda:[self.UserDetails(), self.QuestionGen()])
        self.Toquiz.grid(row = 7, column = 0)
        
        
        
        
        """Quiz"""
        self.Quiz = Frame(parent)
        #Title Banner
        self.TitleLabel = Label(self.Quiz, text = "QUIZ", 
                                bg = "light blue", fg = "white", width = 20, padx = 30, 
                                pady = 10, font = ("comic sans ms", "14", "bold italic"))
        self.TitleLabel.grid(row = 0, columnspan = 2)
        
        #Question
        self.Question = Label(self.Quiz, padx = 5, pady = 5, font = ("comic sans ms", "10"))
        self.Question.grid(row = 1, column = 0)
        
        #Answer box
        self.AnswerBox = Entry(self.Quiz)
        self.AnswerBox.grid(row = 1, column = 1)
        
        #Check Answer box
        self.ButtonCheck = Button(self.Quiz, text = "Check question",
                            activebackground = "yellow",
                            command = lambda:[self.Check()])
        self.ButtonCheck.grid(row = 2, column = 0)
        
        #Feedback
        self.feedback = Label(self.Quiz, padx = 5, pady = 5, font = ("comic sans ms", "10"))
        self.feedback.grid(row = 2, column = 1)
            
        
        
    """FUNCTIONS"""    
    
    def ShowQuiz(self):
        #Removes Welcome and plays 
        self.Welcome.grid_remove()
        self.Quiz.grid()
        
    def ShowWelcome(self):
        #Removes Quiz and shows welcome
        self.Quiz.grid_remove()
        self.Welcome.grid
    
    def UserDetails(self):
        #Check age
        if self.EnterName.get() == "":
            self.Return.configure(text = "Please enter your name!")
        
        else:
            try:
                if int(self.EnterAge.get()) <= 5:
                    self.Return.configure(text = "You're too young!")
                
                elif int(self.EnterAge.get()) >= 16:
                    self.Return.configure(text = "You're too old!")
                    
                else:
                    self.ShowQuiz()
            
            except ValueError:
                self.Return.configure(text = "Please enter your \nage in numbers")            
                
                
    def QuestionGen(self):
        #Generate questions
        
        #list
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        #Picks numbers
        self.number_1 = random.choice(num_list)
        self.number_2 = random.choice(num_list)
        self.total = self.number_1 + self.number_2
        self.add = self.number_1, "+", self.number_2, "="
        
        self.Question.configure(text = self.add)
        
    def Check(self):
        try:
            self.answer = self.AnswerBox.get()
            self.answer_mod = int(self.answer)
            
            #Clears
            self.AnswerBox.delete(0, 'end')
            
            if self.answer_mod == self.total:
                self.feedback.configure(text = "Correct!")
                self.QuestionGen()
    
            else:
                self.feedback.configure(text = "Incorrect!")
                self.QuestionGen()
        
        except ValueError:
            self.feedback.configure(text = "Please enter \na number")
        
"""MAINLOOP"""        
#Begin code
if __name__ == "__main__":
    root = Tk()
    frames = Math(root)
    root.title("Math quiz")
    root.mainloop()    