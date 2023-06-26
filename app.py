import sys
import numpy as np
import statistics
import matplotlib.pyplot as plt
from scipy.signal import medfilt

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class Signal(QWidget):
    """
    Get data from file
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('File Dialog Example')

        # Create a LineEdit widget
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(20, 20, 260, 30)

        # Create a button to open the file dialog
        self.btn_open = QPushButton('Open', self)
        self.btn_open.setGeometry(290, 20, 80, 30)
        self.btn_open.clicked.connect(self.showFileDialog)

        self.show()

    def showFileDialog(self):
        # Open the file dialog and get the selected file path
        file_path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text Files (*.txt)")
        # Update the LineEdit widget with the file path
        self.line_edit.setText(file_path)

        # Open the file and read its contents, split into lines and convert to a list of floats
        with open(file_path, 'r') as f:
            values_list = [float(line) for line in f.read().splitlines()]

        #huge noise filter
        median_value = statistics.median(values_list)
        for i in range(0,len(values_list)):
            if abs(values_list[i]) > 30*abs(median_value):
                values_list[i] = median_value
            else:
                continue

        return values_list
    
    def medianfilter(self):
        # median filter noise 
        values = Signal.showFileDialog(self)
        values = np.array(values)
        values = medfilt(values, kernel_size= (3))
        return values


class UserInfoSystem(QWidget):
    """
    User information window
    """
    def __init__(self):
        super().__init__()
        # Font 
        font = QFont("Arial", 12, QFont.Normal)

        # Create box 1
        group_box_1 = QGroupBox("Patent Information")
        layout_1 = QVBoxLayout()

        # Create the labels and textboxes
        ID_label = QLabel("Patent's ID:")
        ID_label.setFont(font)
        ID_textbox = QLineEdit()
        ID_textbox.setFixedSize(350, 20)
        name_label = QLabel("Patent's Name:")
        name_label.setFont(font)
        name_textbox = QLineEdit()
        name_textbox.setFixedSize(350, 20)
        age_label = QLabel("Patent's Age:")
        age_label.setFont(font)
        age_textbox = QLineEdit()
        age_textbox.setFixedSize(350, 20)
        gender_label = QLabel("Patent's Gender:")
        gender_label.setFont(font)
        gender_textbox = QLineEdit()
        gender_textbox.setFixedSize(350, 20)

        # Create the submit button
        submit_button = QPushButton('Submit')
        submit_button.setFixedSize(350,40)


        # Create the layout and add the widgets
        layout_1.addWidget(ID_label)
        layout_1.addWidget(ID_textbox)
        layout_1.addWidget(name_label)
        layout_1.addWidget(name_textbox)
        layout_1.addWidget(age_label)
        layout_1.addWidget(age_textbox)
        layout_1.addWidget(gender_label)
        layout_1.addWidget(gender_textbox)
        layout_1.addWidget(submit_button)

        group_box_1.setLayout(layout_1)
        group_box_1.setStyleSheet("QGroupBox {font-size: 18px;font-weight: bold; }")
        group_box_1.setFixedHeight(400)

        # Creat box 2
        group_box_2 = QGroupBox("Physician's Notes")
        layout_2 = QVBoxLayout()

        # Create the labels and textboxes
        Doctor_label = QLabel('Note:')
        Doctor_label.setFont(font)
        Doctor_textbox = QLineEdit()
        Doctor_textbox.setFixedSize(350, 300)

        # Create the layout and add the widgets
        layout_2.addWidget(Doctor_label)
        layout_2.addWidget(Doctor_textbox)
        group_box_2.setLayout(layout_2)
        group_box_2.setStyleSheet("QGroupBox {font-size: 18px;font-weight: bold; }")
        group_box_2.setFixedHeight(400)


        self.layout = QVBoxLayout()
        self.layout.addWidget(group_box_1)
        self.layout.addWidget(group_box_2)
        self.setLayout(self.layout)
        self.setFixedSize(400 ,800)


class LinearSignalPlot(QWidget):
    """
    Signal Plot window
    """
    def __init__(self):
        super().__init__()

        group_box = QGroupBox("Velocity")
        layout = QVBoxLayout()


        # Create the plot
        # Get data from file
        y = Signal().medianfilter()
        x = np.arange(len(y))
        z = np.zeros(len(y))
        fig, ax = plt.subplots()
        ax.plot(x, y, linestyle='--')
        ax.plot(x, z, linestyle='dashed')

        # Design plot
        font1 = {'family':'serif','color':'darkred','size':16}
        font2 = {'family':'serif','color':'darkred','size':12}
        ax.set_title("ĐỒ THỊ VẬN TỐC", fontdict=font1)
        ax.set_ylabel('Vận tốc', fontdict=font2)
        ax.set_xlabel('Thời gian', fontdict=font2)
        ax.grid(True)

        # Create the canvas to display the plot
        canvas = FigureCanvas(fig)

        # Create the layout and add the canvas
        layout.addWidget(canvas)
        group_box.setLayout(layout)
        group_box.setStyleSheet("QGroupBox {font-size: 18px;font-weight: bold; }")


        self.layout = QVBoxLayout()
        self.layout.addWidget(group_box)
        self.setLayout(self.layout)
        self.setFixedSize(1000 ,800)
        


class MainWindow(QMainWindow):
    """
    Main window
    """
    def __init__(self):
        super().__init__()

        # Set the main window properties
        self.setWindowTitle('VTA')
        self.setGeometry(100, 100, 1400, 800)

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
