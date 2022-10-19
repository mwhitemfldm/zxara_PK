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


""" Redundant subclasses """ 
# class Central_Compartment:
#     """A Pharmokinetic (PK) model

#     Parameters
#     ----------

#     value: numeric, optional
#         an example paramter

#     """
#     def __init__(self, V: float, CL: float):
#         self.volume = V
#         self.clearance = CL

# class Peripheral_Compartment:
#     """ Compartments """
#     def __init__(self, V: float, Q: float):
#         self.volume = V
#         self.transrate = Q

# class Dosing_Compartment:
#     def __init__(self, ka=None):
#         self.abs = ka