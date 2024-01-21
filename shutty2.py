import customtkinter as ctk
import os
import subprocess


def shutDown(time):
	
    if time < 1:
        time = 1
    command = "shutdown -s -t {x}".format(x = time*60)
    os.system('{command}'.format(command = command))
    print("shutdown in {X} minuten".format(X = time))




def canceled():
    os.system('"shutdown -a"')
    print("canceled")
    
def generateArray(number):
    ary = ["Zeit..."]
    for i in range(1, number):
        ary.append("{x}".format(x = i))
        
    return ary
    
maxTime = 480

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Shutdown Program Reloaded")
root.geometry("650x450")

    
currentVal = ctk.IntVar() 
currentStr = ctk.StringVar()

    
def get_current_value():
    return '{: .2f}'.format(currentVal.get())


def slider_changed(event):
    number.configure(text=get_current_value())
    

frame = ctk.CTkFrame(master= root)
frame.pack(pady = 12, padx = 10)
    

tabView = ctk.CTkTabview(master= frame)
tabView.grid(pady= 20, padx = 60, sticky="nsew")
tabView.add("DropListe")
tabView.add("Slider")
tabView.add("manueller Input")

dropListFrame = ctk.CTkFrame(master=tabView.tab("DropListe"))
dropListFrame.pack(pady= 20, padx = 60, fill="both", expand=True)
dropListFrame.grid_rowconfigure(0, weight = 1)
dropListFrame.grid_columnconfigure((0, 3), weight = 1)

label1 = ctk.CTkLabel( master = dropListFrame, text = "Wann soll der PC ausgemacht werden?")
label1.grid(pady = 12, padx = 10, columnspan=4)


droplist = ctk.CTkComboBox(master=dropListFrame, values=generateArray(maxTime) ,variable=currentStr)
droplist.grid(row = 1, pady = 12, padx = 10, columnspan=4)




start1 = ctk.CTkButton(dropListFrame, command= lambda : shutDown(int(currentStr.get())), text="start")
cancel1 = ctk.CTkButton(dropListFrame, command=canceled, text="Cancel")


start1.grid(pady=12, padx=10, row = 2, column = 0, columnspan = 2,  sticky = "ew")
cancel1.grid(pady = 12, padx = 10, row = 2, column = 3, columnspan = 2, sticky = "ew")




SliderFrame = ctk.CTkFrame(master=tabView.tab("Slider"))
SliderFrame.pack(pady= 20, padx = 60, fill="both", expand=True)
SliderFrame.grid_rowconfigure(0, weight = 1)
SliderFrame.grid_columnconfigure((0, 3), weight = 1)

label2 = ctk.CTkLabel( master = SliderFrame, text = "Wann soll der PC ausgemacht werden?")
label2.grid(row = 0, pady = 12, padx = 10, columnspan=2)


slider = ctk.CTkSlider(master=SliderFrame, from_= 0, to= 480, number_of_steps = maxTime, command = slider_changed, variable=currentVal)
slider.grid(pady = 12, padx = 10, row = 1, column = 0, columnspan = 2, sticky = "ew")

slider.set(0)




number = ctk.CTkLabel(master= SliderFrame, text= get_current_value())
number.grid(column = 3, row = 1, pady = 12, padx = 10)


start2 = ctk.CTkButton(SliderFrame, command= lambda : shutDown(currentVal.get()), text="start")
cancel2 = ctk.CTkButton(SliderFrame, command=canceled, text="Cancel")


start2.grid(pady=12, padx=10, row = 2, column = 0, sticky = "ew")
cancel2.grid(pady = 12, padx = 10, row = 2, column = 1, sticky = "ew")




manFrame = ctk.CTkFrame(master=tabView.tab("manueller Input"))
manFrame.pack(pady= 20, padx = 60, fill="both", expand=True)
manFrame.grid_rowconfigure(0, weight = 1)
manFrame.grid_columnconfigure((0, 3), weight = 1)

label3 = ctk.CTkLabel( master = manFrame, text = "Wann soll der PC ausgemacht werden?")
label3.grid(pady = 12, padx = 10, columnspan=2)

textfield = ctk.CTkEntry(master=manFrame, placeholder_text="Zeit...")
textfield.grid(pady = 12, padx = 10, row = 1, columnspan = 2)




start3 = ctk.CTkButton(manFrame, command= lambda : shutDown(int(textfield.get())), text="start")
cancel3 = ctk.CTkButton(manFrame, command=canceled, text="Cancel")


start3.grid(pady=12, padx=10, row = 2, column = 0, sticky = "ew")
cancel3.grid(pady = 12, padx = 10, row = 2, column = 1, sticky = "ew")



#checkBox = ctk.CTkCheckBox(master=frame, text="enable Settings")
#checkBox.grid(pady = 12, padx = 10)

#maxValueSetting = ctk.CTkEntry(master= frame, state = "disabled", placeholder_text="max number", textvariable=ctk.StringVar(value="480"))
#maxValueSetting.grid(pady = 12, padx = 10)



#checkBox.configure(command=lambda: maxValueSetting.configure(state="disabled") if checkBox.get() == 0 else maxValueSetting.configure(state="normal"))



root.mainloop()