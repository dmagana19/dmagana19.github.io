from tkinter import *
from tkinter import PhotoImage #this is so I can send png files to have pictures
import logging
from collections import Counter

root = Tk()
root.title("Resistor Calculator")

#Putting a pic onto the app
icon = PhotoImage(file="resistor.png")
icon = icon.subsample(4,4)
icon_label = Label(root, image=icon, bg="white",) #Need to use image= function as a way for the code to identify that it is an image and not a variable
icon_label.grid(row=17, column=2)




my_values_resistors= { "0": "Black", "1":"Brown", "2": 'Red',
            '3': 'Orange', '4': 'Yellow', '5': 'Green', '6':"Blue",
            '7': 'Purple', '8': 'Grey', '9': 'White',
            #MULTIPLIERS NOW
            '1.0': 'Black', '10.0': "Brown", '100.0': "Red", '1000.0': 'Orange',
            '10000.0': 'Yellow', '100000.0': 'Green', '1000000.0': 'Blue', '10000000.0': 'Purple',
            '100000000.0': 'Grey', '1000000000.0': 'White', '0.1': 'Gold'
            }




#Using a def function to get the calculator working
def myClick(number):
    box_1.delete(0,END)
    new = box_1.get()
    box_1.delete(0,END)
    box_1.insert(0, str(new) + str(number))



#1st Band
box_1 = Entry(root, width = 20, fg= "Red", borderwidth=5)
box_1.grid(row=12, column=1)

def myClick_1(number):
    band.delete(0,END)
    current = band.get()
    band.delete(0,END)
    band.insert(0, str(current) + str(number))




#2nd Band 
band = Entry(root, width = 20, fg= "Red", borderwidth=5)
band.grid(row=12, column=2)

def myClick_2(number):
    box_2.delete(0,END)
    new = box_2.get()
    box_2.delete(0,END)
    box_2.insert(0, str(new) + str(number))



#3rd multiplier
box_2 = Entry(root, width = 20, fg= "Red", borderwidth=5)
box_2.grid(row=12, column=3)


def myClick_3(number):
    box_3.delete(0,END)
    new_1 = box_3.get()
    box_3.delete(0,END)
    box_3.insert(0, str(new_1) + str(number))



#TOLERANCE Insert
box_3 = Entry(root, width = 20, fg= "Red", borderwidth=5)
box_3.grid(row=12, column=4)

def reset():
    box_1.delete(0,END)
    band.delete(0,END)
    box_2.delete(0,END)
    box_3.delete(0,END)
    result.delete(0,END)

button_clear = Button(root, text='Clear', pady=5, fg='black',borderwidth=1,relief='solid', command=reset)
button_clear.grid(row=12, column= 0, sticky='nsew')




overall_count = Counter()

