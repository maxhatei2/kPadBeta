# kPad Remastered

kPad is a lightweight text editor, made in Python and uses only 2 dependencies.

It's rebuilt from the bottom-up with much cleaner code divided in multiple files.

## Status

Current version is beta 0.14.

## Versioning

Versions 0.2 through 0.9 will not exist! Instead, from 0.1, the next version will be 0.11 until 0.99 (maybe). After that stability will exist and the app will move to a calendar-based versioning system.

## Requirements

Make sure you have Python 3.10 or higher installed.

## Installation

Download and extract the repository (or Git-clone it), then move in the directory and run:

### For Windows (PowerShell)

`python -m venv env
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& .\Scripts\Activate.ps1)
pip install customtkinter CTkMenuBar
python main.py
`

### For Linux/Mac

`
python3 -m venv env
sh ./src/activate
pip install customtkinter CTkMenuBar
python3 main.py
`

## Roadmap (as of 0.14)

- Translation support

- Remember last opened file between sessions

- Config support

## Changelog

<details>
<summary><strong>0.1</strong> Initial beta release</summary>

- Core of a text editor

</details>

<details>
<summary><strong>0.11</strong> New features</summary>

- Unified save / save-as behavior
- Error handling for save, save-as and open commands

</details>
