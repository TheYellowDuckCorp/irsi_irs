from filters import fir_filter, iir_filter, fourier_transform
from scipy.signal import freqz
from numpy import cos, sin, pi, absolute, arange
import numpy as np
from matplotlib import pyplot as plt

if __name__ "__main__":
    #create signal
    np.random.seed(42) #for reproducibility
    #create time steps and corresponding sine wave with gaussian noise
    fs=80 #sampling rate HZ
    ts=np.arange(0,5,1.0 / fs) #timevector - 5sec
    x_t = np. sin(2*np.pi * 1 * ts) # signal @ 1.0 Hz, without noise
    noise = 0.2*sin (2*pi*15.3*ts) + 0.1*sin (2*pi *16.7*ts + 0.1) + 0.1*sin (2*pi *23.45 *ts+.8)
    #noise = 0.5 * np. random. normal (size-len (ts)) # Gaussian noise
    x_noise = x_t + noise

    # plot raw signal
    plt.figure (figsize= (6.4, 2.4))
    plt.plot(ts, x_t, alpha=0.8, lw=3, color="C1", label="Clean signal (ys)")
    plt.plot(ts, x_noise, color="C0", label="Noisy signal (x noise)")
    plt.xlabel("Time / 5")
    plt.ylabel("Amplitude")
    plt.legend(loc="lower center", bbox_to_anchor= [0.5, 11], ncol=2, fontsize="smaller")
    plt.tight_layout()
    plt.show()