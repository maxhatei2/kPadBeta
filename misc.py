from tkinter.messagebox import askyesno

def on_close(parent, textbox):
    if textbox.edit_modified():
        if not askyesno('kPad - Unsaved changes', 'There are unsaved changes. Close anyway?'):
            return
    parent.destroy()

def insert_tab(event):
    event.widget.insert("insert", "    ")  # 4 spaces, or "\t" for a real tab char
    return "break"