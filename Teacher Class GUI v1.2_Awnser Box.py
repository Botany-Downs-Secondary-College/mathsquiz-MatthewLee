#Matthew 12/02/2020

#Import
from tkinter import*

#Class
class MathQuiz():
    def __init__(self, parent):
        
        """Welcome Frame"""
        
        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        
        self.TitleLabel = Label(self.Welcome, text = "Welcome to Mathquiz", 
                                bg = "black", fg = "white", width = 20, padx = 30, 
                                pady = 30, font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        
        self.NextButton = Button(self.Welcome, text = "Next", command = self.show_Quiz)
        self.NextButton.grid(row = 8, column = 1)
        
        """Quiz Frame"""
        
        self.Quiz = Frame(parent)
        
        self.TitleLabel = Label(self.Quiz, text = "QUIZ", 
                                bg = "black", fg = "white", width = 20, padx = 30, 
                                pady = 30, font = ("Time", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        
        #Question
        self.Question = Label(self.Quiz, text = "I am a question", fg = "black",
                             font = ("Arial", "10"))
        self.Question.grid(row = 7, column = 0)
        
        #Awnser Box
        self.AwnserBox = Entry(self.Quiz)
        self.AwnserBox.grid(row = 8, column = 0)
        
        #Next button
        self.NextButton = Button(self.Quiz, text = "Home", command = self.show_Welcome)
        self.NextButton.grid(row = 8, column = 1)    
        
    def show_Welcome(self):
        self.Quiz.grid_remove()
        self.Welcome.grid()
        
    def show_Quiz(self):
        self.Welcome.grid_remove()
        self.Quiz.grid()


#Mainroutine   
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()