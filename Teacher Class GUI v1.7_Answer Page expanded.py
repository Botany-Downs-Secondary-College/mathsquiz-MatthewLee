#Matthew 12/02/2020

#Import
from tkinter import*
import random

#Class
class MathQuiz():
    def __init__(self, parent):
        #Variables
        self.score = 0
        
        """Welcome Frame"""
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        
        #title
        self.TitleLabel = Label(self.Welcome, text = "Welcome to Mathquiz", 
                                bg = "blue", fg = "white", width = 20, padx = 30, 
                                pady = 30, font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        
        #Button
        self.NextButton = Button(self.Welcome, text = "Next", 
                                 command = lambda:[self.QuestionGen(), self.show_Quiz()])
        self.NextButton.grid(row = 8, column = 1)
        
        
        """Quiz Frame"""
        self.Quiz = Frame(parent)
        
        #Title
        self.TitleLabel = Label(self.Quiz, text = "QUIZ", 
                                bg = "blue", fg = "white", width = 20, padx = 30, 
                                pady = 30, font = ("Time", "14", "bold"))
        self.TitleLabel.grid(columnspan = 2)
        
        #Question
        self.Question = Label(self.Quiz, fg = "black",font = ("Arial", "10"))
        self.Question.grid(row = 7, column = 0)
        self.Question.configure(text = "")
        
        #Answer Box
        self.AnswerBox = Entry(self.Quiz)
        self.AnswerBox.grid(row = 8, column = 0)
        
        #Home button
        self.HomeButton = Button(self.Quiz, text = "Home", command = self.show_Welcome)
        self.HomeButton.grid(row = 9, column = 1)
        
        #Check button
        self.CheckButton = Button(self.Quiz, text = "Check", 
                                  command = lambda:[self.Check(), self.clear()])
        self.CheckButton.grid(row = 9, column = 0)
        
        
        """CORRECT page"""
        self.Correct = Frame(parent)
        #Title
        self.TitleLabel = Label(self.Correct, text = "CORRECT!",
                                bg = "green", fg = "white", width = 20, padx = 30, 
                                pady = 30, font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        
        #Back button
        self.BackButton = Button(self.Correct, text = "Next Question", 
                                 command = lambda:[self.QuestionGen(), self.show_Quiz()])
        self.BackButton.grid(row = 9, column = 0)       
        
        
        """INCORRECT page"""
        self.Incorrect = Frame(parent)
        #Title
        self.TitleLabel = Label(self.Incorrect, text = "INCORRECT!",
                                bg = "red", fg = "white", width = 20, padx = 30, 
                                pady = 30, font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        
        #Total
        self.AnswerLabel = Label(self.Incorrect, fg = "black", font = ("Arial", "10"))
        self.AnswerLabel.grid(row = 9, column = 1)
        
        #Back button
        self.BackButton = Button(self.Incorrect, text = "Next Question", 
                                 command = lambda:[self.QuestionGen(), self.show_Quiz()])
        self.BackButton.grid(row = 9, column = 0)         
        
        
        
    #Functions
    #Call welcome page
    def show_Welcome(self):
        self.Quiz.grid_remove()
        self.Welcome.grid()
    
    #Call quiz page
    def show_Quiz(self):
        self.Welcome.grid_remove()
        self.Correct.grid_remove()
        self.Incorrect.grid_remove()
        self.Quiz.grid()
    
    #Clear answer box after clicking 'check'
    def clear(self):
        self.AnswerBox.delete(0, 'end')
        
    #Check the answer
    def Check(self):
        print(self.total)
        self.answer = self.AnswerBox.get()
        self.answer_mod = int(self.answer)
        self.AnswerLabel.configure(text = self.total)
        if self.answer_mod == self.total:
            self.Quiz.grid_remove()
            self.Correct.grid()

        else:
            self.Quiz.grid_remove()
            self.Incorrect.grid()
    
    #Generate questions        
    def QuestionGen(self):
        #list
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        #Picks numbers
        self.number_1 = random.choice(num_list)
        self.number_2 = random.choice(num_list)
        self.total = self.number_1 + self.number_2
        self.add = self.number_1, "+", self.number_2
        
        self.Question.configure(text = self.add)
        
    
#Mainroutine   
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Basic addition quiz")
    root.mainloop()