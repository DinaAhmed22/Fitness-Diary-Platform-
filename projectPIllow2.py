from tkinter import *
from tkinter import ttk #for combobox
from tkinter import messagebox #for alerts
from PIL import ImageTk,Image
def get_age():
    age=int(ageENTRY.get())
    return age
def get_gender():
    gender=str(Gendercombox.get())
    return gender
def get_height():
    height = float(heightENTRY.get())
    return height
def get_weight():
    weight = float(w1.get())
    return weight
def get_weight2():
    weight = float(w.get())
    return weight
def get_Activity():
    activity=str(ActBox.get())
    return activity
def getGoal():
    goal=str(GoalBox.get())
    return goal
def get_Breakfast_cals():
    BreakfastCals=float(BreakfastEntry.get())
    return BreakfastCals
def get_Lunch_cals():
    LunchCals=float(LunchEntry.get())
    return LunchCals
def get_Snacks_cals():
    SnacksCals=float(SnackEntry.get())
    return SnacksCals
def get_Dinner_cals():
    DinnerCals=float(DinnerEntry.get())
    return DinnerCals
def get_Protein_Grams():
    protein=float(proteinEntry.get())
    return protein
def get_Carbohydrates_Grams():
    carbohydrates=float(carbEntry.get())
    return carbohydrates
def get_Fats_Grams():
    Fats=float(fatsEntry.get())
    return Fats
def getGramsinFood():
    grams=float(GramsEntry.get())
    return grams
def getMinutesPlayed():
    minutes=int(WorkoutMinEntry.get())
    return minutes
def getMets():
    Mets=str(MetsComboBox.get())
    return Mets
def Mets():  
    W=get_weight2()
    Met=getMets()
    min=getMinutesPlayed()
    if Met=='Sitting at a desk ':
        burnedcalories=1.3*3.5*(W/200)*min
        burnedcalories=round(burnedcalories)
        MetsResultTable['text']=f"Calories Burned : {burnedcalories} calories"   
    elif Met=='Washing Dishes':
        burnedcalories=2.2*3.5*(W/200)*min
        burnedcalories=round(burnedcalories)
        MetsResultTable['text']=f"Calories Burned : {burnedcalories} calories"   
    elif Met=='Yoga':
        burnedcalories=2.5*3.5*(W/200)*min
        burnedcalories=round(burnedcalories)
        MetsResultTable['text']=f"Calories Burned : {burnedcalories} calories"   
    elif Met=='Housework':
        burnedcalories=3.5*3.5*(W/200)*min
        burnedcalories=round(burnedcalories)
        MetsResultTable['text']=f"Calories Burned : {burnedcalories} calories"   
    elif Met=='Weight Training(Light Weights)':
      burnedcalories=3.5*3.5*(W/200)*min
      burnedcalories=round(burnedcalories)
      MetsResultTable['text']=f"Calories Burned : {burnedcalories} calories"   
    elif Met=='Golf':
        burnedcalories=4.3*3.5*(W/200)*min
        burnedcalories=round(burnedcalories)
        MetsResultTable['text']=f"Calories Burned : {burnedcalories} calories"   
    elif Met=='Weight Training(Heavier Weights)':
        burnedcalories=5*3.5*(W/200)*min
        burnedcalories=round(burnedcalories)
        MetsResultTable['text']=f"Calories Burned : {burnedcalories} calories"   
    elif Met=='Swimming':
        burnedcalories=6*3.5*(W/200)*min
        burnedcalories=round(burnedcalories)
        MetsResultTable['text']=f"Calories Burned : {burnedcalories} calories"   
    elif Met=='bicyling 12-14 mph':
        burnedcalories=8*3.5*(W/200)*min
        burnedcalories=round(burnedcalories)
        MetsResultTable['text']=f"Calories Burned : {burnedcalories} calories"   
    elif Met=='Running (7mph)':
        burnedcalories=11.5*3.5*(W/200)*min
        burnedcalories=round(burnedcalories)
        MetsResultTable['text']=f"Calories Burned : {burnedcalories} calories"   
