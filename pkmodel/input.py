
''' 
Script for user to input all parameter values and store them
'''

# META QUESTIONS ON MODEL

NUM_OF_PCS = int(input('Number of peripheral compartments (0, 1, or 2): '))

DOSAGE_COMPARTMENT = input('Is there a dosage compartment (Yes/No)? ')

# TODO: what if it is a combination of both types of dosage
STEADY_DOSAGE = input('Is drug given in steady application over time (Yes/No)? ')

# SPECIFIC INPUTS BASED ON MODEL TYPE

# Creating central array
VC = float(input('Volume of central compartment in mL: '))
CL = float(input('Clearance rate from central compartment in mL/h: '))
central = [VC, CL]

# Creating peripherals array
peripherals = []
for i in range(0,NUM_OF_PCS):
    VP = float(input('Volume of peripheral compartment {} in mL: '.format(i+1)))
    QP = float(input('Transition rate between central compartment and peripheral compartment {} in mL/h: '.format(i+1)))
    peripherals.append([VP,QP])

# Creating dosing array
dosing = []
if DOSAGE_COMPARTMENT == 'Yes':
    KA = float(input('Absorption rate for dosage compartment (/h) if subcutaneous dosing: '))
    dosing.append(KA)


if STEADY_DOSAGE == 'Yes':
    DOSE = float(input('Dose of drug in ng given at each hour: '))
    TOTAL_TIME = float(input('Time period during which drug is given (h): '))
else: 
    DOSE = int(input('Instantaneous dose of drug given per time point (ng): '))
    TIME_POINTS = list(input('List of time points at which drug is given (h): '))

