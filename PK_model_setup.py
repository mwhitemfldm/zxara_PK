
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
from pkmodel.visualisation import plotPK


STEADY_DOSAGE = True
DOSAGE_COMPARTMENT = False
TMAX = 100
central = (11,.6)

NUM_OF_PCS = 3
peripheral = [ [2,3], [0.1,0.5], [3,5] ]
ka = .9

def dose(t,X):
    if STEADY_DOSAGE:
        return X
    else:
        return X

def rhs(t, y, central, periphal, ka):
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
    X = 2 # User input DOSE AMOUNT

    if DOSAGE_COMPARTMENT:
        Dqd = dose(t,X) - ka*qd
        Dqc =   ka*qd   - CL*qc/VC - sum( Qp*(qc/VC - qp/Vp) )
    else:
        Dqd = np.array([0])
        Dqc = dose(t,X) - CL*qc/VC - sum( Qp*(qc/VC - qp/Vp) )

    Dqp = Qp*(qc/VC - qp/Vp)

    return np.concatenate((Dqd,Dqc,Dqp))

t_eval = np.linspace(0, TMAX, 1000)
y0 = np.zeros(2 + NUM_OF_PCS)

args = (central, peripheral, ka)
sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: rhs(t, y, *args),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, 
        t_eval=t_eval)

t = np.transpose(np.tile(sol.t, (len(sol.y),1)))
y = np.transpose(sol.y)

fig = plt.figure()
plt.plot(t,y)
plt.ylabel('drug mass [ng]')
plt.xlabel('time [h]')
plt.legend(['q1', 'q2', 'q3', 'q4', 'q5'])

plt.show()

print(t.shape)
print(y.shape)

plotPK(t, y, 1)

# %%
 