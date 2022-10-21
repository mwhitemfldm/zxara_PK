def central_input():
    """
    Collect central compartment data from user input:
        Volume, VC / mL
        Clearance rate, CL / mL/h

    Returns:
    central (list): central compartment parameters [VC, CL]
    """
    # TODO: Fail if input anything except int or float
    VC = None

    while True:
        try:
            VC = float(input('Volume of central compartment in mL: '))
        except ValueError:
            print("Incorrect type try again")
            continue
        else:
            break


    while float(input('Volume of central compartment in mL: ') != float:
        VC = (input('Volume of central compartment in mL: '))
    
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
    NUM_OF_PCS = int(input('Number of peripheral compartments: '))

    peripherals = []
    for i in range(0,NUM_OF_PCS):
         # TODO: Fail if input anything except int or float
        VP = float(input(f'Volume of peripheral compartment {i+1} in mL: '))
        QP = float(input(f'Transition rate between central compartment and peripheral compartment {i+1} in mL/h: '))
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

def input_doses():
    '''
    Collect number of doses, whether they are steady or instantaneous, and what amount of drug is given
    '''
    TOTAL_DOSES = int(input('How many total doses is the individual given (steady or continuous)? '))
    dosing_array = []

# change start time
    for i in range(1,TOTAL_DOSES+1):
        print('Dose ' + str(i) + ':')
        # TODO: Fail if input anything except Y/N
        DOSE_TYPE = input('Is drug given in steady application over time (A) or instantaneously (B)? ')

        if DOSE_TYPE == 'A':
            DOSE_RATE = float(input('Dosage rate of drug given (ng/h): ')) # TODO: Only int or float
            START_TIME = float(input('Start time (h): ')) # TODO: Only int or float
            END_TIME = float(input('End time (h): ')) # TODO: Only int or float
            DOSE = DOSE_RATE * (END_TIME - START_TIME)
        
            # Make dosing array
            dosing_array.append([START_TIME, END_TIME, DOSE])
        
        if DOSE_TYPE == 'B':
            DOSE = int(input('Instantaneous dose of drug given per time point (ng): ')) # TODO: Only int or float
            TIME_POINT = float(input('Time point at which drug is given (h): '))
            dosing_array.append([TIME_POINT, TIME_POINT, DOSE])

    return dosing_array

def max_time_input():
    """ # TODO: docstring """
    MAX_TIME = float(input('Enter maximum time for model (h): '))
    return MAX_TIME