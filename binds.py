from filelogic import save, saveAs, new, openfile
import customtkinter as ctk
from misc import insert_tab

def bindShortcuts(parent, textbox):
    parent.bind("<Control-n>", lambda e: new(textbox=textbox))
    parent.bind("<Control-o>", lambda e: openfile(textbox=textbox))
    parent.bind("<Control-s>", lambda e: save(textbox=textbox))
    parent.bind("<Control-Shift-s>", lambda e: saveAs(textbox=textbox))
    parent.bind('<Control-Alt-t>', lambda e: ctk.set_appearance_mode("light" if ctk.get_appearance_mode() == "Dark" else "dark"))
    textbox.bind("<Tab>", insert_tab)