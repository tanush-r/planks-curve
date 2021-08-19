import numpy as np
import matplotlib.pyplot as plt

# Create figure object
fig = plt.figure(figsize=(8, 5), dpi=200)

# Add axes
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Generate wavelength, temperature, and colors
wavelength_x = np.linspace(0.1, 1.6, 100)
temperature_range = range(3000, 6001, 1000)
colors = "#99ff00 #ffee00 #ff8000 #ff0000".split()

# Constants
h = 6.62 * (10 ** -34)  # Planck's constant
c = 3 * (10 ** 8)   # Speed of light
e = 2.718   # Exponent
k = 1.38 * (10 ** -23)  # Boltzmann's constant

# Counter and max values co-ordinate lust
count = 0
max_x = list()
max_y = list()

# Looping for each temperature
for temp in temperature_range:
    # Convert temperature to metres
    wavelength_x_metre = wavelength_x * (10 ** -6)

    # Apply energy density formula
    energy_density_y = ((8 * 3.14 * h * c) / (wavelength_x_metre ** 5)) * (
                1 / (e ** (h * c / (wavelength_x_metre * k * temp)) - 1))
    # Plot curve
    axes.plot(wavelength_x, energy_density_y, color=colors[count], label=str(temp), lw=3)

    # Max value co-ordinates and append to list
    max_y_val = energy_density_y.max()
    max_x_val = wavelength_x[energy_density_y == max_y_val][0]
    max_x.append(max_x_val)
    max_y.append(max_y_val)

    # Counter
    count += 1

# Convert to numpy array
max_x_np = np.array(max_x)
max_y_np = np.array(max_y)

# Visible spectrum black borders
visible_spectrum_x1 = np.ones(100) * 0.38
visible_spectrum_x2 = np.ones(100) * 0.7
visible_spectrum_y = np.linspace(0, 1500000, 100)

axes.plot(visible_spectrum_x1, visible_spectrum_y, color="black", lw=2, alpha=0.75)
axes.plot(visible_spectrum_x2, visible_spectrum_y, color="black", lw=2, alpha=0.75)

# Visible spectrum blue span
axes.plot(max_x_np, max_y_np, color="grey", label="λ max", lw=2, ls="--", marker="o", markersize=8)
axes.axvspan(0.38, 0.7, alpha=0.25, color='cyan', label="Visible Spectrum")

# Labels and title
axes.set_xlabel("Wavelength λ [μm]")
axes.set_ylabel("Energy Density u(λ) [J m-4]")
axes.set_title("Black Body Radiation Spectrum")

# Set Limits and legend
axes.set_xlim(0.1, 1.6)
axes.set_ylim(0, 1500000)
axes.legend()

# Save fig in res folder
fig.savefig("res\\plancks_curve.png", dpi=200)

# Show graph
plt.show()
