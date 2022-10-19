
''' 
Script for user to input all parameter values and store them
'''

# META QUESTIONS ON MODEL

NUM_OF_PCS = int(input('Number of peripheral compartments (0, 1, or 2): '))

DOSAGE_COMPARTMENT = input('Is there a dosage comaprtment (Yes/No)? ')

# TODO: what if it is a combination of both types of dosage
STEADY_DOSAGE = input('Is drug given in steady application over time (Yes/No)? ')

# SPECIFIC INPUTS BASED ON MODEL TYPE

VC = int(input('Volume of central compartment in mL: '))

CL = int(input('Clearance rate from central compartment in mL/h: '))

if NUM_OF_PCS > 0:
    VP1 = int(input('Volume of first peripheral compartment in mL: '))
    QP1 = int(input('Transition rate between central compartment and peripheral compartment 1 in mL/h: '))

if NUM_OF_PCS > 1:
    VP2 = int(input('Volume of second peripheral compartment in mL: '))
    QP2 = int(input('Transition rate between central compartment and peripheral compartment 2 in mL/h: '))

if DOSAGE_COMPARTMENT == 'Yes':
    KA = int(input('Absorption rate for dosage compartment (/h) if subcutaneous dosing: '))

if STEADY_DOSAGE == 'Yes':
    DOSE = int(input('Dose of drug in ng given at each hour: '))
    TOTAL_TIME = int(input('Time period during which drug is given in hours: '))
else: 
    DOSE = int(input('Instantaneous dose of drug given per time point (ng): '))
    TIME_POINTS = list(input('List of time points at which drug is given (hours): '))

