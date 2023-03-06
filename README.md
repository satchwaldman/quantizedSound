# quantizedSound

This is a repository for quantizing an audio file (.mp3) and returning a returning an n-bit quantized audio file (.wav), where n is specified by the user.

In order to run the code, follow the following steps:
1. Clone this repository using "git clone SSH_LINK" where HTTPS_LINK is the link to the github repository 
2. Install Librosa and Numpy in the command line using "pip install numpy" and "pip install librosa"
3. Optionally, update librosa using "pip install --upgrade librosa"
4. To convert a new song, drag it into the "audio_data" folder. Go to soundQuantizer.py and change the "num_bits" variable to the desired number of bits. 
5. If converting a new song, create a new folder, perhaps called "SONG_NAME"_outputs
6. Ensure that the proper filepaths are written, both in the "filename" variable and in "sf.write("OUTPUT_FILEPATH", quantized_audio_int, sr, subtype='PCM_16')". 
7. Run the soundQuantizer script.
8. Collect your files in the folder you created in step 5.