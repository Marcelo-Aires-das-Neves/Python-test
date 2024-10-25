import matplotlib.pyplot as plt
import numpy as np

# Correctly specifying the figure size
plt.figure(figsize=(7, 5))

# Generating x values
x = np.linspace(-10, 10, 1000)

# Computing the sigmoid and tanh functions
sig = 1/(1 + np.exp(-x))
tanh = np.tanh(x)

plt.subplot(1,2,1)
plt.title("Sigmoide")
plt.xlabel('X')
plt.ylabel('Sig')
plt.plot(x, sig)

plt.subplot(1,2,2)
plt.title("Tanh")
plt.xlabel('X') 
plt.ylabel('Tanh')
plt.plot(x, tanh, '--', color='red')   

# Displaying the plot
plt.show()