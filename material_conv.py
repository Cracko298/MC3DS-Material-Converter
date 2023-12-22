import os, sys, ctypes, easygui
from time import sleep

# Open the file dialog
files = ["material", "material3DS", "images", "bak", "dat"]
filestypes = ["*.material", "*.material3DS", "*.mat", "*.bak", "*.dat"]
file_path = easygui.fileopenbox(default="*.images", filetypes=filestypes)

filename = os.path.basename(file_path)
f0, f1 = filename.split('.')

if f1 not in files:
    print(f"WARNING: If you procede with this file. It may cause an error that could result in a Corrupted File.")
    print(f"File extentions that are allowed/expected are as follows: {files}.\n")
    print(f"Press the 'Enter Key' to close the Application.")
    print(f"Press the '0 Key' then press the 'Enter Key' to continue with the selected file.\n")

    u_inpt = input("Press the Corrisponding Key(s) to Procede: ")

    if u_inpt == "":
        sys.exit(1)
    
    elif u_inpt == "0":
        pass

    else:
        print("\nNo Valid response recieved, closing Application to avoid a potential Error.")
        sleep(2)
        sys.exit(1)

else:
    pass

parts = filename.split('.')
out_file = '.'.join(parts[:-1]) + ".json"

with open(file_path,'rb+') as f:
    with open(out_file,'wb') as o:
        dats = f.read()
        data = dats[::-1]
        writable_d = data[::-1]

        o.write(writable_d)