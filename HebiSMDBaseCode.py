import hebi, time, csv
import numpy as np
import matplotlib.pyplot as plt

# --- SMD parameters ---
k = 20.0     # N  m/rad
c = 0.1      # Nms/rad
m = 0.01     # virtual mass, kg·m^2
dt = 0.01    # control timestep
t = 0

# --- Safety limits ---
max_torque = 3.0
max_displacement = 1.5

# External input function
def external_input(t):
    # Example: Step torque of 1.0 Nm after 2 s
    return 0.0 

# --- Setup HEBI ---
lookup = hebi.Lookup()
time.sleep(2)
group = lookup.get_group_from_names(['Nimbus'], ['Arm_M3'])
if group is None:
    raise RuntimeError("Could not find HEBI module Nimbus / Arm_M3")
group_command = hebi.GroupCommand(group.size)
group_feedback = hebi.GroupFeedback(group.size)

# --- Initial position as zero ---
group.get_next_feedback(reuse_fbk=group_feedback)
zero_pos = group_feedback.position[0]

# --- Variables ---
u = 0

# Data logs
time_log = []
pos_log  = []   # measured position
torque_log = [] # commanded torque
u_log = []      # input force/torque

print("Starting Loop")
try:
    while True:
        group.get_next_feedback(reuse_fbk=group_feedback)
        pos_raw = group_feedback.position[0]
        vel = group_feedback.velocity[0]

        # External input
        u = external_input(t)

        # Displacement relative to initial
        pos = pos_raw - zero_pos

        # Compute Torque
        if abs(pos) > max_displacement:
            torque = 0.0
            print("⚠️ Displacement limit exceeded! Torque disabled.")
        else:
            torque = 0.0 # Calculate torque
            torque = max(min(torque, max_torque), -max_torque)
        # Send Command
        group_command.effort = [torque]
        group.send_command(group_command)
        
        #Logging
        time_log.append(t)
        pos_log.append(pos)
        torque_log.append(torque)
        u_log.append(u)

        #Time Step
        time.sleep(dt)
        t=t+dt
except KeyboardInterrupt:
    print("Interrupted by user — setting effort to 0 and exiting.")
finally:
    # Safe Shutdown
    group_command.effort = [0.0]
    group.send_command(group_command)

    # Save logs to CSV
    fname = "hebi_smd_log.csv"
    with open(fname, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time","pos","torque","u"])
        for row in zip(time_log, pos_log, torque_log, u_log):
            writer.writerow(row)
    print(f"Log saved to {fname}")


    # Use numpy.genfromtxt for robust CSV reading
    data = np.genfromtxt(fname, delimiter=',', names=True)  # names=True uses header

    time = data['time']
    pos = data['pos']
    torque = data['torque']
    u = data['u']

    # -------------------------
    # Plotting
    # -------------------------
    plt.figure(figsize=(10,6))

    # Position
    plt.subplot(2,1,1)
    plt.plot(time, pos, label='Position [rad]')
    plt.title("HEBI SMD Experiment")
    plt.xlabel("Time [s]")
    plt.ylabel("Displacement [rad]")
    plt.grid(True)
    plt.legend()

    # Torque + Input
    plt.subplot(2,1,2)
    plt.plot(time, torque, label='Torque Command [Nm]')
    plt.plot(time, u, '--', label='External Input [Nm]')
    plt.xlabel("Time [s]")
    plt.ylabel("Torque [Nm]")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()