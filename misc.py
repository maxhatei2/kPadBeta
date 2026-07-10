from tkinter.messagebox import askyesno
from os.path import basename
import filelogic
from version import __version__

def on_close(parent, textbox):
    if textbox.edit_modified():
        if not askyesno('kPad - Unsaved changes', 'There are unsaved changes. Close anyway?'):
            return
    parent.destroy()

def insert_tab(event):
    event.widget.insert("insert", "    ")  # 4 spaces, or "\t" for a real tab char
    return "break"

def update_title(parent, textbox):
    name = basename(filelogic.OpenPath) if filelogic.OpenPath else "new"
    modified = "*" if textbox.edit_modified() else ""
    parent.title(f"kPad {__version__} - {name}{modified}")

def on_text_modified(event, parent, textbox):
    update_title(parent, textbox)
    textbox.edit_modified(False)

def HandleOpen(parent, textbox):
    filelogic.openfile(textbox=textbox)
    update_title(parent=parent, textbox=textbox)

def HandleSave(parent, textbox):
    filelogic.save(textbox=textbox)
    update_title(parent=parent, textbox=textbox)

def HandleSaveAs(parent, textbox):
    filelogic.saveAs(textbox=textbox)
    update_title(parent=parent, textbox=textbox)

def HandleNew(parent, textbox):
    filelogic.new(textbox=textbox)
    update_title(parent=parent, textbox=textbox)