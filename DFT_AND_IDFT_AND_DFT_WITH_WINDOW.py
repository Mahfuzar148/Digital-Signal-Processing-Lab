#DFT of xa(t)=sin(2π⋅1000t)+0.5sin(2π⋅2000t+4π). Also IDFT. DFT with
#window + window function realization.


import numpy as np
import matplotlib.pyplot as plt



# Parameters
fs = 8000              # Sampling frequency in Hz
N = 64                 # Number of samples
T = 1 / fs             # Sampling period
n = np.arange(N)       # Discrete time indices
t = n * T              # Time vector  
#  time vector is simply a list of those time points.

# Signal: x(t) = sin(2π·1000·t) + 0.5·sin(2π·2000·t + 4π)
# Since sin(θ + 4π) = sin(θ), we ignore the 4π
x = np.sin(2 * np.pi * 1000 * t) + 0.5 * np.sin(2 * np.pi * 2000 * t)

# 1. DFT
X = np.fft.fft(x)
freqs = np.fft.fftfreq(N, d=T)

# 2. IDFT
x_idft = np.fft.ifft(X)

# 3. Windowing with Hamming window
hamming_window = np.hamming(N)
x_windowed = x * hamming_window

# 4. DFT of windowed signal
X_windowed = np.fft.fft(x_windowed)

# Plotting
plt.figure(figsize=(14, 10))

# Original signal
plt.subplot(3, 2, 1)
plt.plot(t * 1000, x, marker='o')
plt.title("Original Signal x[n]")
plt.xlabel("Time [ms]")
plt.grid()

# DFT magnitude
plt.subplot(3, 2, 2)
plt.stem(freqs[:N//2], np.abs(X)[:N//2])  # DFT Magnitude
plt.title("DFT Magnitude Spectrum |X[k]|")
plt.xlabel("Frequency [Hz]")
plt.grid()

# Reconstructed signal from IDFT
plt.subplot(3, 2, 3)
plt.plot(t * 1000, x_idft.real, marker='x')
plt.title("Reconstructed Signal from IDFT")
plt.xlabel("Time [ms]")
plt.grid()

# Hamming window
plt.subplot(3, 2, 4)
plt.plot(hamming_window)
plt.title("Hamming Window")
plt.grid()

# Windowed signal
plt.subplot(3, 2, 5)
plt.plot(t * 1000, x_windowed)
plt.title("Windowed Signal x[n] * w[n]")
plt.xlabel("Time [ms]")
plt.grid()

# DFT of windowed signal
plt.subplot(3, 2, 6)
plt.stem(freqs[:N//2], np.abs(X_windowed)[:N//2])  # DFT Magnitude of windowed signal
plt.title("DFT of Windowed Signal")
plt.xlabel("Frequency [Hz]")
plt.grid()

plt.tight_layout()
plt.show()
