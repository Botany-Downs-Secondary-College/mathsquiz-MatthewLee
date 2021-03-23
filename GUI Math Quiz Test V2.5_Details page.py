#Matthew Lee
#GUI Math Quiz Test v2.2 - 07/03/2021

#IMPORTS
import tkinter as ttk
from random import *
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
                             command = lambda:[self.UserDetails()])
        self.Toquiz.grid(row = 8, column = 0)        
        self.Toquiz.bind("<Return>", lambda event: self.UserDetails())
        root.bind("<Return>", lambda event: self.UserDetails())  
        
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
        self.ButtonCheck.bind("<Return>", lambda event: self.Check())
        root.bind("<Return>", lambda event: self.Check())
        
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
        self.name_display = Label(self.Score_page, textvariable = self.name, font = ("comic sans ms", "11"))
        self.name_display.grid(row = 2, column = 0)
        
        self.age_display = Label(self.Score_page, text = "", font = ("comic sans ms", "11"))
        self.age_display.grid(row = 2, column = 1)
        
        self.result_display = Label(self.Score_page, text = "", font = ("comic sans ms", "11"))
        self.result_display.grid(row = 2, column = 2)
        
        #Home Button
        self.ButtonHome = Button(self.Score_page, text = "Home",
                            activebackground = "yellow", command = lambda:[self.ShowWelcome()])
        self.ButtonHome.grid(row = 3, column = 0)  
        
        #Details Button
        self.ButtonDetails = Button(self.Score_page, text = "All scores",
                                    activebackground = "yellow", command = lambda:[self.ShowDetail()])
        self.ButtonDetails.grid(row = 3, column = 1)
        
        
        """Details page"""
        self.Details_page = Frame(parent)
        #Title
        self.TitleScore = Label(self.Details_page, text = "ALL SCORES", 
                                bg = "light blue", fg = "white", width = 20, padx = 30, 
                                pady = 10, font = ("comic sans ms", "14", "bold italic"))
        self.TitleScore.grid(row = 0, columnspan = 4)
        #Display scores    
        Report_info = ["Name", "Age", "Score"]
        self.report_labels = []
        for i in range(len(Report_info)):
            ColumnHeading = Label(self.Details_page, text = Report_info[i], 
                                  width = "7", height = "2", font = ("comic sans ms", "14", "bold"))
            self.report_labels.append(ColumnHeading)
            ColumnHeading.grid(row = 1, column = i)         
            
        #Add new information to all scores page
        data = open("records.txt", "r")
        extracted_data = (data.readlines())
        data.close()
        self.all_details = []
        for line in range(len(extracted_data)):
            info = Label(self.Details_page, text = extracted_data[line], font = ("comic sans ms", "11"))
            self.all_details.append(info)
            info.grid(row = line+2, column = 1)             
        self.End()
                    
                
    """FUNCTIONS"""    
    def End(self):
        #Should run when count reaches 5
        self.Quiz.grid_remove()
        
        self.name_display.configure(text = self.name)
        self.age_display.configure(text = self.age)
        self.result_display.configure(text = self.result + "/5")
        
        #Open score page
        self.Score_page.grid()
        
    def ShowDetail(self):       
        #Removes scorepage/Homepage and shows all details
        self.Welcome.grid_remove()
        self.Score_page.grid_remove()
        self.Details_page.grid()
    
    def ShowQuiz(self):
        #Removes Welcome and plays 
        self.Welcome.grid_remove()
        self.Quiz.grid()
        
    def ShowWelcome(self):
        #Clears user details for next user
        self.EnterName.delete(0, 'end')
        self.EnterAge.delete(0, 'end')
        #Removes Quiz and shows welcome
        self.Details_page.grid_remove()
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
                    self.QuestionGen()
                    self.ShowQuiz()
            except ValueError:
                self.Return.configure(text = "Please enter your \nage in numbers")    
                return False
                
                
    def QuestionGen(self):
        #Generate questions
        #Picks numbers
        self.number_1 = randrange(10)
        self.number_2 = randrange(10)
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
                self.QuestionGen()
            else:
                self.feedback.configure(text = "Incorrect!")
                count += 1
                self.TitleQuiz.configure(text = "Question {} \nScore: {}/5".format(count + 1, score))
                self.QuestionGen()
        except ValueError:
            self.feedback.configure(text = "Please enter \na number")
        #Question count check
        if count == 5:
            #Collect Info
            self.name = self.EnterName.get()
            self.age = str(self.EnterAge.get())
            self.result = str(score)
            #Copy info to text file
            with open ('records.txt', 'a+') as data_file:
                data_file.write(self.name + ' ' + self.age + ' ' + self.result + ' ' + '\n')
            data_file.close()
            #reset
            score = 0
            count = 0

    def Restart(self):
        self.Score_page.grid_remove()
        restart = Math(root)
            
            
"""MAINLOOP"""        
#Begin code
if __name__ == "__main__":
    root = Tk()
    frames = Math(root)
    root.title("Math quiz")
    root.mainloop()    