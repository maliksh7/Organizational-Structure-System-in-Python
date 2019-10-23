from tkinter import * 
Name_Orgranization  = []
Head_and_Department_Name_list = []
Department_Member_Name = []
Name_Orgranization  = []
Head_and_Department_Name_list = []
Department_Member_Name = []
def cc5(root):  #  head to departments
    head_to_dpt=Canvas(root,width=1500,height=250, highlightthickness=0)

    head_to_dpt.place(x=250,y=140)
    head_to_dpt.create_line(670,0,670,110,width=10)
    head_to_dpt.create_line(120,110,1355,110,width=10)   # 1200 to match with 5th box

    horizental_gap=121

    for i in range(5):   # loop = total number of departments
        head_to_dpt.create_line(horizental_gap,105,horizental_gap,250,arrowshape=(16,20,6),width=10,arrow=LAST)
        horizental_gap+=309
def cc4(root):  #  head to departments
    head_to_dpt=Canvas(root,width=1500,height=250, highlightthickness=0)

    head_to_dpt.place(x=250,y=140)
    head_to_dpt.create_line(670,0,670,110,width=10)
    head_to_dpt.create_line(180,110,1230,110,width=10)   # 1200 to match with 5th box

    horizental_gap=180

    for i in range(4):   # loop = total number of departments
        head_to_dpt.create_line(horizental_gap,105,horizental_gap,250,arrowshape=(16,20,6),width=10,arrow=LAST)
        horizental_gap+=350
def cc3(root):  #  head to departments
    head_to_dpt=Canvas(root,width=1500,height=250, highlightthickness=0)

    head_to_dpt.place(x=250,y=140)
    head_to_dpt.create_line(670,0,670,110,width=10)
    head_to_dpt.create_line(180,110,1075,110,width=10)   # 1200 to match with 5th box

    horizental_gap=180

    for i in range(3):   # loop = total number of departments
        head_to_dpt.create_line(horizental_gap,105,horizental_gap,250,arrowshape=(16,20,6),width=10,arrow=LAST)
        horizental_gap+=450

def cc2(root):  #  head to departments
    head_to_dpt=Canvas(root,width=1500,height=250, highlightthickness=0)

    head_to_dpt.place(x=250,y=140)
    head_to_dpt.create_line(670,0,670,110,width=10)
    head_to_dpt.create_line(380,110,930,110,width=10)   # 1200 to match with 5th box

    horizental_gap=380

    for i in range(2):   # loop = total number of departments
        head_to_dpt.create_line(horizental_gap,105,horizental_gap,250,arrowshape=(16,20,6),width=10,arrow=LAST)
        horizental_gap+=550

def cc1(root):  #  head to departments
    head_to_dpt=Canvas(root,width=1500,height=250, highlightthickness=0)

    head_to_dpt.place(x=250,y=140)
    head_to_dpt.create_line(655,10,655,220,arrowshape=(16,20,6),width=10,arrow=LAST)

        
def Constucting_Orgranizational_Structure():
    starting_point_X = 0
    starting_point_Y = 0
    ending_point_X =0
    ending_point_Y = 0
    New_window = Tk()
    j = 1
    row = 600
    row1 = row
    column = 100
    column2 = 0
   
    New_window.geometry("2000x2000")
    length = len(Head_and_Department_Name_list)
    print(length)
    for i in Head_and_Department_Name_list:
        if (j == 1):
            Label_1 = Label(New_window,text = i.get(),fg = "blue",font = "Arial 20",bg ="black",width = 40)
          
            Label_1.place(x = row,y = column)
            row  = 0
            j = j +1
            starting_point_X = row - 100
            starting_point_Y = column
            
            
            
            #ertyfgulihgfdsd
                
                
        else:
            Label_1 = Label(New_window,text = i.get(),fg = "blue",font = "Arial 20",bg ="black",width =10)
            if (length == 2):
                column = 400
                row = 820
                j = j + 1
            
            if (length ==3):
                print("I am in")
                column = 400
                row = row+ 550
              
            if (length == 4):
                column = 400
                row = row + 400
            
            if (length == 5):
                column = 400
                row = row + 350
            if (length == 6):
                column = 400
                row = row + 300
                
                
            column2 = column
            Label_3 = Label(New_window,text ="|", fg = "blue",bg = "black",font = "Times 30 bold")
            Label_3.place(x=row+75,y =column-60)
            Label_1.place(x = row,y = column)
            Label_3 = Label(New_window,text ="|", fg = "blue",bg = "black",font = "Times 30 bold")
            Label_3.place(x=row+75,y =column+40)
            for k in Department_Member_Name:
                Label_2 = Label(New_window,text = k.get(),fg = "Blue",bg = "black",font = "Arial 20",width =10)
                print (row)
                Label_3 = Label(New_window,text ="|", fg = "blue",bg = "black",font = "Times 20 bold")
                Label_3.place(x=row+75,y =column2+40)
                column2 = column2 + 100
                Label_2.place(x = row,y = column2)
    if (length == 6):  
        cc5(New_window)
    if (length == 5):  
        cc4(New_window)
    if (length == 4):  
        cc3(New_window)
    if (length == 3):
        cc2(New_window)
    if (length == 2):
        cc1(New_window)
    New_window.mainloop()
