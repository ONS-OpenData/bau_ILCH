# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:48:22 2015

@author: Mike
"""

import tkFileDialog
import Tkinter as tk


def get_file1():
    global file1 
    path = tkFileDialog.askopenfilename(filetypes=[("Excel Spreadsheet","*.xls")])
    file1.set(path)    
        
def run():
    runfiles(file1.get())

def runfiles(source):
    
    import shutil
    import os    

    # Get the directory of the selected file
    # Compare length with both \ and / to cover possible other os use
    filepath = source[: source.rfind('\\')]
    if len(source[: source.rfind('/')]) < len(filepath):
        filepath = source[: source.rfind('/')]
    filepath = filepath.replace('/', '\\')    # Swap / for \ so we can compare the two

    # Compare the current working directory with the above.
    # If its the same, we dont want to move or split anything - the files already in the working directory!
    if filepath != os.getcwd():    
        shutil.move(source, os.getcwd())    
    
    # now get the name out of it    

    filename = source.split('/')
    filename = filename[len(filename)-1]
    filename = '"' + filename + '"'

    """
    Now the flename is sorted. This part is just bulding a list of commands, then executing them
    """
    linestolaunch = []
    
    linestolaunch.append('bake --preview ILCH.py ' + filename + ' growth')
    linestolaunch.append('bake --preview ILCH.py ' + filename + ' "level -"')
    
    # Take the quotes back off
    filename = filename[1:-1]  
    
    #Get rid of file extension
    filename = filename[:-4]
    
    linestolaunch.append('python transform_ILCH.py "data-' + filename + '-ILCH-growth.csv"')
    linestolaunch.append('python transform_ILCH.py "data-' + filename + '-ILCH-level -.csv"')
    
    
    import subprocess as sp     
    for each in linestolaunch:
                p = sp.Popen(each, shell=True) #, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                p.communicate()

    print ''    
    print ''
    print '*************'
    print 'NOTE:'
    print ''
    print 'Warnings about "Couldnt identify date! ... etc" are expected.'
    print 'Its messy but otherwise fine.'
    print ''
    print 'Processing Complete. Either select another file of close this window to exit.'
    print ''
    
    
    
"""
THE FOLLOWING CODE IS JUST FOR THE GUI
"""
            
root = tk.Tk()
file1 = tk.StringVar()

description = 'TRANSFORM TOOL - Index of Labout Costs per Hour, V1.0'
label = tk.Label(root, text=description)
label.pack()

description = 'INFO - Select either the NSA or the SA file to continue.You WILL get date warnings during extraction, its fine'
label = tk.Label(root, text=description)
label.pack()

tk.Button(text='Select Source File', command=get_file1).pack()
tk.Label(root, textvariable=file1).pack()

tk.Button(text='Databake, Transform & Validates Files', command=run).pack()
# tk.Button(text='Compare', command=convert).pack()
root.mainloop()



