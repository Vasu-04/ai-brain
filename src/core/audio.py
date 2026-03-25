import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="output.wav", duration=5, sample_rate=44100):
    print("Recording... Speak now")

    # Record audio
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    # Save audio file
    write(filename, sample_rate, audio)

    print(f"Recording saved as {filename}")

    return filename