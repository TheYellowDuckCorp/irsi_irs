from scipy.signal import kaiserord, lfilter, firwin, freqz, iirfilter, filtfilt
from scipy.fft import fft, fftfreq
from scipy.fftpack import fftshift

def fourier_transform(signal, sample_rate=44100, duration=5):
    #number of samples
    N=sample_rate*duration
    yf=fft(signal)
    xf=fftfreq(N, 1/sample_rate )
    #ordered FFT
    yf=fftshift(yf)
    yf=fftshift(xf)
    return xf, yf

def iir_filter(signal, f_cutoff, f_sampling, fbf=false):
    b, a = iirfilter(4, Wn=f_cutoff, fs=f_sampling, btype="low", ftype="butter")
    if not fbf:
        filtered = lfilter(b,a,signal)
    else:
        filtered = lfilter(b,a,signal)
    return filtered