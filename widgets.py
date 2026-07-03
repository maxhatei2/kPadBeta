import customtkinter as ctk
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu
from filelogic import openfile, saveAs

# Universal

def init_widget(parent, WidgetType, PackOptions):
    widget = WidgetType(parent)
    widget.pack(**(PackOptions))
    return widget

def show_about(parent):
    about = ctk.CTkToplevel(parent)
    about.title("About kPad")
    about.geometry("300x200")
    about.resizable(False, False)

    label = ctk.CTkLabel(
        about,
        text=f"kPad 0.1\nA lightweight text editor.\n\nBuilt with CustomTkinter.\n(this window is very basic because\n1. this is v0.1\n2. I don't have much to show about)"
    )
    label.pack(pady=30, padx=20)

def init_menubar(parent, textbox):
    menu = CTkMenuBar(parent)
 
    file_button = menu.add_cascade("File")
    help_button = menu.add_cascade("Help")

    file_dropdown = CustomDropdownMenu(widget=file_button)
    file_dropdown.add_option(option="Save", command=lambda: saveAs(textbox=textbox))
    file_dropdown.add_option(option="Open", command=lambda: openfile(textbox=textbox))
    file_dropdown.add_option(option="Exit", command=parent.quit)

    edit_dropdown = CustomDropdownMenu(widget=help_button)
    edit_dropdown.add_option(option="About", command=lambda: show_about(parent=parent))
 
    return menu

