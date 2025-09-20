from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QTabWidget



class Mainwindow(QMainWindow):
    def __init__(self, parent = None, flags = Qt.WindowFlags()):
        super().__init__(parent, flags)

        self.centralWidget = QWidget(self)
        self.central_layout_vbox = QVBoxLayout(self.centralWidget)

        self.tabbedwidget = QTabWidget(self.centralWidget)
        self.tabbedwidget.setObjectName("tabbedwidget")

        self.central_layout_vbox.addWidget(self.tabbedwidget)



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.showMaximized()
    app.exec_()