import customtkinter as ctk
from widgets import init_widget, init_menubar
from filelogic import openfile, save, saveAs

__version__ = "0.12"

def main():
    root = ctk.CTk()
    root.geometry("480x360")
    root.title(f"kPad {__version__}")

    textbox = ctk.CTkTextbox(root)

    init_menubar(root, textbox, version_label=__version__)

    root.bind("<Control-o>", lambda e: openfile(textbox=textbox))
    root.bind("<Control-s>", lambda e: save(textbox=textbox))
    root.bind("<Control-Shift-s>", lambda e: saveAs(textbox=textbox))
    root.bind('<Control-Alt-t>', lambda e: ctk.set_appearance_mode("light" if ctk.get_appearance_mode() == "Dark" else "dark"))

    textbox.pack(expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()