import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


# Generate some data for this demonstration.
data = norm.rvs(10.0, 2.5, size=500)

# Fit a normal distribution to the data:
mu, std = norm.fit(data)

# Plot the histogram.
plt.hist(data, bins=25, density=True, alpha=0.6, color='g', label='Data')
# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2, label='Fit')
plt.xlabel(r"Random variable")
plt.ylabel(r"$\mathrm{PDF}$")
title = r"Fit results: $\mu = %.2f$,  $\sigma = %.2f$" % (mu, std)
plt.title(title)
plt.legend()
plt.show()

