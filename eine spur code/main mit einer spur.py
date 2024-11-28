from auto import Auto
import time as t
import locale
from random import randint


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


document = True

fh = open("documentation.txt", "a")



current_time = 0.0
spawn_timer = 0.0
time_step = 0.1

autos =  []
autos_meter = []
autos_vel = []

auto_typen=["mini", "pkw", "pkw", "pkw", "pkw", "pkw", "pkw", "van", "lkw", "lkw", "lkw", "lkw", "renn", "renn", "bus", "caprio"]


    


boom = False

achtung_counter = 0
achtung = False

waiting_time = randint(5, 10)
autos.append(Auto.create_auto("pkw", 0))
autos_meter.append(0)
autos_vel.append(0)






def animate_simulation(autos, time_step, spawn_timer, waiting_time):
    # Create the figure and axis for the animation
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10000)  # Set the x-axis limit for the road (0 to 1000 meters)
    ax.set_ylim(-2, 2)  # Set the y-axis just for visibility, not used
    
    # Set up a line object to represent the cars
    line, = ax.plot([], [], 'bo', markersize=8)  # Blue dots for cars
    
    # Initialize the car positions and velocities
    autos_meter = [auto.meter for auto in autos]
    autos_vel = [auto.vel for auto in autos]
    
    # Function to update the car positions for each frame
    def update(frame):
        nonlocal spawn_timer, waiting_time
        
        # Increment current time and spawn timer
        spawn_timer += time_step
        
        # Update car positions and velocities
        for i in range(len(autos)):
            
            if i > 0:
                autos[i].fahren(time_step, autos[i-1].back, autos[i-1].vel)  # Update position of each car
                autos_meter[i] = autos[i].meter  # Update the meter of the car

                # Check for collisions (between consecutive cars)
                if autos[i].meter >= autos[i-1].back:
                    print(f"Crash between car {i} and car {i-1}!")
                    
                    print(i)
                    print(autos[i].spawn_time)
                    print(autos[i-1].spawn_time)
                    print(autos[i].wun_vel)
                    print(autos[i].wun_ab)
                    
                    print(autos[i].vel)
                    print(autos[i-1].vel)
                    
                    
                    return line,
                if autos[i].vel < 0:
                    print("MINUS")
                    print(i)
                    return line,
                # Stop the animation on collision
            else:
                autos[i].fahren(time_step, 0, 0)
                autos_meter[i] = autos[i].meter 
        
        # Spawn new cars at random intervals
        if spawn_timer >= waiting_time:
            auto_art = auto_typen[randint(0, len(auto_typen)-1)]
            new_car = Auto.create_auto(auto_art, current_time)
            autos.append(new_car)
            autos_meter.append(new_car.meter)
            autos_vel.append(new_car.vel)
            spawn_timer = 0
            waiting_time = randint(5, 10)  # Random waiting time for the next car
        
        # Update the car positions on the plot
        line.set_data(autos_meter, np.zeros_like(autos_meter))  # Using meters for x-axis
        return line,  # Return updated line object
    
    # Create the animation
    
    
    ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)
    

        
    
    
    
    plt.title("Car Simulation")
    plt.xlabel("Distance (meters)")
    plt.ylabel("Cars (y-axis for visibility)")
    plt.show()


while not boom:
    current_time+=time_step
    spawn_timer += time_step
    
    if len(autos) == 1:
        autos[0].fahren(time_step, 0, 0)
        autos_meter[0] = locale.format_string('%.2f', autos[0].meter) 
        autos_vel[0] = locale.format_string('%.2f', autos[0].vel) 
    else:
        for i in range(len(autos)):
            
        
        
            achtung_bool = autos[i-1].back < autos[i].meter + autos[i].wun_ab and autos[i].meter > autos[i].wun_ab
            
            autos[i].fahren(time_step, autos[i-1].back, autos[i-1].vel)
            
            
            if i > 0: 
                if autos[i].meter >= autos[i-1].back and autos[i].meter != 0:
                    boom=True
                    """print("!!BOOM!!")
                    print(i)
                    print(autos[i].spawn_time)
                    print(autos[i-1].spawn_time)
                    print(autos[i].wun_vel)
                    print(autos[i].wun_ab)
                    
                    fh.write("!!BOOM!!")
                    fh.write("\n")
                    fh.write(str(i))
                    fh.write("\n")
                    fh.write(autos[i].typ)
                    fh.write("\n")
                    fh.write(str(autos[i].spawn_time))
                    fh.write("\n")
                    fh.write(str(autos[i-1].spawn_time))
                    fh.write("\n")
                    fh.write(str(autos[i].wun_vel))
                    fh.write("\n")
                    fh.write(str(autos[i].wun_ab))
                    fh.write("\n")"""
            
            if autos[i-1].vel < 0 or autos[i].vel < 0:
                boom = True
                print("!!MINUS!!")
                print(i)
            
                
            
            
                
                
            autos_meter[i] = locale.format_string('%.2f', autos[i].meter) 
            autos_vel[i] = locale.format_string('%.2f', autos[i].vel)
    
    if spawn_timer >= waiting_time:
        """
        fh.write("new car")
        fh.write("\n")
        print("new car")
        """
        auto_art = auto_typen[randint(0, len(auto_typen)-1)]
        autos.append(Auto.create_auto(auto_art, current_time))
        autos_meter.append("0")
        autos_vel.append("0")
        waiting_time = randint(5, 20)
        spawn_timer = 0
        """
        fh.write(auto_art)
        fh.write("\n")
        fh.write(str(len(autos)))
        fh.write("\n")
        
        print(auto_art)
        print(str(len(autos)))
        
        t.sleep(1)
        """
    """
    fh.write(locale.format_string('%.2f', current_time))
    fh.write("\n")
    for i in autos_meter:
        
        fh.write(i)
        fh.write("; ")
    fh.write("\n")
    for i in autos_vel:
        
        fh.write(i)
        fh.write("; ")
    fh.write("\n")
    fh.write("\n")
        
    print(locale.format_string('%.2f', current_time))
    
    print(autos_meter)
    print(autos_vel)
    print()
    
    """
    
    animate_simulation(autos, time_step, spawn_timer, waiting_time)

    
    

    
