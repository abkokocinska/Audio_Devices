
#this is a basic audio recorder. The output is a simple .wav file.

#install neccessary devices. We have to install 3 modules to set
#up the tools for building a recorder.
pip install sounddevice 

pip install wavio

pip install scipy


# First you import required libraries
import sounddevice as sd 
from scipy.io.wavefile import write
import wavio as wv  

# Here is the Sampling frequency
freq: 44100

# Here is the Recording duration 
duration = 5

# Now start recorder with the given values 
# of duration and sample frequency 
recording = sd.rec(int(duration*freq,)
           samplerate=freq, channels=2) 

#Next we will record audio for the given number of seconds
sd.wait()

#Below,this will convert the NumPy array to an audio 
#file that is a .wav file, with the given sampling frequency 
write("recording0.wav, freq, recording")

#After, we will convert the NumPy array to audio file 
wv.write("recording1.wav",recording, freq, samplewidth=2)

#tellthe user they aredone recording 
print("you are done recording.")

           