#Matthew 12/02/2020

#Import
from tkinter import*
import random

#Class
class MathQuiz():
    def __init__(self, parent):
        #Variables
        self.score = 0
        self.name = ""
        self.question = ""       
        
        """Welcome Frame"""
        
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        
        #title
        self.TitleLabel = Label(self.Welcome, text = "Welcome to Mathquiz", 
                                bg = "black", fg = "white", width = 20, padx = 30, 
                                pady = 30, font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        
        #BOOTAN
        self.NextButton = Button(self.Welcome, text = "Next", command = self.show_Quiz)
        self.NextButton.grid(row = 8, column = 1)
        
        """Quiz Frame"""
        
        self.Quiz = Frame(parent)
        
        #Title
        self.TitleLabel = Label(self.Quiz, text = "QUIZ", 
                                bg = "black", fg = "white", width = 20, padx = 30, 
                                pady = 30, font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        
        #Question
        self.Question = Label(self.Quiz, fg = "black",font = ("Arial", "10"))
        self.Question.grid(row = 7, column = 0)
        self.Question.configure(text = "2 + 2 = ?")
        
        #Reply
        self.Reply = Label(self.Quiz, fg = "black", font = ("Arial", "10"))
        self.Reply.grid(row = 7, column = 1)
        
        self.Reply.configure(text = "")
        
        #Awnser Box
        self.AwnserBox = Entry(self.Quiz)
        self.AwnserBox.grid(row = 8, column = 0)
        
        #Next button
        self.NextButton = Button(self.Quiz, text = "Home", command = self.show_Welcome)
        self.NextButton.grid(row = 9, column = 1)
        
        #Check button
        self.CheckButton = Button(self.Quiz, text = "Check", command = self.Check)
        self.CheckButton.grid(row = 9, column = 0)
        
    def show_Welcome(self):
        self.Quiz.grid_remove()
        self.Welcome.grid()
        
    def show_Quiz(self):
        self.Welcome.grid_remove()
        self.Quiz.grid()
        
    def Check(self):
        self.awnser = self.AwnserBox.get()
        self.awnser = int(self.awnser)
        if self.awnser == 4:
            self.Reply.configure(text = "Correct!")
            self.score = 1
            print(self.score)
        else:
            self.Reply.configure(text = "Incorrect.")
            print(self.score)
        
    def QuestionGen(self):
        #list
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        #Picks numbers
        self.a = random.choice(num_list)
        self.b = random.choice(num_list)
        
        

#Mainroutine   
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()