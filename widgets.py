import customtkinter as ctk
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu
from filelogic import openfile, saveAs, save, new

# Universal

def init_widget(parent, WidgetType, PackOptions):
    widget = WidgetType(parent)
    widget.pack(**(PackOptions))
    return widget

def show_about(parent, version_label):
    about = ctk.CTkToplevel(parent)
    about.title("About kPad")
    about.geometry("300x200")
    about.resizable(False, False)

    label = ctk.CTkLabel(
        about,
        text=f"kPad {version_label}. Made in CTk and Python."
    )
    label.pack(pady=30, padx=20)

def init_menubar(parent, textbox, version_label):
    menu = CTkMenuBar(parent)
 
    file_button = menu.add_cascade("File")
    appearance_button = menu.add_cascade("Appearance")
    help_button = menu.add_cascade("Help")


    file_dropdown = CustomDropdownMenu(widget=file_button)
    file_dropdown.add_option(option="New...", command=lambda: new(textbox=textbox))
    file_dropdown.add_option(option="Save...", command=lambda: save(textbox=textbox))
    file_dropdown.add_option(option="Save As...", command=lambda: saveAs(textbox=textbox))
    file_dropdown.add_option(option="Open...", command=lambda: openfile(textbox=textbox))
    file_dropdown.add_option(option="Exit...", command=parent.quit)

    appearance_dropdown = CustomDropdownMenu(widget=appearance_button)
    appearance_dropdown.add_option("Change appearance mode...", command=lambda: ctk.set_appearance_mode("light" if ctk.get_appearance_mode() == "Dark" else "dark"))

    help_dropdown = CustomDropdownMenu(widget=help_button)
    help_dropdown.add_option(option="About...", command=lambda: show_about(parent=parent, version_label=version_label))
 
    return menu

