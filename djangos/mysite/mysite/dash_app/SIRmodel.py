import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np
import pandas as pd



def epidemic_model(y, t, beta, gamma):

    """Define equations for the SIR model
       as required by scipy.integrate.ode
    """

    S, I, R = y

    dydt = [

        -beta * S * I,
         beta * S * I - gamma * I,
         gamma * I
    ]

    return dydt


def solve_model(model, initial_conditions, parameters):

    """
    This function solves the ode

    spi.odeint returns a numpy array with 3 columns,
    column 1 for S, column 2 for I, and column 3 for R
    """

    #define times in days
    time_start = 0.0;
    length_of_epidemic = 70
    time_step = 1

    t = np.arange(time_start, length_of_epidemic+time_step, time_step)


    results = spi.odeint( func = model,
                  y0 = initial_conditions,
                  t = t,
                  args = parameters )

    #transform numpy array to pandas dataframe. Comment this block if you don't care.
    results = pd.DataFrame(
        {
         'Susceptible':results[:,0],
         'Infectious':results[:,1],
         'Recovered':results[:,2],
         'time':t
        }
                   )

    results.set_index('time', drop=True, inplace=True)


    return results

def interactive_plot(S0, I0, R0, beta, gamma):

    """
        make an interactive plot to see how
        different parameters affect the evolution
        of the epidemic using the SIR model
    """

    results = solve_model(

                model = epidemic_model,
                initial_conditions = (S0, I0, R0),
                parameters = (beta, gamma) )

    results.plot()
    plt.show()

    return

if __name__=="__main__":

    S0 = 1-1e-6 
    I0 = 1e-6 
    R0 = 0
    beta = 1.4247
    gamma = 0.146

    interactive_plot(
            S0 = S0,
            I0 = I0,
            R0 = R0,
            beta = beta,
            gamma = gamma
           )
