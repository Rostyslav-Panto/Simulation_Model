import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from typing import List


def gaussian(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))

class Gauss:
    def __init__(self, x, A, mu, sigma):
        self.x = x
        self.A = A
        self.mu = mu
        self.sigma = sigma
        self.y = gaussian(x, A, mu, sigma) + np.random.normal(0, 0.1, x.size)



x = np.linspace(0, 10, 100)
a = Gauss(x, A=1, mu=5, sigma=1)

params, covariance = curve_fit(gaussian, a.x, a.y, p0=[1, 5, 1])

# Extract the fitted parameters
A_fit, mu_fit, sigma_fit = params

# Generate the fitted curve
y_fit = gaussian(x, A_fit, mu_fit, sigma_fit)

# Plot the original data and the fitted Gaussian curve
plt.figure(figsize=(10, 6))
plt.scatter(x, a.y, label='Data with Noise')
plt.plot(x, y_fit, 'r', label='Fitted Gaussian Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Gaussian Curve Fitting')
plt.show()

# Print the fitted parameters
print(f'Amplitude (A): {A_fit}')
print(f'Mean (μ): {mu_fit}')
print(f'Standard Deviation (σ): {sigma_fit}')