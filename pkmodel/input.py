def central_input():
    """
    Collect central compartment data from user input:
        Volume, VC / mL
        Clearance rate, CL / mL/h

    Returns:
    central (list): central compartment parameters [VC, CL]
    """
    # TODO: Fail if input anything except int or float
    VC = input('Volume of central compartment in mL: ')
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
    DOSAGE_COMPARTMENT = input('Is there a dosage compartment (Y/N)? ')

    dosage = []
    if DOSAGE_COMPARTMENT == 'Y':
        k_a = float(input('Absorption rate for dosage compartment (/h) if subcutaneous dosing: '))
        dosage.append(k_a)
    
    return dosage


def dosage_protocol_input():
    """ 
    Collect dosage protocol from user input

    Returns:
    STEADY_DOSAGE (string): 'Y' = steady dosage, 'N' = instantaneous dosage
    steady_dict (dict): If STEADY_DOSAGE == 'Y', {'start_time': START_TIME (float), 'end_time': END_TIME (float), 'dose_rate': DOSE_RATE (float)}
    inst_dict (dict): If STEADY_DOSAGE == 'N', {time1: DOSE, time2: DOSE, ...}
    """
    # TODO: what if it is a combination of both types of dosage 
    # TODO: Replace returned dictionaries to make it simpler?

    # TODO: Fail if input anything except Y/N
    STEADY_DOSAGE = input('Is drug given in steady application over time (Y/N)? ')

    if STEADY_DOSAGE == 'Y':
        DOSE_RATE = float(input('Dosage rate of drug given (ng/h): ')) # TODO: Only int or float
        print('Input time period during which drug is given:')
        START_TIME = float(input('Start time (h): ')) # TODO: Only int or float
        END_TIME = float(input('End time (h): ')) # TODO: Only int or float
        
        # Make dict of data
        steady_dict = {'start_time': START_TIME, 'end_time': END_TIME, 'dose_rate': DOSE_RATE}

        return STEADY_DOSAGE, steady_dict
        
    else: 
        DOSE = int(input('Instantaneous dose of drug given per time point (ng): ')) # TODO: Only int or float
        # Create time points list
        TIME_POINTS = [] 
        add_point = 'Y'
        while add_point != 'N':
                TIME_POINTS.append(input('Time point at which drug is given (h): '))
                add_point = input('Add another point (Y/N)? ')
                
        # Make dict of data
        inst_dict = {}
        for t in TIME_POINTS:
            inst_dict[t] = DOSE

        return STEADY_DOSAGE, inst_dict