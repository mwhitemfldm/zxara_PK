def central_input():
    """
    Collect central compartment data from user input:
        Volume, VC / mL
        Clearance rate, CL / mL/h

    Returns:
    central (list): central compartment parameters [VC, CL]
    """
    # TODO: Fail if input anything except int or float
    VC = float(input('Volume of central compartment in mL: '))
    CL = float(input('Clearance rate from central compartment in mL/h: '))
    central = [VC, CL]
    
    return central


def peripheral_input():
    """
    Collect peripheral compartment(s) data from user input:
        Number of compartments
        Volume, V / mL of each compartment
        Transition rate, Q / mL/h of each compartment

    Returns:
    peripherals (list of lists): peripheral compartment parameters [[V1, Q1], [V2, Q2]]
        - empty list if no peripheral compartments
    """
    # TODO: Fail if input anything except int
    NUM_OF_PCS = int(input('Number of peripheral compartments (0, 1, or 2): '))

    peripherals = []
    for i in range(0,NUM_OF_PCS):
         # TODO: Fail if input anything except int or float
        VP = float(input('Volume of peripheral compartment {} in mL: '.format(i+1)))
        QP = float(input('Transition rate between central compartment and peripheral compartment {} in mL/h: '.format(i+1)))
        peripherals.append([VP,QP])
    
    return peripherals



def dosage_input():
    """
    Determine dosage compartment existence and parameters from user input:
        Absorption rate k_a / /h

    Returns:
    dosing (list): dosage compartment parameters [k_a]
        - empty list if no dosage compartment
    """
    DOSAGE_COMPARTMENT = input('Is there a dosage compartment (Yes/No)? ')

    dosage = []
    if DOSAGE_COMPARTMENT == 'Yes':
        k_a = float(input('Absorption rate for dosage compartment (/h) if subcutaneous dosing: '))
        dosage.append(k_a)
    
    return dosage


def dosage_function_input():
    """ 
    Generates dosage function from user input 
    """

    # TODO: Fail if input anything except Yes/No
    STEADY_DOSAGE = input('Is drug given in steady application over time (Yes/No)? ')

    if STEADY_DOSAGE == 'Yes':
        DOSE = float(input('Dose of drug in ng given at each hour: '))
        TOTAL_TIME = float(input('Time period during which drug is given (h): '))
    else: 
        DOSE = int(input('Instantaneous dose of drug given per time point (ng): '))
        TIME_POINTS = list(input('List of time points at which drug is given (h): '))

    # return a_function

    # TODO: Generate function
    # TODO: what if it is a combination of both types of dosage


