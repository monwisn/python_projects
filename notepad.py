import os
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    root = Tk()
    root.geometry('500x400')
    # default window size
    # width = height = 300
    text_area = Text(root)
    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    edit_menu = Menu(menu_bar, tearoff=0)
    help_menu = Menu(menu_bar, tearoff=0)
    scroll_bar = Scrollbar(text_area)
    file = None

    def __init__(self, **kwargs):
        # Set notepad icon
        try:
            self.root.wm_iconbitmap("Notepad.ico")
        except:
            pass
        # self.root.wm_iconbitmap('Notepad.ico')

        # Set the window size (default size is 300x300)
        # try except block with KeyError (same for height)
        try:
            self.width = kwargs['width']
        except KeyError:
            pass

        try:
            self.height = kwargs['height']
        except KeyError:
            pass

        # self.width = kwargs['width']
        # self.height = kwargs['height']

        # Set the window title
        self.root.title('Untitled - Notepad')

        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # For left align
        left = (screen_width / 2) - (self.width / 2)

        # For right align
        top = (screen_height / 2) - (self.height / 2)

        # To make the textarea auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.text_area.grid(sticky=N + E + S + W)

        # To open a new file
        self.file_menu.add_command(label='New', command=self.new_file)

        # To open an existing file
        self.file_menu.add_command(label='Open', command=self.open_file)

        # To save a current file
        self.file_menu.add_command(label='Save', command=self.save_file)

        # To create a line in the dialog
        self.file_menu.add_separator()

        # To exit an application
        self.file_menu.add_command(label='Exit', command=self.quit_app)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        # To give a feature of:
        # cut
        self.edit_menu.add_command(label='Cut', command=self.cut)

        # copy
        self.edit_menu.add_command(label='Copy', command=self.copy)

        # paste
        self.edit_menu.add_command(label='Paste', command=self.paste)

        # editing
        self.menu_bar.add_cascade(label='Edit', menu=self.edit_menu)

        # To create a feature of description of the notepad
        self.help_menu.add_command(label='About Notepad', command=self.show_about)
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)
        self.root.config(menu=self.menu_bar)
        self.scroll_bar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.scroll_bar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scroll_bar.set)

    def quit_app(self):
        self.root.destroy()

    # exit()

    def show_about(self):
        showinfo('Notepad', 'Test information about created notepad.')

    def open_file(self):
        self.file = askopenfilename(defaultextension='.txt',
                                    filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])

        if self.file == '':
            self.file = None  # no file to open
        else:
            self.root.title(os.path.basename(self.file) + '- Notepad')
            self.text_area.delete(1.0, END)
            file = open(self.file, 'r')
            self.text_area.insert(1.0, file.read())
            file.close()

    def new_file(self):
        self.root.title('Untitled - Notepad')
        self.file = None
        self.text_area.delete(1.0, END)

    def save_file(self):
        if self.file is None:
            self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                          filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])

            if self.file == '':
                self.file = None
            else:
                # Try to save the file
                file = open(self.file, 'w')
                file.write(self.text_area.get(1.0, END))
                file.close()

                # Change the window title
                self.root.title(os.path.basename(self.file) + '- Notepad')
        else:
            file = open(self.file, 'w')
            file.write(self.text_area.get(1.0, END))
            file.close()

    def cut(self):
        self.text_area.event_generate('<<Cut>>')

    def copy(self):
        self.text_area.event_generate('<<Copy>>')

    def paste(self):
        self.text_area.event_generate('<<Paste>>')

    def run(self):
        # Run main application
        self.root.mainloop()


notepad = Notepad(width=500, height=400)
notepad.run()

notepad = Notepad()
