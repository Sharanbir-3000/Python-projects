import math
import os

class Math_class:
    def __init__(self):
        print("\n\n\n\t\t\t\t\tWelcome To Math Lab\n\n\n")
    
class Tempraturee:
    
    def __init__(self):
        super().__init__()
        print("\n\t\t\t\t\tTemperature Converter\n\n\n")

    def display_temp(self,sttr,degree):
        print(f"{sttr} = {degree}")

    def cel_to_farh(self):
        degree = int(input("Enter the Celsius Value : "))
        self.display_temp('Fahrenheit',(9/5)*degree + 32)

    def farh_to_cel(self):
        degree = int(input("Enter the Fahrenheit Value : "))
        self.display_temp('Celsius',(degree - 32) / 1.8)

    def kel_to_cel(self):
        degree = int(input("Enter the Kelvin Value : "))
        self.display_temp('Celsius',degree - 273.15)

    def kel_to_fahr(self):
        degree = int(input("Enter the Kelvin Value : "))
        self.display_temp('Fahrenheit',((9/5)*(degree - 273.15) + 32))

    def cel_to_kel(self): 
        degree = int(input("Enter the Celsius Value : "))
        self.display_temp('Kelvin',degree + 273.15)

    def fahr_to_kel(self): 
        degree = int(input("Enter the Fahrenheit Value : "))
        self.display_temp('Kelvin',((5/9)*(degree - 32) + 273.15))

    def temp_inp(self):
        print("\n\n\n\n1. Celsius To Fahrenheit\n2. Fahrenheit To Kelvin\n3. Fahrenheit To Celsius\n4. Kelvin To Fahrenheit\n5. Kelvin To Celsius\n6. Celsius To Kelvin")
        x = int(input("\n\nSelect From Above Options : "))
        os.system('cls')
        return x

    def inputt(self):
        x = self.temp_inp()
        if (x == 1):
            self.cel_to_farh()

        elif (x == 2):
            self.fahr_to_kel()
        
        elif (x == 3):
            self.farh_to_cel()

        elif (x == 4):
            self.kel_to_fahr()

        elif (x== 5):
            self.kel_to_cel()

        elif (x == 6):
            self.cel_to_kel()

        else:
            print("You enter invalid number !!!")
            self.inputt()

