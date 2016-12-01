import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
import scipy.signal as sg
import sys
import shutil
import os
from PyQt5.QtWidgets import QWidget, QApplication, QAction, qApp, QTextEdit, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QListWidget, QFileDialog
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import QCoreApplication
from os.path import isfile, join
import func
class Main(QWidget):
	def __init__(self, parent=None):
		super(Main,self).__init__(parent)
		self.initUI()
	def initUI(self):
		self.all_files1 = []
		self.select1 = QPushButton('Выбрать папку',self)
		self.folder1 = QListWidget()
		self.folder2 = QListWidget()
		label1 = QLabel('Мелодичные',self)
		label2 = QLabel('Немелодичные',self)

		vbox1 = QVBoxLayout()
		vbox2 = QVBoxLayout()
		hbox = QHBoxLayout()
		vbox = QVBoxLayout()
		vbox1.addWidget(label1)
		vbox1.addWidget(self.folder1)
		vbox2.addWidget(label2)
		vbox2.addWidget(self.folder2)
		hbox.addLayout(vbox1)
		hbox.addLayout(vbox2)
		vbox.addLayout(hbox)
		vbox.addWidget(self.select1)

		self.setLayout(vbox)
		self.select1.clicked.connect(self.set_folder)

		self.setGeometry(400,400,500,650)
		self.setWindowTitle('Курсовая')
		self.show()
	def set_folder(self):
		directory = QFileDialog.getExistingDirectory(self,'Выбор папки','C:\Python')
		files_list = os.listdir(directory)
		self.all_files1 = []
		X = np.array([[11999, 3, 1],[10747, 4, 1],[10211, 3, 1],[10888, 3, 1],[9315, 4, 1],[9055, 3, 1],[8370, 3, 1],[5000, 5, 1],[2165, 10, 2],[2792, 9, 2],[3127, 7, 2],[1670, 9, 2],[2693, 8, 2],[2459, 7, 2],[1735, 14, 2],[2196, 9, 2],[1823, 8, 2],[3277, 7, 2]])

		for file in files_list:
			path = os.path.join(directory, file)
			size = os.path.getsize(path)
			self.dir1 = directory
			if isfile(path):
				self.all_files1.append({
					"path": path,
					"size": size,
					"ext": (os.path.splitext(path)[1])[1:]
				})
		self.folder1.clear()
		self.folder2.clear()
		for file in self.all_files1:				
			if isfile(file['path']) and file['ext']=='wav':
				types = {
    				1: np.int8,
    				2: np.int16,
    				4: np.int32
					}
				wav = wave.open(file['path'], mode="r")
				(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
				#Число каналов, число байт на сэмпл, число фреймов в секунду, общее число фреймов, тип сжатия, имя типа сжатия

				duration = nframes / framerate
				w, h = 800, 300
				k = int(nframes/w/32)
				DPI = 72
				peak = 256 ** sampwidth / 2

				content = wav.readframes(nframes)
				samples = np.fromstring(content, dtype=types[sampwidth])
				max_plot = 0
				middle = 0
				for n in range(nchannels):
					channel = samples[n::nchannels]
					channel = channel[0::k]
					signal = np.zeros(len(channel))
					if nchannels == 1:
						channel = channel - peak
					for sig in range(len(channel)):
						signal[sig]=math.fabs(channel[sig])
						if signal[sig]>max_plot:
							max_plot=signal[sig]
						middle = middle + signal[sig]
					sign = sg.triang(duration)
					filtered = sg.convolve(signal,sign)
				razn1=0
				middle = middle/(2*len(signal))
				middle_plot = int(max_plot/middle)
				for plots in range(len(filtered)-1):
					razn = math.fabs(filtered[plots]-filtered[plots+1])
					if razn>razn1:
						razn1=razn
				obj = np.array([razn1, middle_plot])
				k = 3
				object_class = func.k_nearest(X, k, obj)
				if object_class == 1:
					self.folder2.addItem(file['path'])
				else:
					self.folder1.addItem(file['path'])

if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())
