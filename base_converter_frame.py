import tkinter as tk
from abc import abstractmethod
from tkinter import ttk


class BaseConverterFrame(tk.Frame):

    _SCALES = []
    _BACKGROUND_COLOR = ""
    _CONVERTER_DESCRIPTION = ""

    def __init__(self, tab):
        super().__init__()
        # tab configuration
        self._tab = tab
        # Grid Configuration
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=2)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        # Components
        self._create_components()

    @staticmethod
    def set_attributes(scales, bg="#FFEFEF", description=""):
        BaseConverterFrame._SCALES = scales
        BaseConverterFrame._BACKGROUND_COLOR = bg
        BaseConverterFrame._CONVERTER_DESCRIPTION = description

    def _create_components(self):
        # Content box
        content = tk.StringVar(value=BaseConverterFrame._CONVERTER_DESCRIPTION)
        content_lbl = tk.Label(self._tab, textvariable=content, bg=BaseConverterFrame._BACKGROUND_COLOR, height=10,
                               width=80)
        content_lbl.grid(row=0, column=0, columnspan=2)
        # From label
        from_lbl = tk.Label(self._tab, text="From:", borderwidth=1,  bg=BaseConverterFrame._BACKGROUND_COLOR)
        from_lbl.config(font=("Verdana", 13))
        from_lbl.grid(row=1, column=0, padx=50)
        # To label
        to_lbl = tk.Label(self._tab, text="To:", borderwidth=1,  bg=BaseConverterFrame._BACKGROUND_COLOR)
        to_lbl.config(font=("Verdana", 13))
        to_lbl.grid(row=1, column=1)
        # From combobox
        self.from_cbox = ttk.Combobox(self._tab, values=BaseConverterFrame._SCALES, font=10)
        self.from_cbox.grid(row=2, column=0, sticky="NSWE", padx=20, pady=10)
        self.from_cbox.current(0)  # default value
        # To combobox
        self.to_cbox = ttk.Combobox(self._tab, values=BaseConverterFrame._SCALES, font=10)
        self.to_cbox.grid(row=2, column=1, sticky="NSWE", padx=20, pady=10)
        self.to_cbox.current(1)  # default value
        # Input
        # use a variable. use set and get methods
        self.entry_var1 = tk.DoubleVar(value=0)
        self.entry_field = tk.Entry(self._tab, textvariable=self.entry_var1, justify=tk.RIGHT, font=10)
        self.entry_field.grid(row=3, column=0, sticky="NSWE", padx=20)
        # Output
        self.out_var1 = tk.StringVar(value="")
        out_field = tk.Label(self._tab, textvariable=self.out_var1, bg=BaseConverterFrame._BACKGROUND_COLOR, font=10,
                             pady=10)
        out_field.grid(row=3, column=1)
        # Convert Button
        convert_btn = tk.Button(self._tab, text="Convert", font=8, command=self._convert)
        convert_btn.grid(row=4, column=0, sticky="NSWE", padx=20, pady=15)
        # Clear Button
        clear_btn = tk.Button(self._tab, text="Clear", font=8, command=self._clear_output)
        clear_btn.grid(row=4, column=1, sticky="NSWE", padx=20, pady=15)
        # Copy rights lbl
        author_lbl = tk.Label(self._tab, text="All rights reserved to author Cristian Murillo", borderwidth=1,
                              bg=BaseConverterFrame._BACKGROUND_COLOR)
        author_lbl.config(font=("Helvetica", 10))
        author_lbl.grid(row=5, columnspan=2, pady=20)

    def _clear_output(self):
        self.entry_field.delete(0, tk.END)
        self.out_var1.set("")

    @abstractmethod
    def _convert(self):
        pass
