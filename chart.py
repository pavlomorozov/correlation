import matplotlib.pyplot as plt
import WaveReader as reader

# "440Hz_44100Hz_16bit_05sec.wav"
path = "./samples/third.wav"

readerObject = reader.WavReader
signal = readerObject.read_scipy_wavfile(path)

# path = "./samples/440Hz_44100Hz_16bit_05sec.wav"
# signal = read_wave(path)

plt.figure(1)
plt.title("Signal Wave...")
slice = signal[0: 10000]
plt.plot(slice)
plt.show()
