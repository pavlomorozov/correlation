import scipy.signal as signalLib
import numpy
import WaveReader as reader
import matplotlib.pyplot as plt

def correlate(array1, array2):
    correlation = signalLib.correlate(array1, array2, mode='full', method='fft')
    return correlation

path1 = "./samples/440Hz_44100Hz_16bit_05sec.wav"
path2 = "./samples/440Hz_44100Hz_16bit_05sec.wav"

readerObject = reader.WavReader
# signal1 = readerObject.read_scipy_wavfile(path1)
# signal2 = readerObject.read_scipy_wavfile(path2)

signal1 = readerObject.read_wave(path1)
signal2 = readerObject.read_wave(path2)
window_size = 100

window1 = signal1[0: window_size]/20000

eof = False
index = 0

window2 = signal2[index: index + window_size]/20000
#index = int(index + window_size/2)
# correlation = correlate(window1, window2)
correlation = numpy.correlate(window1, window2, "same")
# correlation = numpy.correlate([1,3,2,7,1], [2,6,4,14,2], "same")
# correlation = numpy.correlate([1,3,2,5,7,2,11,4,5], [1,3,2,5,7,2,11,4,5], "same")

fig, axs = plt.subplots(3)
fig.suptitle('Signals and correlation')
axs[0].plot(window1)
axs[1].plot(window2)
axs[2].plot(correlation)

# plt.figure(1)
# plt.title("Correlation")
# plt.plot(correlation)
plt.show()