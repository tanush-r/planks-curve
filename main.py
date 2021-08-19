import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

wavelength_x = np.linspace(0.1, 1.6, 100) * (10 ** -6)

temperature_range = range(3000, 6001, 1000)
colors = "r g b y".split()

h = 6.62 * (10**-34)
c = 3 * (10**8)
e = 2.718
k = 1.38*(10**-23)

count = 0
for temp in temperature_range:
    energy_density_y = ((8*3.14*h*c)/(wavelength_x**5))*(1/(e**(h*c/(wavelength_x*k*temp))-1))
    axes.plot(wavelength_x, energy_density_y, color=colors[count], label=str(temp), lw=3)
    count += 1

axes.plot(0.38 * (10 ** -6), 0, color="black", label="Visible Spectrum", lw=1, alpha=0.5)
axes.plot(0.7 * (10 ** -6), 0, color="black", lw=1, alpha=0.5)

axes.set_xlabel("Wavelength λ [m]")
axes.set_ylabel("Energy Density u(λ) [J m-4]")
axes.set_title("Black Body Radiation Spectrum")

axes.set_xlim(0.1 * (10 ** -6), 1.6 * (10 ** -6))
axes.set_ylim(0, 1500000)

axes.legend()

plt.show()
