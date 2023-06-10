import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import medfilt
import statistics

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class Signal:
    def __init__(self,file,y):
        self.file = file
        self.y = y

    def get_data(self):
        for line in open(f'{self.file}.txt', 'r'):
            self.y.append(float(line))
        median_value = statistics.median(self.y)
        for i in range(0,len(self.y)):
            if abs(self.y[i]) > 30*abs(median_value):
                self.y[i] = median_value
            else:
                continue

        return self.y
    
    def medianfilter(self, kernel):
        self.y = Signal.get_data(self)
        self.y = np.array(self.y)
        self.y = medfilt(self.y, kernel_size= kernel)
        return self.y


class UserInfoSystem(QWidget):
    def __init__(self):
        super().__init__()

        # Create the labels and textboxes
        name_label = QLabel('Name:')
        name_textbox = QLineEdit()
        age_label = QLabel('Age:')
        age_textbox = QLineEdit()
        email_label = QLabel('Email:')
        email_textbox = QLineEdit()

        # Create the submit button
        submit_button = QPushButton('Submit')

        # Create the layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(name_label)
        layout.addWidget(name_textbox)
        layout.addWidget(age_label)
        layout.addWidget(age_textbox)
        layout.addWidget(email_label)
        layout.addWidget(email_textbox)
        layout.addWidget(submit_button)

        self.setLayout(layout)


class LinearSignalPlot(QWidget):
    def __init__(self):
        super().__init__()

        # Create the plot
        y = []
        file = input("Nhập tên file: ")
        y = Signal(file=file,y=y).medianfilter((3))
        x = np.arange(len(y))

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_ylabel('Velocity')

        # Create the canvas to display the plot
        canvas = FigureCanvas(fig)

        # Create the layout and add the canvas
        layout = QVBoxLayout()
        layout.addWidget(canvas)
    
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window properties
        self.setWindowTitle('User Info and Signal Plot App')
        self.setGeometry(100, 100, 1600, 600)

        # Create the widgets
        user_info_widget = UserInfoSystem()
        linear_signal_widget = LinearSignalPlot()

        # Create the layouts
        layout = QHBoxLayout()
        layout.addWidget(user_info_widget)
        layout.addWidget(linear_signal_widget)

        # Set the central widget and layout of the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
