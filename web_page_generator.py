
import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # Button for generating the default HTML text
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=2, padx=(10,10) , pady=(10,10))

        # Button for submitting the custom text
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(row=2, column=1, padx=(10,10) , pady=(10,10))

        # Creates entry for source for custom text entry
        self.source_dir = Entry(width=100)
        # Positions entry in GUI using tkinter grid()
        self.source_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        # Label text for the custom text entry box
        self.lblText = Label(self.master, text= 'Enter custom text or click the Default HTML page button')
        self.lblText.grid(row=0, column=0, columnspan=2, padx=(30,0), pady=(30,0))  


    # Function for the default HTML text
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<bady>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # Function for custom text
    def customHTML(self):
        # Get the text from the Entry widget
        htmlText = self.source_dir.get()
        
        # Write the text to the HTML file
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        
        # Open the generated HTML file in a web browser
        webbrowser.open_new_tab("index.html")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

    
