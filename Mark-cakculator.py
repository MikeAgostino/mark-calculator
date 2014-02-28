# Mark Calculator V 1.1
# By Michael Agostino

class mainFunctions():
    
    def checkNumberResponse(response,error_message):
        valid_response = False
        while valid_response == False:
            try:
                if float(response) <= 100:
                    valid_response = True
                    return response
                else: 
                    response = input(error_message)      
            except:
                if valid_response == False:
                    response = input(error_message)       
                    
    def reMark():
        answer = input("\nWould you like to mark again? (Y/N): ")
        while(answer.lower() != "y" and answer.lower() != "n"):
            answer = input("\nPlease enter a valid answer (Y/N): ")
        if answer.lower() == "y":
            return True
        if answer.lower() == "n":
            return False
        
    def queryExamWeightAndGoal():
        goal_grade = input("\nPlease enter a goal grade in the course: ")
        goal_grade = mainFunctions.checkNumberResponse(goal_grade,"\nPlease enter a valid goal grade (1-100): ")
        exam_weight = input("\nPlease enter an exam weight: ")
        exam_weight = mainFunctions.checkNumberResponse(exam_weight,"\nPlease enter a valid exam weight (1-100) : ")
        return (goal_grade,exam_weight)
        
        
    def mainMarkInput(total_percent = 100):
        number = 1
        mark_list = []
        sum_percent = 0
        while sum_percent < total_percent:
            percent = input("\nPlease enter a weight for mark number "+ str(number) + ": ")
            newPercent = mainFunctions.checkNumberResponse(percent,"Please enter a valid weight for mark number "+ str(number) + " (1-100) : ")
            mark = input("\nPlease enter a grade for mark number "+ str(number) + ": ") 
            newMark = mainFunctions.checkNumberResponse(mark,"Please enter a valid grade for mark number "+ str(number) + " (1-100) : ")
            number +=1
            mark_list.append((newPercent,newMark))
            sum_percent += float(percent)
        return mark_list
        


class partialMark():
    goal_grade = 0
    exam_weight = 0
    
    def __init__(self,goal_grade,exam_weight):
        self.mark_list = []
        self.goal_grade = goal_grade
        self.exam_weight = exam_weight
        self.markInput()
        needed_grade = self.calculatePercentNeeded(self.markCalculator())
        if needed_grade <= 100:
            print("\nYou must attain a " + str(needed_grade) + "% on your exam to obtain a " + self.goal_grade + "% in the course.")
        else:
            print("\nGiven your grades, it is impossible to attain " + self.goal_grade + "% in this course.")
        
        
        
    def markInput(self):
        self.mark_list = mainFunctions.mainMarkInput(100-float(self.exam_weight))
        
    def markCalculator(self):
        mark_sum = 0
        total_course_weight = 100-float(self.exam_weight)
        
        for i in self.mark_list:
            percent = (float(i[0])/100)
            mark = float(i[1])
            new_mark = mark*percent
            mark_sum += new_mark
        return mark_sum
    
    def calculatePercentNeeded(self,mark_sum):
        altered_grade = float(self.goal_grade) - mark_sum
        needed_exam_grade = altered_grade/(float(self.exam_weight)/100)
        return needed_exam_grade
    

class fullMark():
  

    def __init__(self):
        self.mark_list = [] 
        self.markInput()
        print("\nYour Final Grade is " + str(self.markCalculator()) + "%")
    
    
    def markInput(self):
        self.mark_list = mainFunctions.mainMarkInput()
    
    def markCalculator(self):
        mark_sum = 0
        for i in self.mark_list:
            percent = float(i[0])/100
            mark = float(i[1])
            newMark = mark*percent
            mark_sum += newMark
            
        return mark_sum
            
        
if __name__ == "__main__":
    
    
    print("Welcome to Mike's Mark Calculator!\n")
    
    answer = input("If you do not have your exam grade please press 1, if you do press 2: ")
    while answer != '1' and answer != '2':
        answer = input("\nPlease enter a valid answer 1 or 2: ")
    if answer == "1":
        goal_grade_and_exam_weight = mainFunctions.queryExamWeightAndGoal()
        mark = partialMark(goal_grade_and_exam_weight[0],goal_grade_and_exam_weight[1])
        while(mainFunctions.reMark() == True):
            goal_grade_and_exam_weight = mainFunctions.queryExamWeightAndGoal()
            mark = partialMark(goal_grade_and_exam_weight[0],goal_grade_and_exam_weight[1])        

    if answer == "2":
        mark = fullMark()
        while(mainFunctions.reMark() == True):
            mark = fullMark()
