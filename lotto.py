import tkinter as tk
from tkinter.filedialog import askopenfilename as fd
class Lotto():
    def __init__(this):
        
        this.rootw = tk.Tk()
        this.rootw.geometry("640x480")
        this.rootw.resizable(False, False)
        this.rootw.title(" Lotto ")
        
        
        this.TextSzelveny = tk.Text(this.rootw, height = 10, width = 20)
        #this.scrollb = tk.Scrollbar(command = this.TextSzelveny.yview)
        #this.scrollb.pack()
        #this.TextSzelveny['yscrollcommand'] = this.scrollb.set
        this.TextSzelveny.pack()
        this.loadBtn = tk.Button(this.rootw, text = "Szelvény betöltése", command = this.loadFile)
        this.loadBtn.pack()
        
        
        
        this.rootw.mainloop()


    def loadFile(this):
        #this.rootw.withdraw()
        this.TextSzelveny.delete('1.0',tk.END)
        with open(fd(filetypes=[("text files",".csv .txt")]),'rt') as f:
            this.TextSzelveny.insert(tk.END, f.read())

if __name__ == '__main__':
    app = Lotto()

