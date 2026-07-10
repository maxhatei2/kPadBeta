import customtkinter as ctk
from widgets import init_widget, init_menubar
from binds import bindShortcuts
from misc import on_close, update_title
from version import __version__

def main():
    root = ctk.CTk()
    root.geometry("480x360")

    root.minsize(400, 300)

    textbox = ctk.CTkTextbox(root)

    update_title(parent=root, textbox=textbox)

    init_menubar(root, textbox, version_label=__version__)
    bindShortcuts(root, textbox)

    textbox.pack(expand=True, fill="both")

    root.protocol("WM_DELETE_WINDOW", lambda: on_close(root, textbox))

    root.mainloop()

if __name__ == "__main__":
    main()