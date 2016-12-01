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
import kursovaya
app = QApplication(sys.argv)
form = kursovaya.Main()
sizeform = form.geometry()
form.setGeometry(300,300,350,250)
form.show()
if __name__=='__main__':
	sys.exit(app.exec_())