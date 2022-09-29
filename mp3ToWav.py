from pydub import AudioSegment
# sound = AudioSegment.from_mp3("./samples/first.mp3")
# sound.export("./samples/first_96.0 kb_s.wav", bitrate="96.0 kb/s", format="wav")

sound = AudioSegment.from_mp3("./samples/first.mp3")
sound.export("./samples/first.wav", format="wav")
sound = AudioSegment.from_mp3("./samples/third.mp3")
sound.export("./samples/third.wav", format="wav")