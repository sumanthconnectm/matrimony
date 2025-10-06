from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QTabWidget

from alldata_widget import AllDataWidget


from themes.dark import dark_theme
from themes.light import light_theme





class Mainwindow(QMainWindow):
    def __init__(self, parent = None, flags = Qt.WindowFlags()):
        super().__init__(parent, flags)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.central_layout_vbox = QVBoxLayout(self.centralWidget)

        self.tabbedwidget = QTabWidget(self.centralWidget)
        self.tabbedwidget.setObjectName("tabbedwidget")

        self.central_layout_vbox.addWidget(self.tabbedwidget)

        self.alldatawidget = AllDataWidget(self.centralWidget)

        self.tabbedwidget.addTab(self.alldatawidget, "ALL BRIDES")

        qApp.setStyleSheet(dark_theme)
        qApp.setStyleSheet("")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.showMaximized()
    app.exec_()
