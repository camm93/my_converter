"""
Temperature scale conversion.
"""
from abc import abstractmethod

__author__ = "Cristian Murillo"


class TemperatureScales:

    def __init__(self, temperature: float):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature

    @abstractmethod
    def to_celsius(self):
        pass

    @abstractmethod
    def to_fahrenheit(self):
        pass

    def to_kelvin(self):
        return self.to_celsius() + 273.15

    def to_rankine(self):
        return self.to_fahrenheit() + 459.67


class Celsius(TemperatureScales):

    def to_celsius(self):
        return self.temperature

    def to_fahrenheit(self):
        return 1.8 * self.temperature + 32


class Fahrenheit(TemperatureScales):

    def to_celsius(self):
        return (self.temperature - 32) * (5/9)

    def to_fahrenheit(self):
        return self.temperature


class Kelvin(Celsius):

    _kelvin_to_celsius = 273.15

    def __init__(self, temperature):
        super().__init__(temperature - Kelvin._kelvin_to_celsius)


class Rankine(Fahrenheit):

    _rankine_to_fahrenheit = 459.67

    def __init__(self, temperature):
        super().__init__(temperature - Rankine._rankine_to_fahrenheit)


if __name__ == "__main__":
    results = '{:<15s} = {:>8}: [celsius = {:.2f}, Fahrenheit = {:.2f}, Kelvin = {:.2f}, Rankine = {:.2f}]'

    cel = Celsius(0)
    print(results.format(
        cel.__class__.__name__, cel.temperature, cel.to_celsius(), cel.to_fahrenheit(), cel.to_kelvin(),
        cel.to_rankine()
    ))

    fahr = Fahrenheit(32)
    print(results.format(
        fahr.__class__.__name__, fahr.temperature, fahr.to_celsius(), fahr.to_fahrenheit(), fahr.to_kelvin(),
        fahr.to_rankine()
    ))

    kel = Kelvin(273.15)
    print(results.format(
        kel.__class__.__name__, kel.temperature, kel.to_celsius(), kel.to_fahrenheit(), kel.to_kelvin(),
        kel.to_rankine()
    ))

    ran = Rankine(491.67)
    print(results.format(
        ran.__class__.__name__, ran.temperature, ran.to_celsius(), ran.to_fahrenheit(), ran.to_kelvin(),
        ran.to_rankine()
    ))

