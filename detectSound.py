
import sounddevice as sd
import numpy as np

#parameters 
duration = 0.5 #seconds
threshold = 0.1 #volume threshold

def callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata)
    if volume_norm > threshold:
        print("sound detected")
        
#stream microphone input
with sd.InputStream(callback=callback):
    print("Listening...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Canceled")