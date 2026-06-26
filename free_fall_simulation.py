import matplotlib.pyplot as plt
import numpy as np

# Constants
g = -9.81  # Acceleration due to gravity (m/s^2)
t = 0  # Time (s)
y = 100.0  # Initial height (m)
v = 0.0  # Initial velocity (m/s)
dt = float(input("Enter the time step: "))  # Time step (s)

# Lists
time_list = []
euler_height_list = []
timestep_list = []
analytical_height_list = []
dt_values = [0.01, 0.05, 0.1, 0.5, 1.0]
mean_error_values = []
max_error_values = []
error_list = []
error_list.append(0.0) # Starting error at t=0

# Append the starting conditions to the lists
time_list.append(t)
euler_height_list.append(y)
timestep_list.append(dt)
analytical_height_list.append(y)  # Initial height for analytical solution

while y > 0:
    # Update velocity, position, and time using Euler's method
    y += v * dt  # Update height
    v += g * dt  # Update velocity
    t += dt # Update time

    # Calculate the exact height using the analytical solution
    y_exact = 100.0 + (0.0 * t) + (0.5 * g * t**2)
    analytical_height_list.append(y_exact)

    current_error = abs(y - y_exact)
    error_list.append(current_error)

    # Append the current time, height, and time step to the lists
    timestep_list.append(dt)
    time_list.append(t)
    euler_height_list.append(y)

# ERROR VS. TIMESTEP

# testing machine loop
for test_dt in dt_values:
    
    # Reset the starting conditions for each test
    t_test = 0.0
    y_test = 100.0
    v_test = 0.0

    current_run_errors = []
    
    # Run the drop simulation for this specific dt
    while y_test > 0:
        y_test += v_test * test_dt
        v_test += g * test_dt
        t_test += test_dt
        
        # Calculate the exact height to compare against later
        y_exact_test = 100.0 + (0.0 * t_test) + (0.5 * g * t_test**2)

        step_error = abs(y_test - y_exact_test)
        current_run_errors.append(step_error)
        
    mean_error = np.mean(current_run_errors)
    max_error = np.max(current_run_errors)
    mean_error_values.append(mean_error)
    max_error_values.append(max_error)

# Plotting the results

# Figure 1
plt.plot(time_list, euler_height_list, label=f"Euler Method (dt={dt}s)", color="blue", linestyle="--")
plt.plot(time_list, analytical_height_list, label="Analytical (Exact)", color="red", linestyle="-")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Figure 1: Euler vs. Analytical Solution of Free Fall")
plt.legend()
plt.grid(True)

# Figure 2
plt.figure()
plt.plot(time_list, error_list, label=f"Error (dt={dt}s)", color="purple", linestyle="-")
plt.xlabel("Time (s)")
plt.ylabel("Position Error (m)")
plt.title(f"Figure 2: Position Error vs. Time (dt={dt}s)")
plt.legend()
plt.grid(True)

# Figure 3
plt.figure() 
plt.plot(dt_values, mean_error_values, marker="o", color="green", linestyle="-", label="Mean Error")
plt.plot(dt_values, max_error_values, marker="s", color="orange", linestyle="--", label="Max Error")
plt.xlabel("Timestep Size 'dt' (s)")
plt.ylabel("Position Error (m)")
plt.title("Figure 3: Simulation Error vs. Timestep Size")
plt.legend()
plt.grid(True)

print("\n==============================================")
print("             SIMULATION RESULTS               ")
print("==============================================")
print("Timestep (s)  |  Mean Error (m)  |  Max Error (m)")
print("----------------------------------------------")

# Loop through the lists and print each row
for i in range(len(dt_values)):
    dt_str = f"{dt_values[i]:<13}"
    mean_str = f"{mean_error_values[i]:<16.4f}"
    max_str = f"{max_error_values[i]:.4f}"
    
    print(f"{dt_str} | {mean_str} | {max_str}")

print("==============================================\n")

plt.show()