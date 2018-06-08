"""
Main file to run the simulaion

"""

__authors__ = "Prageeth Jayathissa"
__copyright__ = "Copyright 2016, Architecture and Building Systems - ETH Zurich"
__credits__ = []
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Prageeth Jayathissa"
__email__ = "jayathissa@arch.ethz.ch"
__status__ = "BETA"



def solve_convective_coefficient(t_surface, t_inf, gravity, height, viscosity, conductivity_air, prandalt):
    expansion = calculate_expansion(t_surface, t_inf)
    grashof = calculate_grashof(gravity, expansion, height, viscosity, t_surface, t_inf)
    rayleigh = calculate_rayleigh(grashof, prandalt)
    nusselt = calculate_nusselt(rayleigh)

    convective_coefficient = calculate_convective_coefficient(nusselt, conductivity_air, height)
    return convective_coefficient


def calculate_expansion(t_surface, t_inf):
    t_film = (t_surface + t_inf)/2.0
    expansion = 1/t_film
    return expansion



def calculate_grashof(gravity, expansion, height, viscosity, t_surface, t_inf):
    grashof = (gravity * expansion * (t_surface - t_inf) * height**3.)/(viscosity**2.)
    return grashof

def calculate_rayleigh(grashof, prandalt):
    return grashof * prandalt

def calculate_nusselt(rayleigh):
    #For an isothermal vertical plate

    if 10**4 < rayleigh < 10**9:
        nusselt = 0.59 * rayleigh**(1./4.)
    elif 10**9 < rayleigh < 10**13:
        nusselt = 0.1 * rayleigh**(1./3.)
    else:
        raise ValueError("rayleigh number out of bounds")
    return nusselt

def calculate_convective_coefficient(nusselt, conductivity_air, height):
    convective_coefficient = nusselt * conductivity_air / height
    return convective_coefficient

def calculate_heat_transfer(convective_coefficient, t_surface, t_inf):
    heat_transfer = convective_coefficient * (t_surface - t_inf)
    return heat_transfer



if __name__ == "__main__":
    h = solve_convective_coefficient(t_surface=50+273., t_inf=30+273., gravity=9.81, height = 4., viscosity= 1.65 * 10**(-5), conductivity_air = 0.02685, prandalt = 0.7)
    print h

#def constants():
#     prandalt = 0.7 #prandalt Number for air around 300K
#     viscosity = 1.65 * 10**(-5) #kinematic viscosity of air around 300K [m2/s]
#     conductivity_air = 0.02685 #thermal conductivity of air at around 300K  [W/mK]
#     gravity = 9.81 #gravitational accelerateion [m/s2]