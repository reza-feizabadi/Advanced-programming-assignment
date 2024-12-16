# تعریف کلاس فوتبالیست به عنوان والد
class Footbalist:

    # تعریف صفات مربوط به کلاس فوتبالیست
    def __init__(self, first_name, last_name, number, height, weight, age):
        
        self.first_name = first_name

        self.last_name = last_name

        self.number = number

        self.height = height

        self.weight = weight

        self.age = age 

    # تعریف تابع برای نمایش نام بازیکن
    def player_first_number(self):
        return('The player first name: '+ self.first_name)
    
     # تعریف تابع برای نمایش نام خانوادگی بازیکن
    def player_last_number(self):
        return('The playerlast name: '+ self.last_name)
    
     # تعریف تابع برای نمایش شماره بازیکن
    def player_number(self):
        return('the '+ str(self.first_name)+ ' ' + str(self.last_name) + ' number is ' +str(self.number))

     # تعریف تابع برای نمایش قد بازیکن
    def player_height(self):
        return('the '+ str(self.first_name)+ ' ' + str(self.last_name) + ' height is ' +str(self.height))
    
     # تعریف تابع برای نمایش وزن بازیکن
    def player_weight(self):
        return('the '+ str(self.first_name)+ ' ' + str(self.last_name) + ' weight is ' +str(self.weight) + 'kg')
    
     # تعریف تابع برای نمایش سن بازیکن
    def player_age(self):
        return('the '+ str(self.first_name)+ ' ' + str(self.last_name) + ' age is ' +str(self.age))
    
# تعریف کلاس دروازه‌بان به عنوان فرزند
class Goalkeeper(Footbalist):
    pass

# تعریف کلاس دفاع به عنوان فرزند
class Defenders(Footbalist):
    pass

# تعریف کلاس هافبک به عنوان فرزند
class Midfielders(Footbalist):
    pass

# تعریف کلاس محاجم به عنوان فرزند
class Forwards(Footbalist):
    pass

# تعریف اشیاء
player_1 = Footbalist('ali' , 'hasani' , 8 , 186 , 91, 21)

player_2 = Goalkeeper('Ahmad' , 'nameni' , 5 , 189 , 24)

player_3 = Forwards('Ashkan' , 'nazar zade' , 6 , 181 , 25)

player_4 = Forwards('Ehsan' , 'lavasani' , 9 , 184 , 27)

player_5 = Midfielders('Reza' , 'feizabadi' , 10 , 176 , 23)

player_6 = Midfielders('Mahmood' , 'taheri' , 2 , 180 , 25)

player_6 = Defenders('Ebrahim' , 'alipoor' , 1 , 177 , 26)


# چاپ صفت مورد نظر از شیء مورد نظر با فراخاوانی توابع
print(player_1.player_first_number())

print(player_1.player_last_number())

print(player_1.player_number())

print(player_1.player_height())

print(player_1.player_weight())

print(player_1.player_age())



