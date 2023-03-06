import librosa
import numpy as np
import soundfile as sf

# Load the audio file
filename = "audio_data/in_the_end_audio.mp3"
audio, sr = librosa.load(filename, sr=None)

# Convert the audio signal to a numerical representation
audio_int = np.int16(audio * 32767) # Convert to 16-bit integers

# Define the number of bits to use for quantization
num_bits = 2

# Calculate the range of values that can be represented by the chosen number of bits
quantization_range = 2**(num_bits - 1)

# Quantize the audio signal
quantized_audio = np.round(audio_int / (32767/quantization_range))

# Convert the quantized signal back to 16-bit integers
quantized_audio_int = np.int16(quantized_audio * (32767/quantization_range))

# Save the quantized audio file using soundfile
sf.write("in_the_end_outs/in_the_end_2bit.wav", quantized_audio_int, sr, subtype='PCM_16')
