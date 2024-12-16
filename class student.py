# ایجاد کلاس برای دانشجو
class Student:

    # ایجاد صفات
    def __init__(self, first_name, last_name, age, gender, national_number, student_number,GPA ):
        
        self.first_name = first_name 

        self.last_name = last_name

        self.age = age 
 
        self.gender = gender

        self.national_number = national_number

        self.student_number =  student_number

        self.GPA = GPA
    
    
    # ایجاد تابع برای نمایش نام دانشجو
    def get_firsr_name(self):
        return ("The first name: "+ self.first_name)
    
    # ایجاد تابع برای نمایش نام خانوادگی دانشجو
    def get_last_name(self):
        return ("The last name: "+self.last_name) 
    
    # ایجاد تابع برای نمایش سن دانشجو
    def get_age(self):
        return ("The "+self.first_name + 's age is ' + str(self.age))
    
    # ایجاد تابع برای نمایش  جنسیت دانشجو
    def get_gender(self):
        return ("The "+self.first_name + 's gender is ' + str(self.gender))
    
    # ایجاد تابع برای نمایش شماره ملی دانشجو
    def get_national_number(self):
        return ("The "+self.first_name + 's national number is ' + str(self.national_number))

    # ایجاد تابع برای نمایش شماره ملی دانشجو
    def get_student_number(self):
        return ("The "+self.first_name + 's student number is ' + str(self.student_number))
    
    # ایجاد تابع برای نمایش معدل دانشجو
    def get_GPA(self):
        return ("The "+self.first_name + 's GPA is ' + str(self.GPA))
    
# ایجاد اشیاء
student_1 = Student('Ali', 'Amini', 24 , 'Men' , 99211140162022 , 2124003452 , 16.77)

student_2 = Student('Ali', 'Hasani', 21 , 'Men' , 99212240062012 , 2024133458 ,18.50)

student_3 = Student('Zahra', 'Rahimi', 23 , 'Women' , 92141140133002 ,'0025086123' , 19.08)

student_4 = Student('Hossein', 'Zare', 25 , 'Men' , '02121040809016' , '0023143567' , 14.33)

student_5 = Student('Raha', 'Karimi', 18 , 'women' , '02221040507011' , 2104583052 , 17.90)

student_6 = Student('Mahdi', 'Sedaghat', 22 , 'Men' , 9341040102022 , 3412410345 , 13.66)

student_7 = Student('Amir', 'Amiri', 23 , 'Men' , '02121150608011' , '0026024567' , 19.17)

# چاپ صفت مورد نظر از شیء مورد نظر با فراخاوانی توابع
print(student_2.get_age())
print(student_2.get_firsr_name())
print(student_2.get_last_name())
print(student_2.get_gender())
print(student_2.get_national_number())
print(student_2.get_student_number())