#FINAL VALUE RESISTOR
#Need to use the dictionary to create the logger value
def calculate():

    val_1 = box_1.get()
    val_2 = band.get()
    val_3 = box_2.get()
    val_4 = box_3.get()

    #This is a safety to ensure that if the user doesn't enter anything then it will not crash
    if not val_1: val_1 = "0"
    if not val_2: val_2 = '0'
    if not val_3: val_3 = '0'
    if not val_4: val_4 = '0'

    band_1 = int(val_1)
    band_2 = int(val_2)
    band_3 = float(val_3)
    band_4 = val_4



    # TO CREATE A HISTORY
    logging.basicConfig(level=logging.INFO, filename= "History.log", filemode= "a")
    
    #Need to tansform them back into colors. if doesn't have a value assigned then it prints back a unknown. It's a safeguard to prevent fails
    colors_1 = my_values_resistors.get((str(band_1)), "Unknown")
    colors_2 = my_values_resistors.get((str(band_2)), "Unknown")
    colors_3 = my_values_resistors.get((str(band_3)), "Unknown")
    logging.info(f"\n 1st band is {colors_1}, 2nd band is {colors_2}, and 3rd band is {colors_3}")
    my_counter = [colors_1, colors_2, colors_3] #You're counting based off your 3 buttons. We are using a list to make sure it's reading all of them at the same time
    overall_count.update(my_counter)
    most_common_color = overall_count.most_common(1)[0][0]
    logging.info(f"The most commmon color used is {most_common_color}")
    
    resistance = ((band_1 * 10) + band_2) * band_3
    
    if resistance >= 1000 and resistance < 1000000:
        resistance = resistance/1000
        result.delete(0,END)
        result.insert(0, str(resistance) +'k\u2126 ' + "\u00b1" + str(band_4) + "%")
    
    elif resistance >= 1000000 and resistance < 1000000000:
        resistance = resistance/1000000
        result.delete(0,END)
        result.insert(0, str(resistance) +'M\u2126 ' + "\u00b1" + str(band_4) + "%")

    elif resistance >= 1000000000:
        resistance = resistance/1000000000
        result.delete(0,END)
        result.insert(0, str(resistance) +'G\u2126 ' + "\u00b1" + str(band_4) + "%")

    else:
        result.delete(0,END)
        result.insert(0, str(resistance) +'\u2126 ' + "\u00b1" + str(band_4) + "%")



#The button and the result prints
button_calculate = Button(root, text='Calculate', pady=5, fg='black',borderwidth=1,relief='solid', command=calculate)
button_calculate.grid(row=15, column= 2, sticky='nsew')
result = Entry(root, width=15, fg = "red", borderwidth = 5)
result.grid(row=16, column=2)

    

#size of the map
root.geometry("900x900")







#Labeled the titles, causes the column to be even regardless if I stretch the app. The weight indicates the amount of separation. In this case 1 column worth
# The I represents the individual columns and in this case there are 5. The .grid_columnconfigure just is a function that ensures the buttons are evenly spaced
for i in range(5):
    root.grid_columnconfigure(i, weight=1, uniform="col_group")



#column labels
label_color = Label(root, text= "Color", pady = 10, fg= "Black", bg = "#6A6A6A", borderwidth=1, relief= "solid")
label_color.grid(row = 0, column = 0, sticky="nsew")
label_black = Label(root, text= "Black", pady = 10, fg= "White", bg = "#060606", borderwidth=1, relief="solid")
label_black.grid(row=1, column= 0, sticky="nsew")
label_brown = Label(root, text="Brown", pady= 10, fg="white", bg="#62321B", borderwidth=1, relief="solid")
label_brown.grid(row=2, column=0, sticky="nsew")
label_red = Label(root, text="Red", pady= 10, fg="white", bg="#DB1A1A", borderwidth=1, relief="solid")
label_red.grid(row=3, column=0, sticky="nsew")
label_orange = Label(root, text="Orange", pady= 10, fg="white", bg="#FFA600", borderwidth=1, relief="solid")
label_orange.grid(row=4, column=0, sticky="nsew")
label_yellow = Label(root, text="Yellow", pady= 10, fg="white", bg="#EAEA0F", borderwidth=1, relief="solid")
label_yellow.grid(row=5, column=0, sticky="nsew")
label_green = Label(root, text="Green", pady= 10, fg="white", bg="#31DD13", borderwidth=1, relief="solid")
label_green.grid(row=6, column=0, sticky="nsew")
label_blue = Label(root, text="Blue", pady= 10, fg="white", bg="#0000FF", borderwidth=1, relief="solid")
label_blue.grid(row=7, column=0, sticky="nsew")
label_violet = Label(root, text="Purple", pady= 10, fg="white", bg="#9500FF", borderwidth=1, relief="solid")
label_violet.grid(row=8, column=0, sticky="nsew")
label_grey = Label(root, text="Grey", pady= 10, fg="white", bg="#525252", borderwidth=1, relief="solid")
label_grey.grid(row=9, column=0, sticky="nsew")
label_white = Label(root, text="White", pady= 10, fg="Black", bg="#FFFFFF", borderwidth=1, relief="solid")
label_white.grid(row=10, column=0, sticky="nsew")
label_gold = Label(root, text="Gold", pady= 10, fg="Black", bg= "#BAAB00", borderwidth=1, relief="solid")
label_gold.grid(row=11, column=0, sticky="nsew")






