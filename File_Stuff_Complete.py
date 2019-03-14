import tkinter as tk
import tkinter.filedialog as fdialog
from tkinter.constants import YES, BOTH
from tkinter import messagebox as dia
from tkinter import simpledialog as qa
import tkinter.font as tkFont
import sys
from tkinter import ttk
try:
    import win32print
    printFunc=True
except:
    printFunc=False


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.i=1
    def quitc(self, event):
        print("quitting...")
        sys.exit(0)
    def installed_Printers(self):
        printers = win32print.EnumPrinters(2)
        print(type(printers))
        return printers
    def ope(self):
        self.wipe()
        try:
            self.file=fdialog.askopenfilename(filetypes=(("Default Files","*.dimitritxt"),("All Files","*.*")) )
            with open(self.file,"r") as f:
                self.text=f.read()
                print(self.text)
                s=self.text.split(",")
                font=s[1].split(":")
                size=s[2].split(":")
                font=font[1]
                size=size[1]
                self.meta=self.text
                self.Font["family"]=font
                self.Font["size"]=int(size)
                act=s[3].split("::")
                self.result.insert("1.0",act[1])
        except:
            dia.showwarning("Error!","No file loaded. Have you loaded a file?")
        self.master.title("text editor          "+self.file)
    def opes(self,event):
        self.wipe()
        try:
            self.file=fdialog.askopenfilename(filetypes=(("Default Files","*.dimitritxt"),("All Files","*.*")) )
            with open(self.file,"r") as f:
                self.text=f.read()
                print(self.text)
                s=self.text.split(",")
                font=s[1].split(":")
                size=s[2].split(":")
                font=font[1]
                size=size[1]
                self.meta=self.text
                self.Font["family"]=font
                self.Font["size"]=int(size)
                act=s[3].split("::")
                self.result.insert("1.0",act[1])
        except:
           dia.showwarning("Error!","No file loaded. Have you loaded a file?")
        self.master.title("text editor          "+self.file)
    def save(self):
        meta=""
        meta="::START,font:"+self.Font["family"]+",size:"+str(self.Font["size"])+",END::"
        try:
            print(self.file)
            if self.file != "":
                with open(self.file,"w") as f:
                    f.write(meta)
              
                    f.write(self.result.get("1.0",'end-1c'))
                self.master.title("text editor          "+self.file)
            else:
                print("No File Loaded!")
                f=fdialog.asksaveasfile(mode='w',defaultextension=".dimitritxt",filetypes=(("Readable file", "*.dimitritxt"),("All Files(Only Use If You Know What You're Doing)", "*.*")))
                f.write(self.result.get("1.0",'end-1c'))
                f.close()
                self.master.title("text editor          "+self.file)
        except:
            
                print("ERR: no file loaded")
                f=fdialog.asksaveasfile(mode='w',defaultextension=".dimitritxt",filetypes=(("Readable file", "*.dimitritxt"),("All Files(Only Use If You Know What You're Doing)", "*.*")))
                f.write(meta)
                
                f.write(self.result.get("1.0",'end-1c'))
                f.close()
                
                self.master.title("text editor          "+f.name)
    def saves(self,event):
        
        try:
            print(self.file)
            meta=""
            meta="::START,font:"+self.Font["family"]+",size:"+str(self.Font["size"])+",END::"
            if self.file:
                print("Saveing")
                with open(self.file,"w") as f:
                    print("Should write")
                    f.write(meta)
                 
                    f.write(self.result.get("1.0",'end-1c'))
                    print("Shoulda written")
                self.master.title("text editor          "+self.file)
            
        except:
            
                print("ERR: no file loaded")
                meta=""
                meta+="::START,font:"+self.Font["family"]+",size:"+str(self.Font["size"])+",END::"
                f=fdialog.asksaveasfile(mode='w',defaultextension=".dimitritxt",filetypes=(("Readable file", "*.dimitritxt"),("All Files(Only Use If You Know What You're Doing)", "*.*")))
                f.write(meta)
          
                f.write(self.result.get("1.0",'end-1c'))
                f.close()
                self.master.title("text editor          "+f.name)
                self.file=f.name
    def saveas(self):
        meta=""
        meta="::START,font:"+self.Font["family"]+",size:"+str(self.Font["size"])+",END::"
        f=fdialog.asksaveasfile(mode='w',defaultextension=".dimitritxt",filetypes=(("Readable file", "*.dimitritxt"),("All Files(Only Use If You Know What You're Doing)", "*.*")))
        f.write(meta)
        f.write(self.result.get("1.0",'end-1c'))
        f.close()
        
        self.master.title("text editor          "+f.name)
    def chfont(self):
        ans=qa.askstring("Choose font","Pick from:\nTimes\nHelvetica\nArial\nsystem")
        self.Font["family"]=ans
        
    def chsize(self):
        ans=qa.askinteger("Choose size","Pick a size")
        self.Font["size"]=ans
    def plus(self,event):
        print("Plus")
        self.Font["size"]=self.Font["size"]+2
    def sizem(self,event):
        print("Minus")
        self.Font["size"]=self.Font["size"]-2
    def wipe(self):
        try:
            self.result.delete("1.0","end")
            self.Font["family"]="Helvetica"
            self.Font["size"]=12
            self.file=False
            
        except:
            dia.showwarning("Error!","Something went wrong. Please try again or reload the application")
        self.master.title("text editor")
    def wipes(self,event):
        try:
            self.result.delete("1.0","end")
            self.Font["family"]="Helvetica"
            self.Font["size"]=12
            self.file=False
            
        except:
            dia.showwarning("Error!","Something went wrong. Please try again or reload the application")
        self.master.title("text editor")
    def red(self,event):
        try:
            self.result.edit_redo()
        except:
            print("Nothing to redo")
    def und(self,event):
        try:
            self.result.edit_undo()
        except:
            print("Nothing to redo")
    def redm(self):
        self.result.edit_redo()
    def undm(self):
        self.result.edit_undo()
    def create_widgets(self):

        
        
        self.menu=tk.Menu(self)
        self.filem= tk.Menu(self.menu,tearoff=0)
        self.filem.add_command(label="New",command=self.wipe,accelerator="Ctrl+N")
        self.filem.add_command(label="Open",command=self.ope,accelerator="Ctrl+O")
        self.filem.add_command(label="Save",command=self.save,accelerator="Ctrl+S")
        self.filem.add_command(label="Save As",command=self.saveas)
        self.bind_all("<Control-q>", self.quitc)
        self.bind_all("<Control-o>", self.opes)
        self.bind_all("<Control-s>", self.saves)
        self.bind_all("<Control-n>", self.wipes)
        self.bind_all("<Control-=>", self.plus)
        self.bind_all("<Control-z>", self.und)
        self.bind_all("<Control-y>", self.red)
        self.bind_all("<Control-minus>", self.sizem)
        self.menu.add_cascade(label="File", menu=self.filem)
        self.txt_frm = tk.Frame(self, width=1920, height=1080)
        self.txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        self.txt_frm.grid_propagate(False)
        # implement stretchability
        self.txt_frm.grid_rowconfigure(0, weight=1)
        self.txt_frm.grid_columnconfigure(0, weight=1)
        self.Font = tkFont.Font(family="Helvetica", size=12)
        self.result=tk.Text(self.txt_frm,borderwidth=0, relief="sunken", font=self.Font)
        self.result.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        scrollb = tk.Scrollbar(self.txt_frm, command=self.result.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.bind_all("<Control-p>", self.fullscreen)
        
        self.edits=tk.Menu(self.menu,tearoff=0)
        self.edits.add_command(label="Undo",command=self.undm)
        self.edits.add_command(label="Redo",command=self.redm)
        self.edits.add_separator()
        self.edits.add_command(label="Cut",accelerator="Ctrl+Z")
        self.edits.add_command(label="Copy",accelerator="Ctrl+C")
        self.edits.add_command(label="Paste",accelerator="Ctrl+V")
        self.edits.add_command(label="Select All",accelerator="Ctrl+A")
        self.edits.add_separator()
        self.edits.add_command(label="Font",command=self.chfont)
        self.edits.add_command(label="Size",command=self.chsize)
        self.menu.add_cascade(label="Edit",menu=self.edits)
        self.helpm=tk.Menu(self.menu,tearoff=0)
        self.helpm.add_command(label="About and Help",command=self.helpd)
        self.helpm.add_command(label="How to use",command=self.helpde)
        self.menu.add_cascade(label="About",menu=self.helpm)


        self.master.config(menu=self.menu)
        self._geom='200x200+0+0'
        self.result["yscrollcommand"] = scrollb.set
        
        
    def fullscreen(self,event):
        pass
        
        self.master.overrideredirect(val)
    def say_hi(self):
        print("hi there, everyone!")
    def helpd(self):
        
        dia.showinfo("About And Help","If you need help, speak to Dimitri. \n\n Simple, lightweight text editor to write, edit and read files with accuracy")
    def helpde(self):
        
        dia.showinfo("how to use","Simply type and go into 'file' to save! You can also open files. Specific files supported by the program are '.dimitritxt', which include your fonts and size! \n Fonts and size are viewable in the 'edit' tab")
    def print_contents(self,event):
        print("hi. contents of entry is now ---->",
              self.contents.get())
        self.contents.set("")
        self.ent["textvariable"]=self.contents
    def print_contentsb(self):
        print("hi. contents of entry is now ---->",
              self.contents.get())
        self.contents.set("")
        self.ent["textvariable"]=self.contents
root = tk.Tk()
app = Application(master=root)

app.master.title("text editor")
app.master.geometry("1280x720")
app.master.iconbitmap("icon.ico")
app.mainloop()