class S_I_unit_converter:
    def __init__(self):
        print("\n\n\n\n\t\t\t\t\tS_I_Unit Converter\n\n\n")

    def weight_inp(self):
        print("Ton (t) , Kilogram (kg) , Gram (g) , Pound (lb) , Ounce (oz) ")
        unt = input("S.I Unit : ")
        return unt

    def weight_conversion(self):
        unitt = self.weight_inp()
        x = int(input("Enter the Weight : "))
        os.system('cls')

        if (unitt == 'kg'):
            self.kilo = x
            self.gram = x * 1000
            self.ton = self.kilo / 1000  # t
            self.pound = 2.205 * self.kilo # lb
            self.ounce = 35.274 * x # oz
            
        elif(unitt == 'g'):
            self.gram = x
            self.kilo = x/1000
            self.ton = x/1000000 # t
            self.pound = x / 453.6 # lb
            self.ounce = x/28.35 # oz

        elif(unitt == 'oz'):
            self.ounce = x
            self.gram = x * 28.35
            self.kilo = x / 35.274 # oz
            self.ton = x / 35270 # t
            self.pound = x /16 # lb

        elif(unitt == 'lb'):
            self.pound = x
            self.kilo =  x / 2.205
            self.gram = x * 453.6
            self.ounce = x * 16 # oz
            self.ton = x / 2205 # t

        elif (unitt == 't'):
            self.ton = x
            self.kilo = x * 1000
            self.gram = x * 1000000
            self.ounce = x * 35270 # oz
            self.pound = x * 2205 # lb

        else :
            print("Invalid unit!!!\n\n")
            self.weight_conversion()

        print(f"Grams : {self.gram} g\nKilogram : {self.kilo} kg\nTonne : {self.ton} tonne\nPound : {self.pound} lb\nOunce : {self.ounce} oz")

    def dis_inp(self):
        print("Centimetre (cm) , Metre (m) , Kilometre (km) , Miles (mi) , Feet (ft) , Inches (in) , Yards (yd)")
        uni = input("Enter the unit : ")
        return uni

    def Distance_conversion(self):
        unitt = self.dis_inp()
        x = int(input("Enter the Distance : "))
        os.system('cls')

        if (unitt == "cm"):
            self.cm = x
            self.m = x / 100
            self.km = x / 100000
            self.mi = x / 160900
            self.feet = x / 30.48
            self.inch = x / 2.54
            self.yard = x / 91.44
        
        elif (unitt == "m"):
            self.m = x
            self.cm = x * 100
            self.km = x / 1000
            self.mi = x / 1609
            self.feet = x * 3.281
            self.inch = x * 39.37
            self.yard = x * 1.094

        elif (unitt == "km"):
            self.km = x
            self.m = x * 1000
            self.cm = x * 100000
            self.mi = x / 1.609
            self.feet = x * 3281
            self.inch = x * 39370
            self.yard = x * 1094


        elif (unitt == "mi"):
            self.km = x * 1.609
            self.m = x * 1609
            self.cm = x * 160900
            self.mi = x 
            self.feet = x * 5280
            self.inch = x * 63360
            self.yard = x * 1760

        elif (unitt == "ft"):
            self.km = x / 3281
            self.m = x / 3.281
            self.cm = x * 30.48
            self.mi = x / 5280
            self.feet = x 
            self.inch = x * 12
            self.yard = x / 3

        elif (unitt == "in"):
            self.km = x / 39370
            self.m = x / 39.37
            self.cm = x * 2.54
            self.mi = x / 63360
            self.feet = x / 12
            self.inch = x 
            self.yard = x / 36

        elif (unitt == "yd"):
            self.km = x / 1094
            self.m = x / 1.094
            self.cm = x * 91.44
            self.mi = x / 1760
            self.feet = x * 3
            self.inch = x * 36
            self.yard = x 

        else :
            print("Invalid unit!!!\n\n")
            self.Distance_conversion()

        print(f"Centimetre : {self.cm} cm\nMetre : {self.m}  m\nKilometre : {self.km} km\nMile : {self.mi} mi\nYard : {self.yard} yd\nFoot : {self.feet} ft\nInches : {self.inch} in")
   
    def time_inp(self):
        print("Seconds (sec) , Hours (hr) , Mintues (min) , Days (d) , Months (mon) , Weeks (w) , Years (yr)")
        unittt = input("\nEnter the unit : ")
        return unittt

    def Time_conversion(self):
        unitt = self.time_inp()
        x = int(input("Enter the Time : "))
        os.system('cls')

        if (unitt == "sec"):
            self.sec = x
            self.hr = x / 3600
            self.min = x / 60
            self.day = x / 86400
            self.mon = x / 2.628e+6
            self.week = x / 604800
            self.year = x / 3.154e+7
        
        elif (unitt == "hr"):
            self.sec = x * 3600
            self.hr = x 
            self.min = x * 60
            self.day = x / 24
            self.mon = x / 730
            self.week = x / 168
            self.year = x / 8760

        elif (unitt == "min"):
            self.sec = x * 60
            self.hr = x / 60
            self.min = x 
            self.day = x / 1440
            self.mon = x / 43800
            self.week = x / 10080
            self.year = x / 525600

        elif (unitt == "d"):
            self.sec = x * 86400
            self.hr = x * 24
            self.min = x * 1440
            self.day = x 
            self.mon = x / 30.417
            self.week = x / 7
            self.year = x / 365

        elif (unitt == "w"):
            self.sec = x * 604800
            self.hr = x * 168
            self.min = x * 10080
            self.day = x * 7
            self.mon = x / 4.345
            self.week = x 
            self.year = x / 52.143

        elif (unitt == "mon"):
            self.sec = x * 2.628e+6
            self.hr = x * 730
            self.min = x * 43800
            self.day = x * 30.417
            self.mon = x 
            self.week = x * 4.345
            self.year = x / 12

        elif (unitt == "yr"):
            self.sec = x * 3.154e+7
            self.hr = x * 8760
            self.min = x * 525600
            self.day = x * 365
            self.mon = x * 12
            self.week = x * 52.143
            self.year = x 

        else :
            print("Invalid unit!!!\n\n")
            self.Time_conversion()

        print(f"Second : {self.sec} sec\nMintue : {self.min} min\nHour : {self.hr} hr\nWeek : {self.week} weeks\nMonth : {self.mon} months\nYear : {self.year} yr")

    def inp(self):
        print("1. Weight Converter\n2. Distance Conversion\n3. Time Conversion")
        pres = int(input("\n\nSelect From Above Options : "))
        os.system('cls')
        return pres

    def menus(self):
        press = self.inp()
        if(press == 1):
            self.weight_conversion()

        elif(press == 2):
            self.Distance_conversion()

        elif(press == 3):
            self.Time_conversion()

        else:
            print("Invalid Option!!!")
            self.menus()

