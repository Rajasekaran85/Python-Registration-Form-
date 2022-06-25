import os
from tkinter import *
from tkinter import messagebox
from csv import *
from tkcalendar import Calendar, DateEntry


'''
Data Entry Pallet created using tkinter package
User should enter the data employee wise and finally click the submit
All the User entered data will append into the CSV
tkinter background images "bg.png" should copy into the tool location

Employee Details: Employee ID, Employee Name, Department, Employee Desigination, Branch, Mobile Number, Active Status, Date of Birth, Date of Joining.
Employee ID, Employee Name, Desigination, Mobile Number = Keying Entry
Department, Branch = Drop Down Values
Active Status = Checkbox
Date of Birth & Joining = Select the Date from the date picker pallet
'''

# Defining the module size
window=Tk()
window.geometry("900x700+10+10")
window.title("Data Entry Module")  # title of the module

#window backgroung image, image format png
backgroundimg = "bg.png"
bgimg = PhotoImage(file=backgroundimg)

label1 = Label(window, image = bgimg)  # placing the background image in the data entry module
label1.place(x = 0, y = 0)


main_lst=[]


options = [
    "Operations",
    "R&D",
    "Software",
    "QA",
    "HR",
    "Admin",
]

ben = [
    "Bangalore",
    "Chennai",
    "Kanchi",
    "Madurai",
]


clicked1 = StringVar()   # Store the department string value
clicked2 = StringVar()   # Store the branch string value

val1 = StringVar()       # Store the active field string value

val1.set("yes")

clicked1.set( "Select" )  # set the default value
clicked2.set( "Select" )

#Get the csv file path from user
csvfilepath = input(" Enter the File path: ") + "\\" + "Employee_details.csv"


# add function for getting the values from user and store to the lst variable
'''
before adding to the lst variable, check the user entered value is valid or not
Validations:
empty field not allowed
ID & Mobile Number should be numeric value
ID number should be minimum 4 digit
Mobile Number should be 10 digit
'''
def Add():
	idvalue = empid_t.get("1.0",'end-1c')
	message = ""
	if idvalue == "":
		message = "Employee ID"
		messagebox.showerror(message, "Enter the Employee ID Value")
		return
	else:
		if not idvalue.isdigit():
			message = "Employee ID"
			messagebox.showerror(message, "Employee ID must be digit value")
			return
		elif len(idvalue) <= 3:
			message = "Employee ID"
			messagebox.showerror(message, "Employee ID - minimum 4 digit")
			return


	namevalue = empname_t.get("1.0",'end-1c')
	if namevalue == "":
		message = "Employee Name"
		messagebox.showerror(message, "Enter the Employee Name Value")
		return

	deptvalue = clicked1.get()
	defvalue = "Select"
	if deptvalue == defvalue:
		message = "Department"
		messagebox.showerror(message, "Select the Department Value")
		return


	desvalue = empdes_t.get("1.0",'end-1c')
	if desvalue == "":
		message = "Desigination"
		messagebox.showerror(message, "Enter the Desigination Value")
		return

	locvalue = clicked2.get()
	if locvalue == defvalue:
		message = "Branch"
		messagebox.showerror(message, "Select the Branch Value")
		return

	mobvalue = empmob_t.get("1.0",'end-1c')
	if mobvalue == "":
		message = "Mobile Number"
		messagebox.showerror(message, "Enter the Mobile Number")
		return
	else:
		if not mobvalue.isdigit():
			message = "Mobile Number"
			messagebox.showerror(message, "Mobile Number must be digit value")
			return
		elif len(mobvalue) <= 9:
			message = "Mobile Number"
			messagebox.showerror(message, "Mobile Number - 10 digit")
			return

	main_lst=[empid_t.get("1.0",'end-1c'),empname_t.get("1.0",'end-1c'),clicked1.get(),empdes_t.get("1.0",'end-1c'),clicked2.get(),empmob_t.get("1.0",'end-1c'),val1.get(),empdob_t.get(),empdoj_t.get()]
	print(main_lst)




	'''
	Added fields will write to the csv file
	List the CSV Header in the "headerList" variable
	create the csv file
	get the header values using "DictWriter" and store in the dw variable
	If Conditions: csv file size is zero then write the header values, otherwise write only the user entered data.
	'''
	with open(csvfilepath, "a") as csvfile:
		headerList = ["Employee ID","Employee Name","Department","Employee Desigination","Branch","Mobile Number","Active Status","Date of Birth","Date of Joining"]
		csvvalue = writer(csvfile)
		dw = DictWriter(csvfile, delimiter=',', fieldnames=headerList)
		file_is_empty = os.stat(csvfilepath).st_size == 0
		if file_is_empty:
			dw.writeheader()
		csvvalue.writerow(main_lst)
		messagebox.showinfo("Information","Saved succesfully")

	Clear()

