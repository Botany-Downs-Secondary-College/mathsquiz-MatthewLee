#Matthew Lee
#GUI Math Quiz Test v2.2 - 07/03/2021

#IMPORTS
import random
from tkinter import *
from tkinter import Tk


#FUNCTIONS
class Math():
    def __init__(self, parent):
        self.name = ""
        self.age = 0
        self.result = 0
        
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
        self.LabelDiff = Label(self.Welcome, text = "Select difficulty", 
                               fg = "black", padx = 5, pady = 5,
                               font = ("comic sans ms", "10", "bold italic"))
        self.LabelDiff.grid(row = 4, column = 0)
        #setup
        self.difficulty_list = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []
        #Radio button creation
        for i in range(len(self.difficulty_list)):
            rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i,
                             text = self.difficulty_list[i], anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row = i+5, column = 0, sticky = W)
        
        #Button to quiz
        self.Toquiz = Button(self.Welcome, text = "Next", 
                             activebackground = "yellow",
                             command = lambda:[self.UserDetails(), self.QuestionGen()])
        self.Toquiz.grid(row = 8, column = 0)
        
        
        """Quiz"""
        #set score
        global score
        global count
        
        score = 0
        count = 0
        
        self.Quiz = Frame(parent)
        #Title Banner
        self.TitleQuiz = Label(self.Quiz, text = "Question 1 \nScore: 0/5", 
                                bg = "light blue", fg = "white", width = 20, padx = 30, 
                                pady = 10, font = ("comic sans ms", "14", "bold italic"))
        self.TitleQuiz.grid(row = 0, columnspan = 2)
        
        #Question
        self.Question = Label(self.Quiz, padx = 5, pady = 5, font = ("comic sans ms", "10"))
        self.Question.grid(row = 1, column = 0)
        
        #Answer box
        self.AnswerBox = Entry(self.Quiz)
        self.AnswerBox.grid(row = 1, column = 1)
        
        #Check Answer box
        self.ButtonCheck = Button(self.Quiz, text = "Check Answer",
                            activebackground = "yellow",
                            command = lambda:[self.Check()])
        self.ButtonCheck.grid(row = 2, column = 0)
        
        #Feedback
        self.feedback = Label(self.Quiz, padx = 5, pady = 5, font = ("comic sans ms", "10"))
        self.feedback.grid(row = 2, column = 1)
        
        
        
        """Score"""
        self.Score_page = Frame(parent)
        #Title
        self.TitleScore = Label(self.Score_page, text = "YOUR SCORE", 
                                bg = "light blue", fg = "white", width = 20, padx = 30, 
                                pady = 10, font = ("comic sans ms", "14", "bold italic"))
        self.TitleScore.grid(row = 0, columnspan = 4)
        
        #Report
        Report_info = ["Name", "Age", "Score"]
        self.report_labels = []
        
        for i in range(len(Report_info)):
            ColumnHeading = Label(self.Score_page, text = Report_info[i], 
                                  width = "7", height = "2", font = ("comic sans ms", "14", "bold"))
            self.report_labels.append(ColumnHeading)
            ColumnHeading.grid(row = 1, column = i)
        
        #User Details    
        self.name_display = Label(self.Score_page, textvariable = self.name)
        self.name_display.grid(row = 2, column = 0)
        
        self.age_display = Label(self.Score_page, text = "")
        self.age_display.grid(row = 2, column = 1)
        
        self.result_display = Label(self.Score_page, text = "")
        self.result_display.grid(row = 2, column = 2)
        
        #Home Button
        self.ButtonHome = Button(self.Score_page, text = "Home",
                            activebackground = "yellow", command = lambda:[self.ShowWelcome()])
        self.ButtonHome.grid(row = 3, column = 0)           
            
        
                
    """FUNCTIONS"""    
    def End(self):
        #Should run when count reaches 5
        self.Quiz.grid_remove()
        
        self.name_display.configure(text = self.name)
        self.age_display.configure(text = self.age)
        self.result_display.configure(text = self.result)
        
        #Open score page
        self.Score_page.grid()
    
    def ShowQuiz(self):
        #Removes Welcome and plays 
        self.Welcome.grid_remove()
        self.Quiz.grid()
        
    def ShowWelcome(self):
        #Clears user details for next user
        self.EnterName.delete(0, 'end')
        self.EnterAge.delete(0, 'end')
        #Removes Quiz and shows welcome
        self.Score_page.grid_remove()
        self.Welcome.grid()
    
    def UserDetails(self):
        #Check age
        if self.EnterName.get() == "":
            self.Return.configure(text = "Please enter \nyour name!")
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
        #config
        self.Question.configure(text = self.add)
        
    def Check(self):
        global score
        global count
        try:
            self.answer = self.AnswerBox.get()
            self.answer_mod = int(self.answer)
            #Clears
            self.AnswerBox.delete(0, 'end')
            if self.answer_mod == self.total:
                self.feedback.configure(text = "Correct!")
                #Adds
                score += 1
                count += 1
                self.TitleQuiz.configure(text = "Question {} \nScore: {}/5".format(count + 1, score))
                #Question count check
                if count == 5:
                    #Collect Info
                    self.name = self.EnterName.get()
                    self.age = str(self.EnterAge.get())
                    self.result = str(score)
                    #reset
                    score = 0
                    count = 0
                    self.End()  
                else:
                    self.QuestionGen()
            else:
                self.feedback.configure(text = "Incorrect!")
                count += 1
                self.TitleQuiz.configure(text = "Question {} \nScore: {}/5".format(count + 1, score))
                if count == 5:
                    self.End() 
                else:
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