class Calculation:
    def __init__(self):
        print("\n\n\n\t\t\t\t\tMath Calculation\n\n\n")
    
    def sel_inp(self):
        k = int(input("1. Arthmetic \n2. Scientific \n\n\nChoose Any One : "))
        return k

    def selection(self):
        f = self.sel_inp()
        os.system('cls')
        if(f == 1):
            self.Arthmetic()

        elif(f == 2):
            self.scientific()

        else:
            print("Invalid Choice !!!")
            self.selection()

    def print_mth(self,strr,ans):
        print(f"{strr} = {ans}")

    def arth_inp(self):
        print("Select one of these operator (+ , - , * , /) : ",end="")
        s = input() 
        return s

    def Arthmetic(self):
        x = int(input("Enter the first number : "))
        s = self.arth_inp()
        y = int(input("Enter the second number : "))
        os.system('cls')
        
        if (s == '+'):
            self.anss = x + y
            self.print_mth("SUM",self.anss)

        elif (s == '*'):
            self.anss = x * y
            self.print_mth("PRODUCT",self.anss)

        elif (s == '/'):
            self.anss = x / y
            self.print_mth("QUOTIENT",self.anss)

        elif (s == '-'):
            self.anss = x - y
            self.print_mth("SUBTRACTION",self.anss)

        else : 
            print("Invalid Operator !!!!")
            self.Arthmetic()

    def sci_inp(self):
        print("\n\n\n\n1. Reminder\n2. Trignometric Value\n3. Logarithm\n4. Power And Squares")
        x = int(input("\n\nEnter the operation you want to perform : "))
        return x

    def tri_inp(self):
        print("Sin , Cos , tan , Sec , Cot , Cosec")
        fun = input("\nEnter any function from above : ")
        t = int(input("\nEnter the Angle for trignometric value : "))
            
        os.system('cls')

        if(fun == "sin"):
            self.anss = math.sin(t)
            self.print_mth(f"SIN({t})",self.anss)

        elif(fun == "cos"):
            self.anss = math.cos(t)
            self.print_mth(f"COS({t})",self.anss)

        elif(fun == "tan"):
            self.anss = math.tan(t)
            self.print_mth(f"TAN({t})",self.anss)

        elif(fun == "cot"):
            self.tempp = math.tan(t)
            self.anss = 1 / self.tempp
            self.print_mth(f"COT({t})",self.anss)

        elif (fun == "sec"):
            self.tempp = math.cos(t)
            self.anss = 1 / self.tempp
            self.print_mth(f"SEC({t})",self.anss)

        elif (fun == "cosec"):
            self.tempp = math.sin(t)
            self.anss = 1 / self.tempp
            self.print_mth(f"COSEC({t})",self.anss)

        else:
            print("Invalid function!!!")
            self.tri_inp()

    def log_inp(self):
        print("\n\n\n\n1. Custom Base\n2. Base-2\n3. Base-10\n4. Natural Logarithm")
        b = int(input("\n\nSelect from above options : "))
        l = int(input("\nEnter the number for its logarithm : "))
        os.system('cls')
        if(b == 1):
            base = int(input("Enter Base : "))
            self.anss = math.log(l,base)
            self.print_mth(f"log({l},{base})",self.anss)

        elif(b == 2):
            self.anss = math.log2(l)
            self.print_mth(f"log2({l})",self.anss)

        elif(b == 3):
            self.anss = math.log10(l)
            self.print_mth(f"log10({l})",self.anss)

        elif(b == 4):
            self.anss = math.log1p(l)
            self.print_mth(f"loge({l})",self.anss)
            
        else:
            print("Invalid option !!!")
            self.log_inp()

    def pow_inp(self):
        print("\n\n\n\n1. Power\n2. Square\n3. Cube\n4. Square Root\n5. Cube Root")
        k = int(input("\n\nSelect from above option : "))
        n = int(input("\nEnter the number : "))
        if(k == 1):
            m = int(input(f"Enter a number for power of {n} : "))
            self.anss = (n**m)
            self.print_mth(f"Power({n},{m})",self.anss)

        elif(k == 2):
            self.anss = n* n
            self.print_mth(f"Square({n})",self.anss)

        elif(k == 3):
            self.anss = n* n * n
            self.print_mth(f"Cube({n})",self.anss)

        elif(k == 4):
            self.anss = math.sqrt(n)
            self.print_mth(f"Square Root({n})",self.anss)

        elif(k == 5):
            self.anss = math.cbrt(n)
            self.print_mth(f"Cube Root({n})",self.anss)

        else:
            print("Invalid Option!!!")
            self.pow_inp()

    def scientific(self):
        x = self.sci_inp()
        
        if(x == 1):
            a = int(input("Enter the number for divided : "))
            b = int(input("Enter the number for divisor : "))
            os.system('cls')
            self.anss = a % b
            self.print_mth("Remainder",self.anss)

        elif (x == 2):
            self.tri_inp()
        
        elif(x == 3):
            self.log_inp()

        elif(x == 4):
            self.pow_inp()

        else:
            print("Invalid Option!!!")
            self.scientific()

class menu(Math_class, Tempraturee,S_I_unit_converter,Calculation):
    def __init__(self):
        super().__init__()
        self.prees = input("\n\n\n\n\n\n\n\t\t\t\tEnter Any Key...........")
        os.system('cls')

    def innpuut(self):
        print("\n\n\n\n\n\n1. Temperature Conversion\n2. S_I Unit Conversion\n3. Math operations")
        x = int(input("\n\nEnter From Options : "))
        os.system('cls')
        return x

    def mennu(self):
        k = self.innpuut()
        if(k == 1):
            tem = Tempraturee()
            tem.inputt()

        elif(k == 2):
            s_i = S_I_unit_converter()
            s_i.menus()

        elif(k == 3):
            cal = Calculation()
            cal.selection()
        else:
            print("Invalid Option !!!!")
            self.mennu()

if __name__ == "__main__":
    menuuu = menu()
    loop = 1
    while(loop == 1):
        menuuu.mennu()
        loop = int(input("\n\n\nPress 1, If you want to Do it again : "))
        os.system('cls')