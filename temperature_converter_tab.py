from tkinter import messagebox

from TemperatureScales import Celsius, Fahrenheit, Kelvin, Rankine
from base_converter_frame import BaseConverterFrame


class TemperatureConverter(BaseConverterFrame):

    _SCALES = ["Celsius", "Fahrenheit", "Kelvin", "Rankine"]
    _BACKGROUND_COLOR = "#EBF3FD"
    _CONVERTER_DESCRIPTION = '''
        "Temperature is a measure of the average kinetic energy of the particles in an object, 
        which is a type of energy associated with motion. 
        It is the manifestation of thermal energy, present in all matter..."
        Source: Wikipedia
        '''

    def __init__(self, tab):
        super().set_attributes(
            TemperatureConverter._SCALES,
            TemperatureConverter._BACKGROUND_COLOR,
            TemperatureConverter._CONVERTER_DESCRIPTION
        )
        super().__init__(tab)

    def _convert(self):
        in_scale = self.from_cbox.current()
        out_scale = self.to_cbox.current()
        entry = self.entry_var1.get()
        temperature_list = [Celsius, Fahrenheit, Kelvin, Rankine]

        if in_scale == -1:
            messagebox.showerror('Error Message', 'Select an input temperature scale.')
        if out_scale == -1:
            messagebox.showerror('Error Message', 'Select the corresponding output temperature scale.')

        temperature = temperature_list[in_scale](entry)

        if out_scale == 0:
            self.out_var1.set(f'{temperature.to_celsius():.2f}')
        elif out_scale == 1:
            self.out_var1.set(f'{temperature.to_fahrenheit():.2f}')
        elif out_scale == 2:
            self.out_var1.set(f'{temperature.to_kelvin():.2f}')
        elif out_scale == 3:
            self.out_var1.set(f'{temperature.to_rankine():.2f}')

