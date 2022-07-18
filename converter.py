import sys
import tkinter as tk
from tkinter import ttk, Menu
from PIL import Image, ImageTk
from temperature_converter_tab import TemperatureConverter
from pressure_converter_tab import PressureConverter
from calculadora_tab import Calculadora


class Converter(tk.Tk):
    def __init__(self):
        super().__init__()
        # main window
        # window size (in pixels)
        self.geometry('600x450+350+200')
        # Change window title
        self.title('MultiPurpose Converter')
        self.resizable(width=False, height=False)
        self.iconbitmap("images/calculator.ico")
        self.config(bd=5, bg="#BFC4BF")
        # Create tabs
        self._create_tabs()
        # Create menu
        self._create_menu()

    def _create_menu(self):
        # Menu setup
        main_menu = Menu(self)
        # Sub-menu1
        # tear-off = False. menu remains docked to main windows
        submenu_file = Menu(main_menu, tearoff=False)
        # adding options to file_menu
        submenu_file.add_command(label="Exit", command=self._exit_window)
        main_menu.add_cascade(menu=submenu_file, label="File")
        # Sub-menu2
        submenu_mod = Menu(main_menu, tearoff=False)
        submenu_mod.add_command(label="Calculator", command=lambda: self._select_tab(1))
        # Add a separator
        submenu_mod.add_separator()
        submenu_mod.add_command(label="Pressure", command=lambda: self._select_tab(2))
        submenu_mod.add_separator()
        submenu_mod.add_command(label="Temperature", command=lambda: self._select_tab(3))
        main_menu.add_cascade(menu=submenu_mod, label="Modules")
        # Sub-menu3
        submenu_help = Menu(main_menu, tearoff=0)
        submenu_help.add_command(label="Home", command=lambda: self._select_tab(0))
        main_menu.add_cascade(menu=submenu_help, label="About")
        # Displaying menu
        self.config(menu=main_menu)

    def _exit_window(self):
        self.quit()
        self.destroy()
        print("Closing Multi-Purpose Converter".center(40, "-"))
        sys.exit()

    def _create_tabs(self):
        # tab control with class Notebook
        self.tab_control = ttk.Notebook(self)
        # create tabs
        self.tab1 = tk.Frame(self.tab_control, height=440)
        self.tab_control.add(self.tab1, text="Home")
        self._tab1_components()
        self.tab2 = tk.Frame(self.tab_control, height=440, bg="#FFF3F3", relief=tk.SUNKEN, border=3)
        self.tab_control.add(self.tab2, text="Calculator")
        self._tab2_components()
        self.tab3 = tk.Frame(self.tab_control,  height=440, bg="#EBF6EB", relief=tk.SUNKEN, border=3)
        self.tab_control.add(self.tab3, text="Pressure")
        self._tab3_components()
        self.tab4 = tk.Frame(self.tab_control,  bg="#EBF3FD", relief=tk.SUNKEN, border=3)
        self.tab_control.add(self.tab4, text="Temperature")
        self._tab4_components()
        self.tab_control.pack(fill="both")

    def _tab1_components(self):
        content = tk.StringVar(value="""
        All rights reserved.
        Enjoy it!
        """)
        content_lbl = tk.Label(self.tab1, textvariable=content, bg='#FFCBCB', height=3,
                               relief=tk.RAISED, font=("Roman", 14))
        content_lbl.pack(side=tk.TOP, fill="both", pady=1)
        self.bg_image = ImageTk.PhotoImage(Image.open("images/love_atom_big.png"))
        bg_image_lbl = tk.Label(self.tab1, image=self.bg_image)
        bg_image_lbl.place(x=1, y=72)

    def _tab2_components(self):
        Calculadora(self.tab2)

    def _tab3_components(self):
        PressureConverter(self.tab3)

    def _tab4_components(self):
        TemperatureConverter(self.tab4)

    def _select_tab(self, tab_id):
        self.tab_control.select(tab_id)


if __name__ == "__main__":
    converter1 = Converter()
    converter1.mainloop()