#Column 1st band
label_band_1 = Label(root, text="1st Band", pady = 10, fg = "black", bg = "#6a6a6a", borderwidth=1, relief= "solid")
label_band_1.grid(row = 0, column = 1, sticky="nsew")
label_black_1 = Label(root, text= "0", pady = 10, fg="#2d2828", bg = "#2D2828", borderwidth=1, relief="solid")
label_black_1.grid(row=1, column= 1, sticky="nsew")

button_brown = Button(root, text="1", pady=10, fg="black", bg='#62321B', borderwidth=1, relief="solid", command=lambda: myClick(1))
button_brown.grid(row=2, column = 1, sticky="nsew")
button_red = Button(root, text="2", pady=10, fg="black", bg="#DB1A1A", borderwidth=1, relief="solid", command=lambda:myClick(2))
button_red.grid(row=3, column = 1, sticky="nsew")
button_orange = Button(root, text="3", pady=10, fg="black", bg="#ffa600", borderwidth=1, relief="solid", command=lambda:myClick(3))
button_orange.grid(row=4, column = 1, sticky="nsew")
button_yellow = Button(root, text="4", pady=10, fg="black", bg="#eaea0f", borderwidth=1, relief="solid", command=lambda:myClick(4))
button_yellow.grid(row=5, column = 1, sticky="nsew")
button_green = Button(root, text="5", pady=10, fg="black", bg="#31dd13", borderwidth=1, relief="solid", command=lambda:myClick(5))
button_green.grid(row=6, column = 1, sticky="nsew")
button_blue = Button(root, text="6", pady=10, fg="black", bg="#0000ff", borderwidth=1, relief="solid", command=lambda:myClick(6))
button_blue.grid(row=7, column = 1, sticky="nsew")
button_violet = Button(root, text="7", pady=10, fg="black", bg="#9500ff", borderwidth=1, relief="solid", command=lambda:myClick(7))
button_violet.grid(row=8, column = 1, sticky="nsew")
button_grey = Button(root, text="8", pady=10, fg="black", bg="#525252", borderwidth=1, relief="solid", command=lambda:myClick(8))
button_grey.grid(row=9, column = 1, sticky="nsew")
button_white = Button(root, text="9", pady=10, fg="black", bg="#FFFFFF", borderwidth=1, relief="solid", command=lambda:myClick(9))
button_white.grid(row=10, column = 1, sticky="nsew")

label_gold_2 = Label(root, text=" ", pady=10, fg="black", bg="#Baab00", borderwidth=1, relief="solid")
label_gold_2.grid(row=11, column = 1, sticky="nsew")







#2nd band column
label_band_2 = Label(root, text="2nd Band", pady = 10, fg = "black", bg = "#6a6a6a", borderwidth=1, relief="solid")
label_band_2.grid(row = 0, column = 2, sticky="nsew")
label_gold_3 = Label(root, text=" ", pady=10, fg="black", bg='#Baab00', borderwidth=1, relief="solid")
label_gold_3.grid(row=11, column = 2, sticky="nsew")#This is on the last row but is a label

