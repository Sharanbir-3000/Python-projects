from functools import reduce
from collections import Counter
import os

def msg():
    print("\n\n\n\t\t\t\tWelcome to math class \n\n\n")
    print("\n\t\t\t\t      STATISTICS\n")

def mean(x):
    n = x.__len__()
    summ = reduce(lambda a,b:a+b,x)
    ans = summ/n
    print('Mean   : %.2f'%ans)

def mode(x):
    l_len = x.__len__()
    sett = set(x)
    s_len = sett.__len__()
    if l_len == s_len:
        print("Mode   : Not exist!!!")

    else:
        modde = dict(Counter(x))
        ans = max(zip(modde.values(),modde.keys()))[1]
        print(f"Mode   : {ans}")

def median(x):
    x.sort()
    l_len = x.__len__() 
    if l_len % 2 == 0:
        i = (l_len)//2
        print(f"Median : {x[i-1]} and {x[i]}")

    else:
        i = (l_len)//2
        print(f"Median : {x[i]}")

def direct_meann(dt):
    freq = []
    f_x = []
    print("CLASS INTERVAL | FREQUENCY(Fi) | CLASS MARK(Xi) |   FiXi   ")
    print("---------------|---------------|----------------|----------")
    for i in sorted(dt.keys()):
        print("{:>9}".format(i),end='')
        print('{:>7}'.format('|'),end='')
        print("{:>8}".format(dt[i]),end='')
        print('{:>8}'.format('|'),end='')
        x_y = i.split('-')
        int_list = list(map(int,x_y))
        x_i = (int_list[0] + int_list[1]) / 2
        print("{:>9}".format(x_i),end='')
        print('{:>8}'.format('|'),end='')
        Fi_Xi = dt[i] * x_i
        freq.append(dt[i])
        f_x.append(Fi_Xi)
        print("{:>8}".format(Fi_Xi))
        
    sum_freq = reduce(lambda a,b:a+b,freq)
    sum_f_x = reduce(lambda a,b:a+b,f_x)
    ans = sum_f_x / sum_freq
    print("\n\n")
    print("\t\t Mean = \u03A3FiXi")
    print("\t\t        -----")
    print("\t\t         \u03A3Fi ")
    print("\n")
    print(f"\t\t\u03A3FiXi = {sum_f_x} , \u03A3Fi = {sum_freq}\n")
    print(f"\t\tMean = {sum_f_x}")
    print("\t\t        -----")
    print(f"\t\t         {sum_freq}")
    print(f"\n\t\tMean = {ans}")
    print("\n")

def assumed_mean(dt):
    a,j = 0,0
    list_x_i = []
    list_d_i = []
    f_d = []
    freq = []
    for i in sorted(dt.keys()):
        x_y = i.split('-')
        int_list = list(map(int,x_y))
        x_i = (int_list[0] + int_list[1]) / 2
        list_x_i.append(x_i)

    a_index = list_x_i.__len__() // 2 
    if list_x_i.__len__() % 2 == 0:
        a = list_x_i[a_index-1] 
    else:
        a = list_x_i[a_index]

    print("CLASS INTERVAL | FREQUENCY(Fi) | CLASS MARK(Xi) |  Di = Xi - a  |    FiDi    ")
    print("---------------|---------------|----------------|---------------|------------")
    for i in sorted(dt.keys()):
        print(f"{i:>10}",end='')
        print(f"{'|':>6}",end='')
        print(f"{dt[i]:>8}",end='')
        print(f"{'|':>8}",end='')
        print(f"{list_x_i[j]:>10}",end='')
        print(f"{'|':>7}",end='')
        d_i = list_x_i[j] - a
        print(f"{d_i:>10}",end='')
        print(f"{'|':>6}",end='')
        list_d_i.append(d_i)
        freq.append(dt[i])
        Fi_Di = dt[i] * list_d_i[j]
        j += 1
        f_d.append(Fi_Di)
        print(f"{Fi_Di:>8}")

    sum_freq = reduce(lambda a,b:a+b,freq)
    sum_f_d = reduce(lambda a,b:a+b,f_d)
    ans = a + (sum_f_d / sum_freq)
    print("\n\n")
    print("\t\t Mean = a + \u03A3FiDi")
    print("\t\t            -----")
    print("\t\t             \u03A3Fi ")
    print("\n")
    print(f"\t\ta = {a} , \u03A3FiDi = {sum_f_d} , \u03A3Fi = {sum_freq}\n")
    print(f"\t\tMean = {a} + {sum_f_d}")
    print("\t\t              -----")
    print(f"\t\t                {sum_freq}")
    print(f"\n\t\tMean = {ans}")
    print("\n")
    
