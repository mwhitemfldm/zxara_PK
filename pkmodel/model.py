#
# Model class
#


class Model:
    """
    Parameters
    ----------
    central: numeric, optional
        an example paramter
    peripherals: array of lists, 
    dosing: list. 
          if i.b. dosing : empty list 
          if s.c dosing : contains absorption rate k_a
    
    Functions
    ----------
    pcount: int, number of peripheral compartments

    """

    def __init__(self, central, peripherals, dosing=[]):
        self.central = central
        self.peripherals = peripherals
        self.dose = dosing

    @property
    def pcount(self):
        return len(self.peripherals)