def DailyCalorieCal():
    breakfast=get_Breakfast_cals()
    lunch=get_Lunch_cals()
    Snack=get_Snacks_cals()
    Dinner=get_Dinner_cals()
    totalcalories=round(breakfast+lunch+Snack+Dinner)
    LabelTotalDayCalories['text']=f"Total Daily Calories :{totalcalories} "
    if totalcalories<1000:
        messagebox.showwarning("showwarning", "Eating Less than 1000 calories will harm your health")
def deleteData():
    w.delete("0","end")
    w1.delete("0","end")
    heightENTRY.delete("0","end")
    ageENTRY.delete("0","end")
    Gendercombox.delete("0","end")
    ActBox.delete("0","end")   
    GoalBox.delete("0","end")
    BreakfastEntry.delete("0","end")
    LunchEntry.delete("0","end")
    SnackEntry.delete("0","end")
    DinnerEntry.delete("0","end")
    proteinEntry.delete("0","end")
    carbEntry.delete("0","end")
    fatsEntry.delete("0","end")
    GramsEntry.delete("0","end")
    MetsComboBox.delete("0","end")
    WorkoutMinEntry.delete("0","end")
def calculate_bmi():   
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
        bmi=round(bmi,2)
        if bmi <= 18.5:
            res =  str(bmi)+" " +" Underweight!"
            ENTRYBMIRES['text']=f"{res}"
        elif 18.5< bmi <= 24.9:
            res =  str(bmi)+' '+ "Healthy Weight"
            ENTRYBMIRES['text']=f"{res}"
        elif 25.0 < bmi <= 30:
            res =  str(bmi)+' '+ " Overweight."
            ENTRYBMIRES['text']=f"{res}"
        elif 30.0 < bmi <= 34.9:
            res =  str(bmi)+' '+ "obese Class 1"
            ENTRYBMIRES['text']=f"{res}"
        elif 35.0 < bmi <= 39.9:
            res = str(bmi)+' '+ "obese class 2"
            ENTRYBMIRES['text']=f"{res}"
        else:
            res =  str(bmi) +' '+ " Obese Class 3 "
            ENTRYBMIRES['text']=f"{res}"
            
def calculate_BMR():
    height = get_height()
    weight = get_weight()
    age=get_age()
    gender=get_gender()
    if get_gender()=='Male':
        BMR=round(88.362+(13.397*weight)+(4.799*height)-(5.677*age))
        BMRLabel['text']=f"BMR : {BMR} Calories"
    elif get_gender()=='Female':
        BMR=round(447.593+(9.247*weight)+(3.098*height)-(4.330*age))
        BMRLabel['text']=f"BMR : {BMR} Calories"
    else:
        messagebox.showinfo("Show warning","Invalid Input ")
    return BMR    
def calories_Needed_according_to_activity():
    activity = get_Activity()
    x=calculate_BMR()
    if activity=="Little Exercise or No Exercise":
       caloriesneeded=round(x*1.2)
       CaloriesNeededLabel['text']=f"Calories Needed: {caloriesneeded}"
    elif activity==" Light Exercise or few times a week":
        caloriesneeded=round(x*1.375)
        CaloriesNeededLabel['text']=f"Calories Needed: {caloriesneeded}" 
    elif activity== "Moderate Exercise 3-5 times a week":
        caloriesneeded=round(x*1.55)
        CaloriesNeededLabel['text']=f"Calories Needed: {caloriesneeded}"
    elif activity=="Heavy exercise 6-7 times per week":
        caloriesneeded=round(x*1.725)
        CaloriesNeededLabel['text']=f"Calories Needed: {caloriesneeded}"
    else:
      
        messagebox.showinfo("Show Warning","Invalid Input" )   
    return caloriesneeded

def BodyGoal():
    y=calories_Needed_according_to_activity()
    g=getGoal()
    if g=="Lose Weight":
        Calor=round(y-500.0)
        GoalLabel['text']=f"You need {Calor} calories to lose weight"
    elif g=="Gain Weight":
        Calor=round(y+500.0)
        GoalLabel['text']=f"You need {Calor} calories to gain weight"
    elif g=="Mantain Weight":
         Calor=y
         GoalLabel['text']=f"You need :{Calor} calories"
    else:
        messagebox.showinfo("Show warning","Invalid Input ")
    return Calor
