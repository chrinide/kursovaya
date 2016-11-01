import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

wav = wave.open("Temple.wav", mode="r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()

duration = nframes / framerate
w, h = 800, 300
k = nframes/w/32
DPI = 72
peak = 256 ** sampwidth / 2

content = wav.readframes(nframes)
samples = np.fromstring(content, dtype=types[sampwidth])
max_plot = 0
middle = 0
plus_plot = 0
for n in range(nchannels):
    channel = samples[n::nchannels]
    channel = channel[0::k]
    for plot in range(len(channel)):
    	if channel[plot] > 0:
    	    middle = middle + 1
    	    plus_plot = plus_plot + channel[plot]
    	if channel[plot]>max_plot:
    		max_plot=channel[plot]
    if nchannels == 1:
        channel = channel - peak

middle_plot = int(plus_plot/middle)	
melod = int(max_plot/middle_plot)
if melod>5:
	print("Melodious")
else:
	print("Tuneless")
