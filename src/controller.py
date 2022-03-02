'''!
@file          controller.py
@brief
@details
@author        Cesar Santana
'''

class PID:
    '''!
    This class
    '''
    
    def __init__(self, K_P, K_I, K_D, setpoint):
        '''!
        '''
        self.setpoint = setpoint
        
        self.K_P = K_P
        
        self.K_I = K_I
        
        self.K_D = K_D
        ## Desired time step to be used by the controller
        self.t_step = 0
        ## Error of the controller
        self.error = 0
        ## Proportional error of the controller
        self.P_error = 0
        ## Integral error of the controller
        self.I_error = 0
        ## Derivative error of the controller
        self.D_error = 0
        
        
        self.time_vals = []
        
        self.meas_vals = []
        
        self.ref_vals = []
        
        ## Output value generated by the controller
        self.output = 0
    
    def ref(self, setpoint):
        '''!
        This method sets the target value for
        the controller
        @param setpoint Desired value for the controller 
        '''
        self.setpoint = setpoint
        
        # return self.setpoint
    
    def prop_gain(self, K_P):
        '''!
        This method sets the proportional gain for
        the controller
        @param K_P Proportional gain of the controller
        '''
        
        self.K_P = K_P
        
        return self.K_P
    
    def int_gain(self, K_I):
        '''!
        This method sets the integral gain for
        the controller
        @param K_I Integral gain of the controller
        '''
        
        self.K_I = K_I
        
        return self.K_I
    
    def deriv_gain(self, K_D):
        '''!
        This method sets the derivative gain for
        the controller
        @param K_D Derivative gain of the controller
        '''
        
        self.K_D = K_D
        
        return self.K_D
    
    def compute(self, meas, t_step, save_data = False):
        '''!
        This method computes the total output of the PID controller by
        using the proportional, integral, and derivative error
        @param meas   Measured value to be corrected
        @param t_step Desired time step value
        '''
        self.meas = meas
        
        self.t_step = t_step
        
        if save_data:
            self.time_vals.append(t_step)
            self.meas_vals.append(meas)
            self.ref_vals.append(self.setpoint)
            
        self.error = self.setpoint - self.meas
        
        self.P_error = self.error
        
        self.I_error = self.error * self.t_step
         
        self.D_error = self.error / self.t_step
        
        self.output = self.P_error*self.K_P + self.I_error*self.K_I + self.D_error*self.K_D
        
        # if self.output > 100:
        #     self.output = 100
        # elif self.output < -100:
        #     self.output = -100
                
        return self.output
    
    def clear(self):
        
        self.time_vals = []
        
        self.meas_vals = []
        
        self.ref_vals = []