def CaloriesperFood():
    carbs=get_Carbohydrates_Grams()
    protein=get_Protein_Grams()
    fats=get_Fats_Grams()
    grams=getGramsinFood()
    protein=protein*4.0
    fats=fats*9.0
    carbs=carbs*4.0
    total=(protein+fats+carbs)*(grams)
    total=round(total)
    TotalCaloriesperFoodLabel['text']=f"{total} "
def opennewwindowWorkouts():
    newwindow=Toplevel(root)
    newwindow.title("Workouts Options")
    newwindow.geometry('800x800')
    newwindow.config(bg='#91256B')
    Framex=Frame(newwindow,bg='#C20A82',width='700',height='700')
    Framex.pack(side=TOP)
    Cardiworkout=Label(Framex,text='Cardio Workouts ',bg='pink',font=('Helvetica', 11, 'bold')).pack()
    Cardiworkout=ttk.Treeview(Framex,columns=(1,2,3,4),show='headings',height=8)
    Cardiworkout.pack()
    Cardiworkout.heading(1,text='Workout',anchor=CENTER)
    Cardiworkout.heading(2,text='sets',anchor=CENTER)
    Cardiworkout.heading(3,text='reps',anchor=CENTER)
    Cardiworkout.heading(4,text='Equipment needed',anchor=CENTER)
    Cardiworkout.insert(parent="",index=0,values=('Push-ups','3 sets','10 reps','With a wall '))
    Cardiworkout.insert(parent="",index=1,values=('Jumping Jacks','3 sets' ,'30 reps','No equipment'))
    Cardiworkout.insert(parent="",index=2,values=('Jumping Rope','3 sets' ,'30 reps','Rope '))
    Cardiworkout.insert(parent="",index=3,values=('March in Place','3 sets' ,'30 reps','No Equipment'))
    Cardiworkout.insert(parent="",index=4,values=('Jumping Squats','3 sets' ,'30 reps','Resitance band ,Dumbells '))
    Cardiworkout.insert(parent="",index=5,values=('Mountain Climbers','3 sets' ,'30 reps','No equipment'))
    Cardiworkout.insert(parent="",index=6,values=('Step-Ups ','3 sets' ,'15 reps on each leg','Chair or Stepper'))
    Cardiworkout.insert(parent="",index=7,values=('Russian Swing ','3 sets' ,'30 reps','KettleBell,1 Dumbell,Bottle of Water'))
    style=ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    Strengthworkout=Label(Framex,text='Strength Workouts ',bg='pink',font=('Helvetica', 11, 'bold')).pack()
    Strengthworkout=ttk.Treeview(Framex,columns=(1,2,3,4),show='headings',height=8)
    Strengthworkout.pack()
    Strengthworkout.heading(1,text='Workout',anchor=CENTER)
    Strengthworkout.heading(2,text='sets',anchor=CENTER)
    Strengthworkout.heading(3,text='reps',anchor=CENTER)
    Strengthworkout.heading(4,text='Equipment Needed',anchor=CENTER)
    Strengthworkout.insert(parent="",index=0,values=('Bicep-Curl(Biceps)','3 sets','15 reps','Dumbells,Water Bottles'))
    Strengthworkout.insert(parent="",index=1,values=('Deadlifts(Lower Body)','3 sets','15 reps','Dumbells'))
    Strengthworkout.insert(parent="",index=2,values=('Sumo-Deadlift(Lower body)','3 sets' ,'15 reps','Dumbells'))
    Strengthworkout.insert(parent="",index=3,values=('Tricep-Kickbacks(Triceps)','3 sets' ,'15 reps','Dumbells,Water Bottles'))
    Strengthworkout.insert(parent="",index=4,values=('Overhead extension(Triceps)','3 sets' ,'15 reps','Dumbells,Water Bottles'))
    Strengthworkout.insert(parent="",index=5,values=('Russian Twist(Abs)','3 sets' ,'15 reps','Dumbells,Water Bottles'))
    Strengthworkout.insert(parent="",index=6,values=('Bulgrian Squats(Lower body)','3 sets' ,'8 reps on each leg','Dumbells,KettleBell'))
    Strengthworkout.insert(parent="",index=7,values=('Hammer Curls(Biceps)','3 sets' ,'15 reps ','Dumbells,Water Bottles'))
    Strengthworkout.insert(parent="",index=8,values=('Reverse Lunges (Lower body) ','3 sets' ,'8 reps on each leg','Dumbells'))
    Strengthworkout.insert(parent="",index=9,values=('Calves Raise (Calves)','3 sets' ,'15 reps','Dumbells'))
    Strengthworkout.insert(parent="",index=10,values=('Goblet Squat (Lower Body)','3 sets' ,'15 reps','Dumbells,KettleBell'))
    Strengthworkout.insert(parent="",index=11,values=('Chest Press (Chest)','3 sets' ,'15 reps','Dumbells,Water Bottles'))
    style=ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    EquipmentLA=Label(Framex,text='Gym Equipment You Can have at home ',bg='pink',font=('Helvetica', 11, 'bold')).pack()
    Equipment=ttk.Treeview(Framex,columns=(1,2),show='headings',height=8)
    Equipment.pack()
    Equipment.heading(1,text='Equipment',anchor=CENTER)
    Equipment.heading(2,text='Place to buy from',anchor=CENTER)
    Equipment.insert(parent="",index=0,values=('Trademill','Amazon(online)'))
    Equipment.insert(parent="",index=1,values=('Dumbells','Amazon(online)'))
    Equipment.insert(parent="",index=2,values=('KettleBell','Amazon(online)'))
    Equipment.insert(parent="",index=3,values=('Pull-Up','Ali-Baba(online)'))
    Equipment.insert(parent="",index=4,values=('Resitance Bands','Amazon(online)'))
    Equipment.insert(parent="",index=5,values=('Orbit Track','Amazon(online)'))
    Equipment.insert(parent="",index=6,values=('Top Fit AB Rocket','Amazon(online)'))
    Equipment.insert(parent="",index=7,values=('Gym Bike','Jumia(online)'))
    style=ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    YoutubeChannelsLabel=Label(Framex,text=" Youtube Channels You can workout with",bg='pink',font=('Helvetica', 11, 'bold')).pack()
    YoutubeChannels=ttk.Treeview(Framex,columns=(1,2),show='headings',height=8)
    YoutubeChannels.pack()
    YoutubeChannels.heading(1,text='Youtube Channels',anchor=CENTER)
    YoutubeChannels.heading(2,text='Level',anchor=CENTER)
    YoutubeChannels.insert(parent="",index=0,values=('Lumowell','beginners'))
    YoutubeChannels.insert(parent="",index=1,values=('PopSugar Fittnes','All levels'))
    YoutubeChannels.insert(parent="",index=2,values=('Hasfit','All Level'))
    style=ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    newwindow.resizable(False,False)
    newwindow.mainloop()
