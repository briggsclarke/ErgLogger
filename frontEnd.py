#Author: Briggs Clarke 
#Front end code for Erg Logger. Intakes data and passes to read.py

import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Enter your distance (m), average split (x:xx.x), spm(xx), and time(x:xx.xx):")
label.pack()

totalDistEntry = tk.Entry(fg='black', bg='white', width=50)
totalDistEntry.pack()
aveSplitEntry = tk.Entry(fg="black", bg="white", width=50)
aveSplitEntry.pack()
spmEntry = tk.Entry(fg='black', bg='white', width=50)
spmEntry.pack()
timeEntry = tk.Entry(fg='black', bg='white', width=50)
timeEntry.pack()



aveSplit = aveSplitEntry.get()
spm = spmEntry.get()
totalDist = totalDistEntry.get()
time = timeEntry.get()

window.mainloop()