def step_deviation(dt):
    a,j,h = 0,0,0
    list_x_i = []
    list_d_i = []
    list_u_i = []
    f_u = []
    freq = []
    for i in sorted(dt.keys()):
        x_y = i.split('-')
        int_list = list(map(int,x_y))
        x_i = (int_list[0] + int_list[1]) / 2
        h = int_list[1] - int_list[0]
        list_x_i.append(x_i)

    a_index = list_x_i.__len__() // 2 
    if list_x_i.__len__() % 2 == 0:
        a = list_x_i[a_index-1] 
    else:
        a = list_x_i[a_index]

    print("CLASS INTERVAL | FREQUENCY(Fi) | CLASS MARK(Xi) |  Di = Xi - a  | Ui = Di / h |   FiUi   ")
    print("---------------|---------------|----------------|---------------|-------------|----------")
    for i in sorted(dt.keys()):
        print(f"{i:>10}",end='')
        print(f"{'|':>6}",end='')
        print(f"{dt[i]:>8}",end='')
        print(f"{'|':>8}",end='')
        print(f"{list_x_i[j]:>10}",end='')
        print(f"{'|':>7}",end='')
        d_i = list_x_i[j] - a
        print(f"{d_i:>10}",end='')
        print(f"{'|':>6}",end='')
        u_i = d_i / h
        print(f"{u_i:>7}",end='')
        print(f"{'|':>7}",end='')
        list_u_i.append(u_i)
        Fi_Ui = u_i * dt[i]
        print(f"{Fi_Ui:>7}")
        j += 1
        f_u.append(Fi_Ui)
        freq.append(dt[i])

    sum_freq = reduce(lambda a,b:a+b,freq)
    sum_f_u = reduce(lambda a,b:a+b,f_u)
    ans = a + ((sum_f_u / sum_freq) * h)
    print("\n\n")
    print("\t\t Mean = a + \u03A3FiUi * h")
    print("\t\t            -----")
    print("\t\t             \u03A3Fi ")
    print("\n")
    print(f"\t\th = {h} , a = {a} , \u03A3FiUi = {sum_f_u} , \u03A3Fi = {sum_freq}\n")
    print(f"\t\tMean = {a} + {sum_f_u} * {h}")
    print("\t\t              -----")
    print(f"\t\t                {sum_freq}")
    print(f"\n\t\tMean = {ans}")
    print("\n")
        
def mean_menu(dt):
    print("1. Direct Mean \n2. Assumed Mean \n3. Step-Deviation Mean")
    x = int(input("Enter the mean method number : "))
    os.system('cls')
    if x == 1:
        direct_meann(dt)
    
    elif x == 2:
        assumed_mean(dt)

    elif x == 3:
        step_deviation(dt)

    else:
        print("You choose wrong option, Try again!!!!")
        print("\n")
        mean_menu(dt)

def modal_class(dt):
    modal = []
    int_list = []
    h,lowerr = 0,0
    for i in sorted(dt.keys()):
        modal.append(dt[i])

    f_1 = max(modal)              # f1
    indx = modal.index(f_1)
    f_0 = modal[indx - 1]          # f0
    f_2 = modal[indx + 1]          # f2
        
    print("|CLASS INTERVAL | FREQUENCY(Fi) |")
    print("|---------------|---------------|")
    for i in sorted(dt.keys()):
        print("|{:>9}".format(i),end='')
        print('{:>7}'.format('|'),end='')
        print("{:>8}".format(dt[i]),end='')
        print('{:>8}'.format('|'))
        if f_1 == dt[i]:
            x_y = i.split('-')
            int_list = list(map(int,x_y))
            lowerr = int_list[0]             # l 
            h = int_list[1] - int_list[0]     # h


    ans = lowerr + (((f_1 - f_0) / ((2 * f_1) - f_0 - f_2)) * h)
    print("\n\n")
    print("\t\t Mode = l    +   (F1 - F0)   *   h")
    print("\t\t                -----------")
    print("\t\t               ((2*F1)-F0-F2) ")
    print("\n")
    print(f"\t\tl = {lowerr} , h = {h} , F1 = {f_1} , F0 = {f_0} , F2 = {f_2}\n")
    print(f"\t\t Mode = {lowerr}    +  ({f_1} - {f_0})   *   {h}")
    print("\t\t                ----------")
    print(f"\t\t               ((2*{f_1})-{f_0}-{f_2}) ")
    print(f"\n\t\tMode = {ans}")
    print("\n")