def Sub_Divisional_Member():
    New_window = Tk()
    
    Listing = ["Head Of Department Name","Department's Manager Name","Department Employees"]
    New_window.geometry("900x900")
    i = 0
    for i in range(0,3):
        
        Label_1 = Label (New_window,text =Listing[i],font = "Times 15")
        entry_Name = Entry(New_window,width = 50)
        Label_1.pack(padx =5,pady = 10)
        entry_Name.pack(ipady=3)
        Department_Member_Name.append(entry_Name)
    
    button1 = Button(New_window,text= "Submit",fg = "blue",font = "Arial 15 bold",width = 10,height =1,bg = "Black",command = Constucting_Orgranizational_Structure)
    button1.pack(padx =5,pady = 10) 
    button2 = Button(New_window,text= "Quit",fg = "blue",font = "Arial 15 bold",width = 10,height =1,bg = "Black",command = New_window.destroy)
    #inserting on the Stack    
    button2.pack()
    New_window.mainloop()
    
    
from tkinter import * 
def Department_Name(vara):
    Department_Frame = Tk()
    
    Department_Frame.geometry("900x900")
    i = 0
    Name = Label(Department_Frame,text = "Organizational Structure",fg = "Blue",font = "Times 50",width = 100)
    Name.pack()
    if (vara == "One"):
        Looping_vara = 2
    if (vara == "Two"):
        Looping_vara = 3
    if (vara == "Three"):
        Looping_vara = 4
    if (vara == "Four"):
        Looping_vara = 5
    if (vara == "Five"):
        Looping_vara = 6
    listing = ["Head of Organization","1st Department Name","2nd Department Name","3rd Department Name","4th Department Name","5th Department Name"]
    
    while( i < Looping_vara):
        Label_1 = Label (Department_Frame,text =listing[i],font = "Times 15")
        entry_Name = Entry(Department_Frame,width = 50)
        Label_1.pack()
        entry_Name.pack(ipady=3)
        Head_and_Department_Name_list.append(entry_Name)
        i = i + 1
        
    button1 = Button(Department_Frame,text= "Submit",fg = "blue",font = "Arial 15 bold",width = 10,height =1,bg = "Black",command =Sub_Divisional_Member)
    button1.pack(padx =5,pady = 10) 
    button2 = Button(Department_Frame,text= "Quit",fg = "blue",font = "Arial 15 bold",width = 10,height =1,bg = "Black",command = Department_Frame.destroy)
    #inserting on the Stack    
    button2.pack()
    
    
    Department_Frame.mainloop()
    
from tkinter import * #http://localhost:8888/notebooks/Documents/Untitled.ipynb?kernel_name=python2#

def new_function():
    newtop = Tk()
    
    newtop.geometry("700x700")
    Name = Label(newtop,text = "Select Number of Department", fg = "silver",font = "Times 40 underline bold ",width = 80)
    Name.pack()
    
    One= IntVar()
    Checkbutton(newtop,text = "One ",variable =One,font = "Times 30 italic bold",command =lambda:Department_Name("One")).pack()
    Two = IntVar()
    Checkbutton(newtop,text = "Two ",variable = Two,font = "Times 30 italic bold",command =lambda:Department_Name("Two")).pack()
    Three = IntVar()
    Checkbutton(newtop,text = "Three ",variable = Three,font = "Times 30 italic bold",command =lambda:Department_Name("Three")).pack()
    Four = IntVar()
    Checkbutton(newtop,text = "Four",variable = Four,font = "Times 30 italic bold",command =lambda:Department_Name("Four")).pack()
    Five = IntVar()
    Checkbutton(newtop,text = "Five",variable = Five,font = "Times 30 italic bold",command =lambda:Department_Name("Five")).pack()
    
    button1 = Button(newtop,text= "Back",fg = "blue",font = "Arial 15 bold",width = 10,height = 2,bg = "gray")#command =Submit_button )
    button1.pack(padx =5,pady = 10)
    button2 = Button(newtop,text= "Quit",fg = "blue",font = "Arial 15 bold",width = 10,height = 2,bg = "gray",command = newtop.destroy)
    #inserting on the Stack    
    button1.pack(padx =5,pady = 10)
    button2.pack()
    
    newtop.mainloop()
    
new_function()    
