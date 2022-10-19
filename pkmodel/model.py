#
# Model class
#

# function to catch type error in list
def catchTypeError(input_list):
    for val in input_list:
        if val < 0 or not isinstance(val, (float, int)):
            raise ValueError('input values should be non-negative numbers')


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

    Exceptions
    -----------
    raise value error if a non numerical value or negative number is given as an input
    raise value error if k_a input is not an empty list, or list containing non negative number

    """
    def __init__(self, central, peripherals=[], dosing=[]):
        catchTypeError(central)
        for periph in peripherals:
            catchTypeError(periph)
        if len(dosing) not in [0,1] or (len(dosing) == 1 and not isinstance(dosing[0], (int, float))):
            raise ValueError('invalid k_a input')
        self.central = central
        self.peripherals = peripherals
        self.dose = dosing

    @property
    def pcount(self):
        return len(self.peripherals)