def Clear():
	empid_t.delete("1.0","end")         # for clearing the text widget values use 1.0 to end
	empname_t.delete("1.0","end")
	empdes_t.delete("1.0","end")
	clicked1.set( "Select" )
	clicked2.set( "Select" )
	val1.set("yes")
	empmob_t.delete("1.0","end")
	empdob_t.delete(0,"end")            # for clearing the date value use use 0 to end...
	empdoj_t.delete(0,"end")







# Fields options in the Tkinter application

empdet=Label(window, text='Employee Details', font='helvetica 15', bg='#b3ecff')
empdet.place(x=50, y=50)
empid=Label(window, text='Employee ID', font='Calbri 12', bg='#b3ecff')
empid.place(x=50, y=120)
empid_t=Text(window, height=1.5, width=25, font=("Courier", 12))
empid_t.place(x=180, y=120)

empname=Label(window, text='Employee Name', font='Calbri 12', bg='#b3ecff')
empname.place(x=50, y=170)
empname_t=Text(window, height=1.5, width=25, font=("Courier", 12))
empname_t.place(x=180, y=170)

empdept=Label(window, text='Department', font='Calbri 12', bg='#b3ecff')
empdept.place(x=50, y=220)

empdept_t=OptionMenu(window, clicked1, *options)
empdept_t.pack()
empdept_t.place(x=180, y=220)



empdes=Label(window, text='Desgination', font='Calbri 12', bg='#b3ecff')
empdes.place(x=50, y=270)
empdes_t=Text(window, height=1.5, width=25, font=("Courier", 12))
empdes_t.place(x=180, y=270)


emploc=Label(window, text='Branch', font='Calbri 12', bg='#b3ecff')
emploc.place(x=50, y=320)
emploc=OptionMenu(window, clicked2, *ben)
emploc.pack()
emploc.place(x=180, y=320)


empmob=Label(window, text='Mobile Number', font='Calbri 12', bg='#b3ecff')
empmob.place(x=50, y=370)
empmob_t=Text(window, height=1.5, width=25, font=("Courier", 12))
empmob_t.place(x=180, y=370)



empstatus=Label(window, text='Status', font='Calbri 12', bg='#b3ecff')
empstatus.place(x=50, y=430)

empstatus1=Checkbutton(window, text = "Active", font='Calbri 12', variable=val1, onvalue="yes", offvalue="no")
empstatus1.place(x=180, y=430)


empdob=Label(window, text='Date of Birth', font='Calbri 12', bg='#b3ecff')
empdob.place(x=50, y=490)
empdob_t=DateEntry(window, height=5, width=16, background="magenta3", foreground="white",bd=2,year=2000,month=1,date=1, date_pattern="dd-mm-y")
empdob_t.place(x=180, y=490)


empdoj=Label(window, text='Date of Join', font='Calbri 12', bg='#b3ecff')
empdoj.place(x=400, y=490)
empdoj_t=DateEntry(window, width=16, background="magenta3", foreground="white",bd=2, date_pattern="dd-mm-y")
empdoj_t.place(x=550, y=490)

add=Button(window,text="Submit", font='Calbri 12', padx=20, pady=10, command=Add, bg='#40ff00')
add.place(x=120, y=630)


empclear=Button(window, text='Clear', font='Calbri 12', padx=20, pady=10, command=Clear, bg='#4d88ff')
empclear.place(x=240, y=630)

Exit=Button(window, text="Exit", font='Calbri 12', padx=20, pady=10, command=window.quit, bg='#ff6666')
Exit.place(x=350, y=630)

window.mainloop()
