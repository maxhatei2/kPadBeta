import customtkinter as ctk
from widgets import init_widget, init_menubar
from binds import bindShortcuts
from misc import on_close

__version__ = "0.13"

def main():
    root = ctk.CTk()
    root.geometry("480x360")
    root.title(f"kPad {__version__}")

    root.minsize(400, 300)

    textbox = ctk.CTkTextbox(root)

    init_menubar(root, textbox, version_label=__version__)

    bindShortcuts(root, textbox)

    textbox.pack(expand=True, fill="both")

    root.protocol("WM_DELETE_WINDOW", lambda: on_close(root, textbox))

    root.mainloop()

if __name__ == "__main__":
    main()