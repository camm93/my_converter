"""
Pressure scale conversion.
"""

from abc import abstractmethod

__author__ = "Cristian Murillo"


class PressureScales:
    def __init__(self, pressure):
        self._pressure = pressure

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        self._pressure = pressure

    @abstractmethod
    def to_atmosphere(self):
        pass

    def to_mmhg(self):
        return self.to_atmosphere() * 760

    @abstractmethod
    def to_psia(self):
        pass

    def to_psig(self):
        return self.to_psia() - 14.6959

    @abstractmethod
    def to_bar(self):
        pass

    def to_pascal(self):
        return self.to_bar() * 100000


class Atmosphere(PressureScales):

    def to_atmosphere(self):
        return self.pressure

    def to_psia(self):
        return self.pressure * 14.6959

    def to_bar(self):
        return self.pressure * 1.01325


class MmHg(PressureScales):

    def to_atmosphere(self):
        return self.pressure / 760

    def to_mmhg(self):
        return self.pressure

    def to_psia(self):
        return self.pressure / 51.715

    def to_bar(self):
        return self.pressure / 750.06


class Psia(PressureScales):

    def to_atmosphere(self):
        return self.pressure / 14.6959

    def to_psia(self):
        return self.pressure

    def to_bar(self):
        return self.pressure / 14.50377


class Psig(Psia):

    _psia_to_psig = 14.6959

    def __init__(self, pressure):
        super().__init__(pressure + Psig._psia_to_psig)


class Bar(PressureScales):

    def to_atmosphere(self):
        return self.pressure / 1.01325

    def to_psia(self):
        return self.pressure * 14.50377

    def to_bar(self):
        return self.pressure


class Pascal(Bar):

    _bar_to_pascal = 100000

    def __init__(self, pressure):
        super().__init__(pressure / Pascal._bar_to_pascal)


if __name__ == "__main__":
    results = '{:<15s} = {:>8}: [atm = {:.2f}, mmHg = {:.2f}, psia = {:.2f}, psig = {:.2f}, bar = {:.2f}, pa = {:.2f}]'

    atm = Atmosphere(1)
    print(results.format(
        atm.__class__.__name__, atm.pressure, atm.to_atmosphere(), atm.to_mmhg(), atm.to_psia(), atm.to_psig(),
        atm.to_bar(), atm.to_pascal()
    ))

    mmHg = MmHg(760)
    print(results.format(
        mmHg.__class__.__name__, mmHg.pressure, mmHg.to_atmosphere(), mmHg.to_mmhg(), mmHg.to_psia(), mmHg.to_psig(),
        mmHg.to_bar(), mmHg.to_pascal()
    ))

    psia = Psia(14.6959)
    print(results.format(
        psia.__class__.__name__, psia.pressure, psia.to_atmosphere(), psia.to_mmhg(), psia.to_psia(), psia.to_psig(),
        psia.to_bar(), psia.to_pascal()
    ))

    psig = Psig(0)
    print(results.format(
        psig.__class__.__name__, psig.pressure, psig.to_atmosphere(), psig.to_mmhg(), psig.to_psia(), psig.to_psig(),
        psig.to_bar(), psig.to_pascal()
    ))

    bar = Bar(1.01325)
    print(results.format(
        bar.__class__.__name__, bar.pressure, bar.to_atmosphere(), bar.to_mmhg(), bar.to_psia(), bar.to_psig(),
        bar.to_bar(), bar.to_pascal()
    ))

    pascal = Pascal(101325)
    print(
        results.format(
            pascal.__class__.__name__, pascal.pressure, pascal.to_atmosphere(), pascal.to_mmhg(), pascal.to_psia(),
            pascal.to_psig(), pascal.to_bar(), pascal.to_pascal()
        ))
