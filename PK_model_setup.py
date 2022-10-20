#%%
'''
INPUTS
    Number of peripheral compartments (n int)
    Dose regime (constant or times, amount pairs)
    Dose compartment (True/False)
    Protocols (transitions Q, volumes V and clearance CL)
'''
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate

STEADY_DOSAGE = False
DOSAGE_COMPARTMENT = False
TMAX = 10
central = (11,.6)

NUM_OF_PCS = 3
peripheral = [ [2,3], [0.1,0.5], [3,5] ]
ka = .9

def rhs(t, y, central, periphal, ka, dose_concentration):
    '''
    t       : time, independant
    y       : [q_dosage, q_central, q_periphal_1, ..., q_periphal_n]
    central : [VC, CL]
    periph  : [ [Q1,V1],..., [Qn,Vn] ]
    ka      : subcutaneous dosing absorption rate, possibly None
    '''
    qd = np.array([y[0]])
    qc = np.array([y[1]])
    qp = np.array(y[2:]) #What happens if empty?
    VC, CL = central
    Qp = np.array([item[0] for item in periphal])
    Vp = np.array([item[1] for item in periphal])

    if DOSAGE_COMPARTMENT:
        Dqd = dose_concentration - ka*qd
        Dqc =   ka*qd   - CL*qc/VC - sum( Qp*(qc/VC - qp/Vp) )
    else:
        Dqd = np.array([0])
        Dqc = dose_concentration - CL*qc/VC - sum( Qp*(qc/VC - qp/Vp) )

    Dqp = Qp*(qc/VC - qp/Vp)

    return np.concatenate((Dqd,Dqc,Dqp))

def Integrate(t_interval, y0, central, periphal, ka, dose_concentration):
    args = (central, periphal, ka, dose_concentration)
    sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: rhs(t, y, *args),
            t_span=[t_interval[0], t_interval[-1]],
            y0=y0, 
            t_eval=t_interval)
    
    return sol.t, sol.y
    
t0 = 0
dose_concentration = 0
DOSE_REGIME = [[1.,1.,2.], [2.,2.,3.]]
y0 = np.zeros(2 + NUM_OF_PCS)
tsol = []
ysol = np.zeros((5,1))

for dosage in DOSE_REGIME:
    ## PRE-DOSE INTERVAL
    t_interval = np.arange(t0,dosage[0],TMAX/1000) # Increment dosage concentration at start of t_interval
    sol_t, sol_y = Integrate(t_interval, y0, central, peripheral, ka, dose_concentration)
    tsol.append(sol_t)
    ysol = np.hstack([ysol,sol_y])
    y0 = sol_y[:,-1]


    ## DOSE INTERVAL
    if dosage[0]==dosage[1]:
        y0[0] += dosage[2]
        t0 = dosage[0]

    else:
        t_interval = np.arange(dosage[0],dosage[1],TMAX/1000)
        dose_concentration = dosage[2]
        sol_t, sol_y = Integrate(t_interval,y0, central, peripheral, ka, dose_concentration)
        tsol.append(sol_t)
        ysol = np.hstack([ysol,sol_y])
    
    t0 = dosage[1]
    dose_concentration = 0

t_interval = np.arange(t0,TMAX,TMAX/1000)
sol_t, sol_y = Integrate(t_interval,y0, central, peripheral, ka, dose_concentration)
tsol.append(sol_t)
ysol = np.hstack([ysol,sol_y])

tsol = np.concatenate((tsol))
ysol = ysol[:,1:]


fig = plt.figure()
plt.plot(tsol,np.transpose(ysol))
plt.ylabel('drug mass [ng]')
plt.xlabel('time [h]')
plt.legend(['q1', 'q2', 'q3', 'q4', 'q5'])

plt.show()
# %%
