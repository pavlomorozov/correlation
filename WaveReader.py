import numpy as np
import wave
import sys
import scipy.io.wavfile as scipy_wavfile

class WavReader:
    # mono file
    def read_wave(path):

        spf = wave.open(path, "r")
        # Extract Raw Audio from Wav File
        signal = spf.readframes(-1)
        signal = np.fromstring(signal, np.int16)

        # If Stereo
        if spf.getnchannels() == 2:
            print("Just mono files")
            sys.exit(0)

        return signal

    # stereo file
    def read_scipy_wavfile(path):
        # data = wf.read(path)
        # for frame in data[1]:
        #     data = np.append(data, frame[0])

        rate, data = scipy_wavfile.read(path)
        # data0 is the data from channel 0.
        data0 = data[:, 0]
        # data1 = data[:, 1]
        return data0
