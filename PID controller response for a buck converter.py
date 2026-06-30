import numpy as np
import matplotlib.pyplot as plt

# PID Controller for Buck Converter Output Voltage Regulation
# Simulating response to a load step disturbance

# System parameters
Vref = 12.0      # Reference/desired output voltage (V)
dt = 1e-5        # Time step (10 microseconds)
t_end = 0.05     # Simulation time (50ms)
t = np.arange(0, t_end, dt)

# PID gains — tune these
Kp = 500  # Proportional gain
Ki = 1000 # Integral gain
Kd = 0.01     # Derivative gain

# Initialize arrays
Vout = np.zeros(len(t))
error = np.zeros(len(t))
integral = 0
derivative = 0
prev_error = 0

# Simulate
for i in range(1, len(t)):
    # Load disturbance — step drop at t=10ms, recovery at t=30ms
    if t[i] < 0.01:
        disturbance = 0
    elif t[i] < 0.03:
        disturbance = -2.0   # Voltage drops by 2V due to load step
    else:
        disturbance = 0

    # PID calculation
    error[i] = Vref - Vout[i-1]
    integral += error[i] * dt
    derivative = (error[i] - prev_error) / dt
    
    # PID output (duty cycle correction)
    correction = Kp * error[i] + Ki * integral + Kd * derivative
    
    # Update output voltage
    Vout[i] = Vout[i-1] + correction * dt + disturbance * dt
    prev_error = error[i]

# Plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle('PID Controller — Buck Converter Voltage Regulation', fontweight='bold')

ax1.plot(t*1000, Vout, color='blue', label='Vout with PID')
ax1.axhline(y=Vref, color='red', linestyle='--', label='Vref = 12V')
ax1.axvline(x=10, color='gray', linestyle=':', label='Load step')
ax1.axvline(x=30, color='gray', linestyle=':')
ax1.set_xlabel('Time (ms)')
ax1.set_ylabel('Output Voltage (V)')
ax1.set_title('Output Voltage Response')
ax1.legend()
ax1.grid(True)

ax2.plot(t*1000, error, color='green')
ax2.axhline(y=0, color='black', linewidth=0.5)
ax2.set_xlabel('Time (ms)')
ax2.set_ylabel('Error (V)')
ax2.set_title('Error Signal')
ax2.grid(True)

plt.tight_layout()
plt.show()