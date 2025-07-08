import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

fs = 1000  # Sampling frequency
f_clean = 10
f_noise = 100  # Frequency of noise

t = np.linspace(0,1,fs,endpoint = False)  # Time vector
x_clean = np.sin(2 * np.pi * f_clean * t)  # Clean signal
x_noise = np.sin(2 * np.pi * f_noise * t)  # Noise signal
x = x_clean + x_noise  # Noisy signal


# Design a low-pass FIR filter
cutoff = 20  # Cutoff frequency
numtaps = 101  # Number of filter taps
nyquist = fs/2  # Nyquist frequency
normalized_cutoff = cutoff / nyquist  # Normalized cutoff frequency
b = signal.firwin(numtaps, normalized_cutoff,window='hamming')  # FIR filter coefficients   

filtered_signal = signal .convolve(x,b,mode='same')  # Apply the filter to the noisy signal
# Plot the signals
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, x_clean, label='Clean Signal', color='blue')
plt.title('Clean Signal')


plt.subplot(3, 1, 2)
plt.plot(t, x, label='Noisy Signal', color='red')
plt.plot(t, x_clean, label='Clean Signal', color='blue', linestyle='--')
plt.legend()
plt.title('Noisy Signal')


plt.subplot(3, 1, 3)
plt.plot(t, filtered_signal, label='Filtered Signal', color='green')
plt.title('Filtered Signal')
plt.tight_layout()
plt.show()

