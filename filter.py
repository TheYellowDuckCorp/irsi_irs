from scipy.signal import kaiserord, lfilter, firwin, freqz, iirfilter, filtfilt 
from scipy.fft import fft, fftfreq
from scipy. fftpack import fftshift

def fourier_transform(signal, sample_rate=44100, duration=5):
    # Number of samples
    N = sample_rate * duration
    yf = fft (signal)
    xf = fftfreq(N, 1 / sample_rate)
    # Ordered FFT
    yf = fftshift(yf)
    xf = fftshift(xf)
    return xf, yf

def iir_filter(signal, f_cutoff, f_sampling, fbf=False):
    b, a = iirfilter(4, Wn =f_cutoff, fs = f_sampling, btype="low", ftype="butter")
    if not fbf:
        filtered = lfilter(b, a, signal)
    else:
        filtered = filtfilt(b, a, signal)
    return filtered

def fir_filter(signal, nyq_rate, f_cutoff):
    #Window Width
    width = 5.0/nyq_rate
    #The desired attenuation in the stop band, in dB
    ripple_db = 60.0