button_black_2 = Button(root, text= "0", pady = 10, fg="black", bg = "Black", borderwidth=1, relief="solid",command=lambda:myClick_1(0))
button_black_2.grid(row=1, column= 2, sticky="nsew")
button_brown_1 = Button(root, text="1", pady=10, fg="black", bg='#62321B', borderwidth=1, relief="solid", command=lambda:myClick_1(1))
button_brown_1.grid(row=2, column = 2, sticky="nsew")
button_red_1 = Button(root, text="2", pady=10, fg="black", bg='#Db1A1a', borderwidth=1, relief="solid", command=lambda:myClick_1(2))
button_red_1.grid(row=3, column = 2, sticky="nsew")
button_orange_1 = Button(root, text="3", pady=10, fg="black", bg='#ffa600', borderwidth=1, relief="solid", command=lambda:myClick_1(3))
button_orange_1.grid(row=4, column = 2, sticky="nsew")
button_yellow_1 = Button(root, text="4", pady=10, fg="black", bg='#eaea0f', borderwidth=1, relief="solid", command=lambda:myClick_1(4))
button_yellow_1.grid(row=5, column = 2, sticky="nsew")
button_green_1 = Button(root, text="5", pady=10, fg="black", bg='#31dd13', borderwidth=1, relief="solid", command=lambda:myClick_1(5))
button_green_1.grid(row=6, column = 2, sticky="nsew")
button_blue_1 = Button(root, text="6", pady=10, fg="black", bg='#0000ff', borderwidth=1, relief="solid", command=lambda:myClick_1(6))
button_blue_1.grid(row=7, column = 2, sticky="nsew")
button_violet_1 = Button(root, text="7", pady=10, fg="black", bg='#9500ff', borderwidth=1, relief="solid",command=lambda:myClick_1(7))
button_violet_1.grid(row=8, column = 2, sticky="nsew")
button_grey_1 = Button(root, text="8", pady=10, fg="black", bg='#525252', borderwidth=1, relief="solid", command=lambda:myClick_1(8))
button_grey_1.grid(row=9, column = 2, sticky="nsew")
button_white_1 = Button(root, text="9", pady=10, fg="black", bg="#FFFFFF", borderwidth=1, relief="solid", command=lambda:myClick_1(9))
button_white_1.grid(row=10, column = 2, sticky="nsew")



#Multiplier Column
label_multiplier = Label(root, text="Multiplier", pady = 10, fg = "black", bg = "#6a6a6a", borderwidth=1, relief="solid")
label_multiplier.grid(row = 0, column = 3, sticky = "nsew")

button_black_3 = Button(root, text= "1", pady = 10, fg="black", bg = "#060606", borderwidth= 1, relief="solid", command=lambda: myClick_2(1.0))
button_black_3.grid(row=1, column= 3, sticky="nsew")
button_brown_2 = Button(root, text="10", pady=10, fg="black", bg='#62321B', borderwidth=1, relief="solid", command=lambda:myClick_2(10))
button_brown_2.grid(row=2, column=3, sticky='nsew')
button_red_2 = Button(root, text="100", pady=10, fg="black", bg='#db1a1a', borderwidth=1, relief="solid", command=lambda: myClick_2(100))
button_red_2.grid(row=3, column=3, sticky='nsew')
button_orange_2 = Button(root, text="1000", pady=10, fg="black", bg='#ffa600', borderwidth=1, relief="solid", command=lambda: myClick_2(1000))
button_orange_2.grid(row=4, column=3, sticky='nsew')
button_yellow_2 = Button(root, text="10000", pady=10, fg="black", bg='#eaea0f', borderwidth=1, relief="solid", command=lambda: myClick_2(10000))
button_yellow_2.grid(row=5, column=3, sticky='nsew')
button_green_2 = Button(root, text="100000", pady=10, fg="black", bg='#31dd13', borderwidth=1, relief="solid", command=lambda: myClick_2(100000))
button_green_2.grid(row=6, column=3, sticky='nsew')
button_blue_2 = Button(root, text="1000000", pady=10, fg="black", bg='#0000ff', borderwidth=1, relief="solid", command=lambda: myClick_2(1000000))
button_blue_2.grid(row=7, column=3, sticky='nsew')
button_violet_2 = Button(root, text="10000000", pady=10, fg="black", bg='#9500ff', borderwidth=1, relief="solid", command=lambda:myClick_2(10000000))
button_violet_2.grid(row=8, column=3, sticky='nsew')
button_grey_2 = Button(root, text="100000000", pady=10, fg="black", bg='#525252', borderwidth=1, relief="solid", command=lambda:myClick_2(100000000))
button_grey_2.grid(row=9, column=3, sticky='nsew')
button_white_2 = Button(root, text="1000000000", pady=10, fg="black", bg="#FFFFFF", borderwidth=1, relief="solid", command=lambda:myClick_2(1000000000))
button_white_2.grid(row=10, column=3, sticky='nsew')
button_gold = Button(root, text="0.1", pady=10, fg="black", bg='#baab00', borderwidth=1, relief="solid", command=lambda:myClick_2(0.1))
button_gold.grid(row=11, column=3, sticky='nsew')



