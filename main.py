import numpy as np
import matplotlib.pyplot as plt

# Model parameters
beta = 0.3  # Infection rate
gamma = 0.1  # Recovery rate
mu = 0.02  # Death rate

# Initial conditions
S0 = 0.99  # Initial susceptible fraction
I0 = 0.01  # Initial infectious fraction
R0 = 0.0   # Initial recovered fraction
D0 = 0.0   # Initial died fraction

# Total population
N = 1000  # Total population size

# Discrete time step (stride)
dt = 0.1

# Number of time steps
T = 209
num_steps = int(T / dt)

# Arrays to store results
S = [S0 * N]
I = [I0 * N]
R = [R0 * N]
D = [D0 * N]

# Simulation loop
for _ in range(num_steps):
    dS = -beta * S[-1] * I[-1] * dt
    dI = (beta * S[-1] - gamma - mu) * I[-1] / N * dt
    dR = gamma * I[-1] * dt
    dD = mu * I[-1] * dt

    S.append(S[-1] + dS)
    I.append(I[-1] + dI)
    R.append(R[-1] + dR)
    D.append(D[-1] + dD)

# Time array
t = np.arange(0, T + dt, dt)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Susceptible')
plt.plot(t, I, label='Infectious')
plt.plot(t, R, label='Recovered')
plt.plot(t, D, label='Died')
plt.xlabel('Time')
plt.ylabel('Fraction of Population')
plt.legend()
plt.title('SIRD Model with Discrete Time Steps')
plt.show()