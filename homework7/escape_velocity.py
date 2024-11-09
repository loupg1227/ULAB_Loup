# File = escape_velocity.py
# IF CALLED OUTSIDE THIS MODULE, THE CONVENTION IS ALWAYS "VELOCITY OF SPACESHIP" AS THE FIRST ARGUMENT, "MASS OF PLANET" AS THE SECOND ARGUMENT, "MASS OF SPACESHIP" AS THE THIRD ARGUMENT AND "RADIUS OF PLANET" AS THE LAST ARGUMENT. THIS IS THE ORDER TO FOLLOW ALWAYS. EVEN IF A FUNCTION DOES NOT INCLUDE ALL OF THESE PARAMETERS, THEY WILL ALWAYS FOLLOW THIS ORDER. 

import numpy as np

G = 6.6743e-11 # Gravitational constant

def get_kinetic_energy(speed_of_spaceship, mass_of_spaceship):
    """
    As a general topic, what I want to do is simply compare the kinetic energy of a spaceship     
    with the potential energy supplied by the planet that they are on. The first function will    
    calculate the kinetic energy of the spaceship, the second one will calculate the potential    
    energy supplied of the planet, and the last one will compare the 2. All units are in SI 
    units.

    Inputs:
    Mass of spaceship (Kilogram)
    Velocity of spaceship (Meters per second)

    Outputs:
    Kinetic Energy of the spaceship (Joules)
    """
    kinetic_energy = (0.5 * mass_of_spaceship)
    kinetic_energy *= (speed_of_spaceship ** 2) # Both of these lines simply compute the kinetic energy of the spaceship
    
    return kinetic_energy


def get_potential_energy(mass_of_planet, mass_of_spaceship, radius_of_planet):
    
    """
    This is the second function in the module which will compute the potential energy that the 
    energy supplies

    Inputs:
    Mass of planet (Kilogram)
    Mass of spaceship (Kilogram)
    Radius of planet (Meter)

    Outputs:
    Potential Energy of the planet (Joules)
    """
    
    potential_energy = G * mass_of_spaceship * mass_of_planet
    potential_energy /= radius_of_planet # Same as the first function, but this one computes the potential energy. 
    
    return potential_energy

def will_it_escape(speeds, mass_of_planet, mass_of_spaceship, radius_of_planet):
    """
    This is the last function which will compare the two values using the above functions, and will 
    return whether or not our spaceship will be able to escape the planet it is currently on. It's 
    important to keep in mind that while the test cases are Jupiter and Earth, this would work for 
    planet as long as the radius and mass was known

    Inputs:
    Range of speeds we wish to check (Meters per second)
    Mass of planet (Kilogram)
    Mass of spaceship (Kilogram)
    Radius of planet (Meter) 

    Outputs:
    Statement whether or not the speed will be enough to escape.
    """
    
    potential_energy = get_potential_energy(mass_of_planet, mass_of_spaceship, radius_of_planet) # Because we always stay on the same planet, we can set a variable inside the function as the potential energy of the planet and use it to compare it to a range of speeds that we may want to check. 
    
    escape_status = [] # Empty array where we will put out statements depending on whether the spaceship can escape. 
    
    for i in speeds: # We run through every element in our speeds array to see if each speed can or cannot escape the planet's gravity.  
        
        kinetic_energy = get_kinetic_energy(i, mass_of_spaceship) # For each iteration, we set this variable equal to the kinetic energy of the spaceship at that speed.
        
        if kinetic_energy > potential_energy: # If the kinetic energy of the specific "i" value is greater than the potential energy of the system, it will escape.
            result = "The spaceship will escape the planet's gravity"
        
        elif kinetic_energy == potential_energy: 
            result = "The spaceship will barely escape the planet's gravity" # Just for fun I set a new condition to say if the spaceship has barely enough speed, to warn people that it's best to probably boost the spaceship a little bit more just in case something unexpected happens.
        
        else: # If none of these things happens, the spaceship doesn't have enough speed to escape. 
            result = "The spaceship will not escape the planet's gravity"
        
        escape_status.append(result) # For each iteration, we get one result which will append into this empty array.
   
    return escape_status