#Tolerance COLUMN
label_tolerance = Label(root, text="Tolerance (\u00b1)", pady = 10, fg = "black", bg = "#6a6a6a", borderwidth=1, relief="solid")
label_tolerance.grid(row = 0, column = 4, sticky="nsew")
label_black_4 = Label(root, text= "0", pady = 10, fg= "#2d2828", bg = "#2d2828", borderwidth=1, relief="solid")
label_black_4.grid(row=1, column= 4, sticky="nsew")


button_brown_3 = Button(root, text='\u00B1 1%', pady=10, fg='black', bg= "#62321B",borderwidth=1,relief='solid', command=lambda: myClick_3(1))
button_brown_3.grid(row=2, column= 4, sticky='nsew')
button_red_3 = Button(root, text='\u00B1 2%', pady=10, fg='black', bg= '#db1a1a',borderwidth=1,relief='solid', command=lambda: myClick_3(2))
button_red_3.grid(row=3, column= 4, sticky='nsew')
button_orange_3 = Button(root, text='\u00B1 0.05%', pady=10, fg='black', bg= '#ffa600',borderwidth=1,relief='solid', command=lambda: myClick_3(0.05))
button_orange_3.grid(row=4, column= 4, sticky='nsew')
button_yellow_3 = Button(root, text='\u00B1 0.02%', pady=10, fg='black', bg= '#eaea0f',borderwidth=1,relief='solid', command= lambda: myClick_3(0.02))
button_yellow_3.grid(row=5, column= 4, sticky='nsew')
button_green_3 = Button(root, text='\u00B1 0.5%', pady=10, fg='black', bg= '#31dd13',borderwidth=1,relief='solid', command=lambda: myClick_3(0.5))
button_green_3.grid(row=6, column= 4, sticky='nsew')
button_blue_3 = Button(root, text='\u00B1 0.25%', pady=10, fg='black', bg= '#0000ff',borderwidth=1,relief='solid', command=lambda: myClick_3(0.25))
button_blue_3.grid(row=7, column= 4, sticky='nsew')
button_violet_3 = Button(root, text='\u00B1 0.1%', pady=10, fg='black', bg= '#9500ff',borderwidth=1,relief='solid', command=lambda: myClick_3(0.1))
button_violet_3.grid(row=8, column= 4, sticky='nsew')
button_grey_3 = Button(root, text='\u00B1 0.01%', pady=10, fg='black', bg= '#525252',borderwidth=1,relief='solid', command=lambda: myClick_3(0.01))
button_grey_3.grid(row=9, column= 4, sticky='nsew')
label_white_2 = Label(root, text=' ', pady=10, fg='black', bg= "#FFFFFF",borderwidth=1, relief='solid')
label_white_2.grid(row=10, column= 4, sticky='nsew')
button_gold_3 = Button(root, text='\u00B1 5%', pady=10, fg='black', bg= '#baab00',borderwidth=1,relief='solid', command=lambda:myClick_3(5))
button_gold_3.grid(row=11, column= 4, sticky='nsew')


#Label to gain a space in the columns
label_empty = Label(root, text=' ', pady=5)
label_empty.grid(row=13, column= 0, sticky='nsew')



root.mainloop()