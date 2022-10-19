#
# Model class
#


class Model:
    """
    Parameters
    ----------
    central: list, [central_volume, clearance_rate]
    peripherals: array of lists, [[compartment1_volume, transition_rate1], ...]
    dosing: list, 
          if i.b. dosing : empty list 
          if s.c dosing : list contains absorption rate KA
    
    Functions
    ----------
    pcount: int, number of peripheral compartments

    """
    
    def __init__(self, central, peripherals=[], dosing=[]):
        self.central = central
        self.peripherals = peripherals
        self.dose = dosing

    @property
    def pcount(self):
        return len(self.peripherals)
