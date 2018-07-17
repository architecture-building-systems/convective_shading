"""
Resistive model

"""

__authors__ = "Prageeth Jayathissa"
__copyright__ = "Copyright 2016, Architecture and Building Systems - ETH Zurich"
__credits__ = []
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Prageeth Jayathissa"
__email__ = "jayathissa@arch.ethz.ch"
__status__ = "BETA"


def calculate_t_window(t_out, t_in, q_hw, q_vent, q_hfair, q_hfin):

	r_w = 112.0 #W/m2/K Radiation hitting window
	r_f= 30.0 #W/m2/K Radiation hitting foil
	q_w = 1.0 #u value of the glass


	q1=(1-(q_hfair**2/(q_hfin + q_hfair)))*(q_hw + q_vent + q_hfair)
	q2=(q_vent*t_out + (q_hfair/(q_hfin+q_hfair))*(r_f + t_in*q_hfin))/q1


	t_window = (r_w + q_w*t_out + q_hw*q2)/((q_w + q_hw)*(1-q_hw**2/(q1*(q_w + q_hw))))


	return t_window


if __name__ == "__main__":
    t_w = calculate_t_window(t_out=10.0, t_in = 20.0, q_hw=2000.0, q_vent=0.0, q_hfair=2000.0, q_hfin=2000.0)
    print t_w