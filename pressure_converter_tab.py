from tkinter import messagebox

from base_converter_frame import BaseConverterFrame
from PressureScales import Atmosphere, MmHg, Psia, Psig, Bar, Pascal


class PressureConverter(BaseConverterFrame):

    _SCALES = ["Atmosphere", "mmHg", "Psia", "Psig", "Bar", "Pascal"]
    _BACKGROUND_COLOR = "#EBF6EB"
    _CONVERTER_DESCRIPTION = '''
        "Pressure is the force applied perpendicular to the surface of an object per unit area
        over which that force is distributed. Various units are used to express pressure. 
        For example, the pascal (Pa), is one newton per square metre (N/m2). Similarly, 
        the pound-force per square inch (psi) is the traditional unit of pressure in the imperial 
        and U.S. customary systems..."
        Source: Wikipedia
        '''

    def __init__(self, tab):
        super().set_attributes(
            PressureConverter._SCALES,
            PressureConverter._BACKGROUND_COLOR,
            PressureConverter._CONVERTER_DESCRIPTION
        )
        super().__init__(tab)

    def _convert(self):
        in_scale = self.from_cbox.current()
        out_scale = self.to_cbox.current()
        entry = self.entry_var1.get()
        pressure_list = [Atmosphere, MmHg, Psia, Psig, Bar, Pascal]

        if in_scale == -1:
            messagebox.showerror('Error Message', 'Select an input pressure scale.')
        if out_scale == -1:
            messagebox.showerror('Error Message', 'Select the corresponding output pressure scale.')

        pressure = pressure_list[in_scale](entry)

        if out_scale == 0:
            self.out_var1.set(f'{pressure.to_atmosphere():.4f}')
        elif out_scale == 1:
            self.out_var1.set(f'{pressure.to_mmhg():.4f}')
        elif out_scale == 2:
            self.out_var1.set(f'{pressure.to_psia():.4f}')
        elif out_scale == 3:
            self.out_var1.set(f'{pressure.to_psig():.4f}')
        elif out_scale == 4:
            self.out_var1.set(f'{pressure.to_bar():.4f}')
        elif out_scale == 5:
            self.out_var1.set(f'{pressure.to_pascal():.4f}')