def openRecipesWindow():
    newwindow=Toplevel(root)
    newwindow.title("Food Calorie Table")
    newwindow.geometry('900x1000')
    newwindow.config(bg='#91256B')
    newwindow.resizable(False,False)
    Framex=Frame(newwindow,bg='#C20A82',width='900',height='1000')
    Framex.pack()
    FastLabel=Label(Framex,text='Fast Food',bg='#7B0750',font=('Helvetica', 11, 'bold')).pack()
    FastView=ttk.Treeview(Framex,columns=(1,2,3),show='headings',height=8)
    FastView.pack()
    FastView.heading(1,text='Food',anchor=CENTER)
    FastView.heading(2,text='Quantity',anchor=CENTER)
    FastView.heading(3,text='Calories',anchor=CENTER)
    FastView.insert(parent="",index=0,values=('MacDondals Big Mac','80 oz,210 gr','490'))
    FastView.insert(parent="",index=1,values=('Hamburger Burger King','60 oz,180 gr' ,'360'))
    FastView.insert(parent="",index=2,values=('Fried Chicken KFC','20 oz,70 gr' ,'195'))
    style=ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    FruitsLabel=Label(Framex,text='Fruits ',bg='#7B0750',font=('Helvetica', 11, 'bold')).pack()
    FoodTreeView=ttk.Treeview(Framex,columns=(1,2,3),show='headings',height=8)
    FoodTreeView.pack(padx='10',pady='10')
    FoodTreeView.heading(1,text='Food',anchor=CENTER)
    FoodTreeView.heading(2,text='Quantity',anchor=CENTER)
    FoodTreeView.heading(3,text='Calories',anchor=CENTER)
    FoodTreeView.insert(parent="",index=0,values=('Apples','35 oz,100 gram','58'))
    FoodTreeView.insert(parent="",index=1,values=('Orange','35 oz,100 gram' ,'45'))
    FoodTreeView.insert(parent="",index=2,values=('Pear','35 oz,100 gram' ,'76'))
    FoodTreeView.insert(parent="",index=3,values=('Strawberries','35 oz,100 gram' ,'72'))
    style=ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    DriedFruitsLabel=Label(Framex,text='Dried Fruits',bg='#7B0750',font=('Helvetica', 11, 'bold')).pack()
    DriedFrutsView=ttk.Treeview(Framex,columns=(1,2,3),show='headings',height=8)
    DriedFrutsView.pack()
    DriedFrutsView.heading(1,text='Food',anchor=CENTER)
    DriedFrutsView.heading(2,text='Quantity',anchor=CENTER)
    DriedFrutsView.heading(3,text='Calories',anchor=CENTER)
    DriedFrutsView.insert(parent="",index=0,values=('Almonds','35 oz,100 gram' ,'640'))
    DriedFrutsView.insert(parent="",index=1,values=('Hazelnuts','35 oz,100 gram' ,'630'))
    DriedFrutsView.insert(parent="",index=2,values=('Chestnuts','35 oz,100 gram' ,'610'))
    style=ttk.Style()
    style.theme_use("default")
    style.map("Treeview")
    OilsFatsLabel=Label(Framex,text='Oils and Fat',bg='#7B0750',font=('Helvetica', 11, 'bold')).pack()
    OilsFatsView=ttk.Treeview(Framex,columns=(1,2,3),show='headings',height=8)
    OilsFatsView.pack()
    OilsFatsView.heading(1,text='Food',anchor=CENTER)
    OilsFatsView.heading(2,text='Quantity',anchor=CENTER)
    OilsFatsView.heading(3,text='Calories',anchor=CENTER)
    OilsFatsView.insert(parent="",index=0,values=('Olive Oil','spoon( 3 oz,10 gr)','90'))
    style=ttk.Style()
    style.theme_use("default")
    style.map("Treeview")

    newwindow.mainloop()
