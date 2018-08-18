#!/usr/bin/python

import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np
import pandas as pd
import sys
import os

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


def interactive_plot(beta, gamma, S0=0.9999, I0=0.0001, R0=0.0):
    
    """
        make an interactive plot to see how
        different parameters affect the evolution
        of the epidemic using the SIR model
    """
 
    #initial_conditions = (S0, I0, R0)
    results = solve_model( 
        
                model = epidemic_model, 
                initial_conditions = (S0, I0, R0), 
                parameters = (beta, gamma) )
   
    results.plot() 
    plt.title(r'SIR model for $\beta$=%3.1f, $R_0$ = %3.1f'%(beta, beta/gamma))
    ax = plt.gca()
    ax.set_facecolor((0.8, 0.47, 0.3, 0.2))
    plt.ylabel('Proportions')
    plt.xlabel('time (in days)')

    #http://hplgit.github.io/web4sciapps/doc/pub/._web4sa_django006.html#wf:vib:django 
    #if not os.path.isdir('static/epilearn/img'):
    #    os.mkdir('static')
    #else:
        # Remove old plot files
    #    os.remove('static/epilearn/img/SIRmodel.png')

    #plotfile = os.path.join(path, 'SIRmodel.png') 
    
    dirname = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dirname, 'static/epilearn/img/SIRmodel.png')
    plt.savefig(filename)
    return 0
    

if __name__=="__main__":
	
    beta = float(sys.argv[1])   #rate of infection
    R0   = float(sys.argv[2])   #basic reproductive number for the disease
    gamma = beta/R0
    
    interactive_plot(beta, gamma)
