#USE CTRL + K + C TO COMMENT MULTIPLE LINES
#USE CTRL + K + U TO UNCOMMENT MULTIPLE LINES
# #Miles --> km converter
# import tkinter as tk #importing tkinter with the abbreviation tk for convinience
# from tkinter import ttk #classes for themed widgets
# #import ttkbootstrap as ttk

# def convert():
#     mile_input = entry_int.get() #getting the value inputed by user and stroing in variable
#     km_output = mile_input * 1.61 #coverting the miles to km by multiplying by 1.61
#     output_string.set(km_output) #set value of the string

# #window
# window = tk.Tk() #creates a window #use ttk.Window(themename = 'darkly')) w/ttkbootstrap
# window.title('Demo') #window name
# window.geometry('300x150') #window size

# #title
# title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold') #creates title label
# title_label.pack() #packs label onto screen

# #input field
# input_frame = ttk.Frame(master = window) #input box
# entry_int = tk.IntVar() #store and update values
# entry = ttk.Entry(master = input_frame, textvariable = entry_int) #enter into input box
# button = ttk.Button(master = input_frame, text = 'Convert', command = convert) #makes button, uses convert function created above
# entry.pack(side = 'left', padx = 10) #packs box with padding
# button.pack(side = 'left')
# input_frame.pack(pady = 10) #packs input frame with padding

# #output
# output_string = tk.StringVar()
# output_label = ttk.Label(
#     master = window,
#     text = 'Output',
#     font = 'Calibri 24',
#     textvariable = output_string) #output label
# output_label.pack(pady = 5) #pack and pad

# #run
# window.mainloop() #run the window

# import tkinter as tk
# from tkinter import ttk

# def button_func():
#     print('a button was pressed')

# def button_func2():
#     print('hello')

# #create a window
# window = tk.Tk()
# window.title('Window and Widgets')
# window.geometry('800x500')

# #ttk widgets
# label = ttk.Label(master = window, text = 'This is a test')
# label.pack()

# #create widgets
# text = tk.Text(master = window) #create a widget on the window in the variable text
# text.pack() #pack/place the widget onto the screen

# #ttk entry
# entry = ttk.Entry(master = window)
# entry.pack()

# label2 = ttk.Label(master = window, text = 'my label')
# label2.pack()

# #ttk button
# button = ttk.Button(master = window, text = 'A button', command = button_func) #pressing the button calls the function, putting button_func() would call it regardless
# button.pack()

# #button2 = ttk.Button(master = window, text = 'button2', command = button_func2)
# button2 = ttk.Button(master = window, text = 'button2', command = lambda:print('hello'))
# button2.pack()

# #run
# window.mainloop() #updates the gui, checks for events

# #First pack() coded places above all the other, then the next gets packed, and so on

# import tkinter as tk
# from tkinter import ttk

# def button_func():
#     #print(entry.get()) #get the content of entry
#     entry_text = entry.get() #gets the thing typed in entry box
#     entry['state'] = 'disabled' #disables the entry

#     #update the label
#     #label.config(text = 'Some other text') #this line and the one below do the same thing
#     label['text'] = entry_text #'Some other text'

# def button2_func():
#     label['text'] = 'Some text' #changes label to 'some text'
#     entry['state'] = 'enabled' #enables the entry box

# #window
# window = tk.Tk()
# window.title('Getting and setting widgets')

# #widgets
# label = ttk.Label(master = window, text = 'Some text')
# label.pack()

# entry = ttk.Entry(master = window)
# entry.pack()

# button = ttk.Button(master = window, text = 'The button', command = button_func)
# button.pack()

# button2 = ttk.Button(master = window, text = 'Button 2', command = button2_func)
# button2.pack()

# #run
# window.mainloop()

# import tkinter as tk
# from tkinter import ttk

# def button_func():
#     print(string_var.get()) #gets the thing from the string
#     string_var.set('Button pressed') #resets the string to the woeds 'Button pressed'

# #window
# window = tk.Tk()
# window.title('Tkinter Variables')

# #tkinter variable
# string_var = tk.StringVar() #can pass argument value to have something start in there

# #widgets
# label = ttk.Label(master = window, text = 'label', textvariable = string_var)
# label.pack()

# entry = ttk.Entry(master = window, textvariable = string_var)
# entry.pack()

# entry2 = ttk.Entry(master = window, textvariable = string_var) #entry 1, entry 2 and the label are all connected by the variable
# entry2.pack()

# button = ttk.Button(master = window, text = 'Button', command = button_func)
# button.pack()

# string_var2 = tk.StringVar(value = 'test')

# entry3 = ttk.Entry(master = window, textvariable = string_var2)
# entry3.pack()
# entry4 = ttk.Entry(master = window, textvariable = string_var2)
# entry4.pack()
# label2 = ttk.Label(master = window, textvariable = string_var2)
# label2.pack()

# #run
# window.mainloop()

import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#button
def button_func():
    print('A basic button')
    
def button_func2():
    print(radio_var.get())

button_string = tk.StringVar(value = 'A simple button with string var')
button = ttk.Button(window, text = 'Simple button', command = button_func, textvariable = button_string)
button.pack()

#checkbutton
check_var = tk.IntVar(value = 10) #or BooleanVar() #value = 10 sets it to on, as the onvalue is 10
check = ttk.Checkbutton(window,
                        text = 'Checkbox 1',
                        command = lambda: print(check_var.get()), #gets value stored in check_var and prints in the terminal
                        variable = check_var, #puts variavle into button
                        onvalue = 10, #sets on value to 10 instead of 1
                        offvalue = 5) #sets off value to 5 instead of 0
check.pack()

check2 = ttk.Checkbutton(window,
                         text = 'Checkbox 2',
                         command = lambda: print('test'))
check2.pack()

#radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window,
                         text = 'Radiobutton 1',
                         value = 'radio 1',
                         variable = radio_var,
                         command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window,
                         text = 'Radiobutton 2',
                         value = 2,
                         variable = radio_var,
                         command = button_func2)
radio2.pack()

#run
window.mainloop()

#1:12:00