import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win64':
    base = "Win64GUI"
6
os.environ['TCL_LIBRARY'] = r"C:\Users\sssss7j\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\sssss7j\AppData\Local\Programs\Python\Python310\tcl\tk8.6"
executables = [cx_Freeze.Executable("TextEditor.py", base=base, icon="notepad.ico")]


cx_Freeze.setup(
    name = "Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["notepad.ico",'tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "1.0",
    description = "Tkinter Application",
    executables = executables
    )