# # # # ################################
root=Tk()
root.title("My Fittness Diary")
root.geometry('700x700')
root.config(bg='#797D7F')
canvas= Canvas(root,bg='#797D7F', width= 150, height= 150)
canvas.pack(padx='10',pady='10')
img= (Image.open("E:\ss2.png"))
resized_image= img.resize((100,100), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_image(25,25, anchor=NW, image=new_image)
Frame1=Frame(root,bg="#CCB4C7",width='399',height='499') #Personal Data Frame
Frame1.pack(side=LEFT,padx='5',pady='10')
Frame3=Frame(root,bg='#0D8689',width='599',height='499') #Calories burnt calculator
Frame3.pack(side=LEFT,padx='50',pady='50')
Frame4=Frame(root,bg='#7A4A4A',width='399',height='499') #calorie and food tracker calculator
Frame4.pack(side=RIGHT,padx='6',pady='10')
#########################################       
Frame5=Frame(root,bg='#797D7F',width='499',height='599')#for buttons
Frame5.place(x=1,y=1)
ExitBut=Button(Frame5,text='Exit',bg='#5C0101',fg='black',width='20',command=exit).pack(side=TOP,padx='10',pady='10')
WorkoutsopBut=Button(Frame5,text='Workouts Options',bg='#8811A1',fg='black',width='20',command=opennewwindowWorkouts).pack(side=TOP,padx='10',pady='10')
HealthRecipiesMenuButton=Button(Frame5,text="Food Calories ",bg='#7A4A4A',fg='black',width='20',command=openRecipesWindow).pack(side=TOP,padx='10',pady='10')
####################################################################
Tt1=Label(Frame1,text="Enter Your Personal Data",bg='#CCB4C7',fg='#000057',font=('Helvetica', 11, 'bold'))
Tt1.pack()
LabelW=Label(Frame1,text="Enter Your Weight in (KG) ",fg='Black',bg="#CCB4C7")
LabelW.pack()
w1=Entry(Frame1,justify='center')
w1.pack()
LabelH=Label(Frame1,text="Enter Your Height in (CM) ",fg='Black',bg='#CCB4C7')
LabelH.pack()
heightENTRY=Entry(Frame1,justify='center')
heightENTRY.pack()
Labela=Label(Frame1,text="Enter Your age ",fg='Black',bg='#CCB4C7')
Labela.pack()
ageENTRY=Entry(Frame1,justify='center')
ageENTRY.pack()
genderL=Label(Frame1,text="Choose Your Gender",fg='Black',bg='#CCB4C7')
genderL.pack()
Gendercombox=ttk.Combobox(Frame1,values=['Female','Male'])
Gendercombox.pack()
Labelact=Label(Frame1,text="Enter Activity Level ",fg='Black',bg='#CCB4C7')
Labelact.pack()
ActBox=ttk.Combobox(Frame1,values=["Little Exercise or No Exercise"," Light Exercise or few times a week","Moderate Exercise 3-5 times a week","Heavy exercise 6-7 times per week"],state='read only',justify='center')
ActBox.pack()
GoalCalsLabel=Label(Frame1,text="Choosee Your Goal",bg='#CCB4C7',fg='black')
GoalCalsLabel.pack()           
GoalBox=ttk.Combobox(Frame1,value=['Lose Weight','Gain Weight','Mantain Weight'])
GoalBox.pack()
Tt2=Label(Frame1,text=" Calculate ",bg='#CCB4C7',fg='#2424ff',font=('Helvetica', 11, 'bold'))
Tt2.pack()
BUTTONBMI = Button(Frame1, text="BMI Calculate",  command=calculate_bmi)
BUTTONBMI.pack()
ENTRYBMIRES=Label(Frame1,fg='Black',bg='#CCB4C7')
ENTRYBMIRES.pack()
BMRButton=Button(Frame1,text="BMR Calculate ",command=calculate_BMR)
BMRButton.pack()
BMRLabel=Label(Frame1, text="",bg='#CCB4C7',fg='black')
BMRLabel.pack()
CalsActButton=Button(Frame1, text=" AMR Calculate ",command=calories_Needed_according_to_activity)
CalsActButton.pack()
CaloriesNeededLabel=Label(Frame1,text="",bg='#CCB4C7',fg='black')
CaloriesNeededLabel.pack() 
GoalCalsButton=Button(Frame1,text="Calories according to goal",command=BodyGoal).pack()
GoalLabel=Label(Frame1,text="   ",bg='#CCB4C7',fg='black')
GoalLabel.pack()
DeleteDataButton=Button(Frame1,text="Erase Data",bg='#922B21',command=deleteData,fg='Black')
DeleteDataButton.pack(side=LEFT)
root.resizable('false','false')
########################################################################################################################
TitleLabel4=Label(Frame4,text='Calorie Tracker',bg='#7A4A4A',fg='#3A0731',font=('Helvetica', 12, 'bold')).pack()
labelLunch=Label(Frame4,text="Enter Calories of Breakfast",bg='#7A4A4A',fg='black').pack()
BreakfastEntry=Entry(Frame4,justify='center')
BreakfastEntry.pack()
labelLunch=Label(Frame4,text="Enter Calories of Lunch",bg='#7A4A4A',fg='black').pack()
LunchEntry=Entry(Frame4,justify='center')
LunchEntry.pack()
labelSnack=Label(Frame4,text="Enter Calories of Snacks",bg='#7A4A4A',fg='black').pack()
SnackEntry=Entry(Frame4,justify='center')
SnackEntry.pack()
labelLunch=Label(Frame4,text="Enter Calories of Dinner",bg='#7A4A4A',fg='black').pack()
DinnerEntry=Entry(Frame4,justify='center')
DinnerEntry.pack()
TotalCalsButton=Button(Frame4, text="Calculate Total calories/day",command=DailyCalorieCal)
TotalCalsButton.pack()
LabelTotalDayCalories=Label(Frame4,text="",bg='#7A4A4A',fg='black')
LabelTotalDayCalories.pack()
######################################################################################
TitleLabel4=Label(Frame4,text='Food Calorie Calculator',bg='#7A4A4A',fg='#3A0731',font=('Helvetica', 12, 'bold')).pack()
proteinLabel=Label(Frame4,text="Enter Grams of protein/gram",bg='#7A4A4A',fg='black').pack()
proteinEntry=Entry(Frame4,justify='center')
proteinEntry.pack()
CarbLabel=Label(Frame4,text="Enter Grams of Carbs/gram",bg='#7A4A4A',fg='black').pack()
carbEntry=Entry(Frame4,justify='center')
carbEntry.pack()
FatsLabel=Label(Frame4,text="Enter Grams of fats/gram",bg='#7A4A4A',fg='black').pack()
fatsEntry=Entry(Frame4,justify='center')
fatsEntry.pack()
GramsLabel=Label(Frame4,text="Enter Grams of Food(using scale)",bg='#7A4A4A',fg='black').pack()
GramsEntry=Entry(Frame4,justify='center')
GramsEntry.pack()
CaloriesperfoodButton=Button(Frame4,text="Calculate Total Calories in Food",command=CaloriesperFood)
CaloriesperfoodButton.pack()
TotalCaloriesperFoodLabel=Label(Frame4,text=" ",bg='#7A4A4A',fg='black')
TotalCaloriesperFoodLabel.pack()
DeleteDataButton2=Button(Frame4,text="Erase Data",command=deleteData,bg='#922B21',fg='Black')
DeleteDataButton2.pack(side=LEFT)
####################################################################
TitleLabel=Label(Frame3,text="Activity Burner Calculator",fg='Black',bg='#0D8689',font=('Helvetica', 11, 'bold'))
TitleLabel.pack()
KGMetsLabel=Label(Frame3,text="Enter Weight in KG ",fg='Black',bg='#0D8689')
KGMetsLabel.pack()
w=Entry(Frame3,justify='center')
w.pack()
TypeWorkoutLabel=Label(Frame3,text="Choose Activity(Workout) done",fg='Black',bg='#0D8689').pack()
MetsComboBox=ttk.Combobox(Frame3,values=['Sitting at a desk ','Washing Dishes','Yoga','Housework','Weight Training(Light Weights)','Golf','Weight Training(Heavier Weights)','Swimming','bicyling 12-14 mph','Running (7mph)'])
MetsComboBox.pack()
MinLabel=Label(Frame3,text="Enter Workout Minutes ",fg='Black',bg='#0D8689')
MinLabel.pack()
WorkoutMinEntry=Entry(Frame3,justify='center')
WorkoutMinEntry.pack()
CalorieBurnedButton=Button(Frame3,text="Calculate Calories Burnt",command=Mets)
CalorieBurnedButton.pack()
MetsResultTable=Label(Frame3,text=" ",fg='Black',bg='#0D8689')
MetsResultTable.pack()
DeleteDataButton3=Button(Frame3,text="Erase Data",command=deleteData,bg='#922B21',fg='Black')
DeleteDataButton3.pack(side=LEFT)
root.mainloop()