def median_class(dt):
    n,lowerr , freq,h = 0,0,0,0
    c_f ,indx = 0,0
    c_f_list = []
    print("CLASS INTERVAL | FREQUENCY(Fi) | CUMULATIVE FREQUENCY (C.F)|")
    print("---------------|---------------|---------------------------|")
    for i in sorted(dt.keys()):
        print("{:>9}".format(i),end='')
        print('{:>7}'.format('|'),end='')
        print("{:>8}".format(dt[i]),end='')
        print('{:>8}'.format('|'),end='')
        n += dt[i]
        c_f_list.append(n)
        print("{:>14}".format(n),end='')
        print('{:>14}'.format('|')) 
        
    mediann = n / 2 # n/2
    for i in c_f_list:
        if i > mediann:
            indx = c_f_list.index(i)
            c_f = c_f_list[indx - 1] # c.f
            # print(c_f)
            break

    for i,j in enumerate(sorted(dt.keys())):  
        if i == indx:
            x_y = j.split('-')
            int_list = list(map(int,x_y))
            lowerr = int_list[0]           # lower_ class
            h = int_list[1] - int_list[0] # h
            freq = dt[j]    # freq
            # print(f"\n {lowerr} and {freq}")
        
    ans = lowerr + (((mediann - c_f) / freq) * h)
    print("\n\n")
    print("\t\t Median = l    +   (N/2 - C.F)   *   h")
    print("\t\t                   -----------")
    print("\t\t                        F ")
    print("\n")
    print(f"\t\tl = {lowerr} , h = {h} , F = {freq} , C.F = {c_f} , N = {n} , N/2 = {mediann}\n")
    print(f"\t\t Median = {lowerr}    +  ({mediann} - {c_f})   *   {h}")
    print("\t\t                    ----------")
    print(f"\t\t                        {freq} ")
    print(f"\n\t\tMedian = {ans}")
    print("\n")

def struct_menu(dt):
    print("1. Mean \n2. Median \n3. Mode")
    x = int(input("Enter the operation number you want to perform : "))
    os.system('cls')
    if x == 1:
        mean_menu(dt)

    elif x == 2:
        median_class(dt)

    elif x == 3:
        modal_class(dt)

    else:
        print("You choose wrong option, Try again!!!!")
        print("\n")
        struct_menu(dt)

def struct_input():
    x = int(input("Enter the number of observations to add : "))
    dt = {}
    # dt = {"10-25": 2,"25-40":3,"40-55":7,"55-70":6,"70-85":6,"85-100":6}
    print("Enter class interval like provided example(example : 10-20)")
    for i in range(x):
        x = input("Class interval : ")
        y = int(input("Frequency : "))
        dt[x] = y
    os.system('cls')
    struct_menu(dt)

def unstruct_inpuut():
    data = []
    print("\n")
    x = int(input("Enter the number of Observations to add : "))
    print("\n")
    for i in range(x):
        y = int(input(f"Enter observation {i+1} : "))
        data.append(y)
    
    print("\n")
    mean(data)
    mode(data)
    median(data)
    
def menu():
    print("\n\n\t\tWhat kind of data you have, choose one from below\n")
    print("\t\t1. Structured Data ")
    print("\n\t\tExample :| 10-20 | 20-30 | 30-40 |")
    print("\t\t         |   5   |   8   |   3   |")
    print("\n\n")
    print("\t\t2. Unstructured Data\n")
    print("\t\tExample :   23   4   12   3   10")
    x = int(input("\n\n\t\tSelect 1 or 2 : "))
    os.system('cls')
    if x == 1:
        struct_input()

    elif x == 2:
        unstruct_inpuut()

    else:
        print("You pressed wrong option, try again!!!")
        menu()

if __name__ == "__main__":
    msg()
    menu()