import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import time
from tkinter import messagebox


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        # Sets title of GUI window
        self.master.title("File Transfer")
          
        # Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        # Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        # Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        # Positions entry in GUI using tkinter grid()
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        # Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        # Positions destination button in GUI using tkinter grid()
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        # Creates entry for destination directory selection
        self.dest_dir = Entry(width=75)
        # Positions entry in GUI using tkinter grid()
        self.dest_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        # Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        # Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        # Creates an Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        # Positions the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

        #Creates a check files button
        self.check_files_btn = Button(text="Check Recent Files", width=20, command=self.check_recent_files)
        #positioning for the check files button
        self.check_files_btn.grid(row=3, column=1, padx=(200, 0), pady=(0, 15))



    # Creates method to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # Clear any existing content in the Entry widget
        self.source_dir.delete(0, END)
        # Insert the selected path into the Entry widget
        self.source_dir.insert(0, selectSourceDir)

    # Creates method to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        # Clear existing text
        self.dest_dir.delete(0, END)
        # Insert new text
        self.dest_dir.insert(0, selectDestDir)

    # Creates function to transfer files from one directory to another
    def transferFiles(self):
        # Gets source directory
        source = self.source_dir.get()
        # Gets destination directory
        destination = self.dest_dir.get()
        # Gets a list of files in the source directory
        source_files = os.listdir(source)
        # Runs through each file in the source directory
        for i in source_files:
            # Moves each file from the source to the destination
            shutil.move(os.path.join(source, i), destination)
            print(f'{i} was successfully transferred.')

    # Function to check recent files and if they have been modified within the last 24 hours
    def check_recent_files(self):
        directory = self.source_dir.get()  # Access source directory from the Entry widget
        if not directory:
            messagebox.showerror("Error", "Please select a source directory.")
            return
        
        #importing time and setting up the 24 parameter 
        import time
        now = time.time()
        one_day_ago = now - 24 * 60 * 60
        recent_files = []
        
        # Try if and else block for the recent files
        try:
            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)
                if os.path.isfile(filepath):
                    file_modified_time = os.path.getmtime(filepath)
                    if file_modified_time > one_day_ago:
                        recent_files.append(f"{filename} (Modified: {time.ctime(file_modified_time)})")

            if recent_files:
                messagebox.showinfo("Recent Files", "\n".join(recent_files))
            else:
                messagebox.showinfo("Recent Files", "No files modified in the last 24 hours.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


        
    # Creates function to exit program
    def exit_program(self):
        # Terminates the main GUI loop
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()



