from tkinter.filedialog import asksaveasfilename, askopenfilename

def saveAs(textbox):
    path = asksaveasfilename()
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(textbox.get('1.0', 'end-1c'))

def openfile(textbox):
    path = askopenfilename()
    if path:
        with open(path, "r", encoding="utf-8") as f:
            textbox.delete("1.0", "end")
            textbox.insert("1.0", f.read())