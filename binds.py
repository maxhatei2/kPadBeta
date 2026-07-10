from misc import HandleNew, HandleOpen, HandleSave, HandleSaveAs
import customtkinter as ctk
from misc import insert_tab, on_text_modified

def bindShortcuts(parent, textbox):
    parent.bind("<Control-n>", lambda e: HandleNew(parent=parent, textbox=textbox))
    parent.bind("<Control-o>", lambda e: HandleOpen(parent=parent, textbox=textbox))
    parent.bind("<Control-s>", lambda e: HandleSave(textbox=textbox, parent=parent))
    parent.bind("<Control-Shift-s>", lambda e: HandleSaveAs(parent=parent, textbox=textbox))
    parent.bind('<Control-Alt-t>', lambda e: ctk.set_appearance_mode("light" if ctk.get_appearance_mode() == "Dark" else "dark"))
    textbox.bind("<Tab>", insert_tab)
    textbox.bind("<KeyRelease>", lambda e: on_text_modified(e, parent=parent, textbox=textbox))