import tkinter as tk
from tkinter import ttk
import os
import PIL.Image as img
from tkinter import *
import time

# Clear all fields function for Clear button
def clear_fields():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    progress_var.set(0)
    result_label.config(text="")

# Exit the app function for Quit Button
def exit_app():
    root.destroy()

# Create Convert folder in folder input URL
def create_folder(url):
    folder_path = url+"/convert"
    os.mkdir(folder_path)
    return folder_path

# Progress convert Image file function for Convert Button
def convert_file():
    format_file = str(entry_a.get())
    url = str(entry_b.get())
    quality = int(entry_c.get())

    folder_path = create_folder(url)
    count=1
    for i in os.listdir(url):
        if os.path.isfile(url+"/"+i):
            image = img.open(url+"/"+i)
            image = image.convert('RGB')
            image.save(folder_path+"/"+i.split(".")[0]+"."+ format_file,optimize = True, quality = quality) #100%

        # progress bar run
        progress_var.set(count/len(os.listdir(url))*100)
        root.update_idletasks()
        time.sleep(0.02)
        count+=1

    result_label.config(text="Convert successfully !")
   
# Creare the application
root = tk.Tk()
root.geometry("400x240")
root.title("Convert file")

label_a = tk.Label(root, text="Enter format file: (ex: JPG, PNG, WEBP,...)").pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Enter folder URL:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

label_c = tk.Label(root, text="Enter optimized quality : (ex: 60, 70, 80,..)").pack()
entry_c = tk.Entry(root)
entry_c.pack()

label_processing = tk.Label(root, text="Processing ...").pack()
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, length=200, mode="determinate")
progress_bar.pack()

panel1=Frame(root)
panel1.pack(fill = BOTH, expand = True)

solve_button = tk.Button(panel1, text="Convert", command= convert_file)
solve_button.pack(side=tk.LEFT, expand = True)

clear_button = tk.Button(panel1, text="Clear", command=clear_fields)
clear_button.pack(side=tk.LEFT, expand = True)
exit_button = tk.Button(panel1, text="Quit", command=exit_app)
exit_button.pack(side=tk.LEFT, expand = True)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()