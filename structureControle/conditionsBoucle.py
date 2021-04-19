#Structures conditionnelles


#If elif else
a = 10
if (a > 0):
    print(str(a) + " est supérieur à 0")
    if a%2 == 0:
        print(str(a) + " est pair")
    else:
        print(str(a) + " est pair")




#Switch case
def week(i):
        switcher={
            0:'Sunday',
            1:'Monday',
            2:'Tuesday',
            3:'Wednesday',
            4:'Thursday',
            5:'Friday',
            6:'Saturday'
        }
        print(type(switcher))
        return switcher.get(i,"Invalid day of week")

print(week(10))