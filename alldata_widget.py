
from PyQt5.QtWidgets import QWidget, QVBoxLayout,QTableWidget, QTableWidgetItem, QLineEdit
from PyQt5.QtCore import Qt

from read_database import Database
from PyQt5.QtWidgets import QApplication

class AllDataWidget(QWidget):
    def __init__(self, parent = None, flags = Qt.WindowFlags()):
        super().__init__(parent, flags)

        
        self.central_layout_vbox = QVBoxLayout(self)

        self.searchbar = QLineEdit(self)
        self.central_layout_vbox.addWidget(self.searchbar)

        self.table = QTableWidget(self)
        self.table.setColumnCount(6)
        self.central_layout_vbox.addWidget(self.table)
        # self.table.setRowCount(1)

        self.db = Database()

        self.update_table()


    def update_table(self):
        self.table.setRowCount(len(self.db.brides()))
        for row, bride in enumerate(self.db.brides()):
            self.table.setItem(row, 0, QTableWidgetItem(str(bride.id)))
            self.table.setItem(row, 1, QTableWidgetItem(bride.dob))
            self.table.setItem(row, 2, QTableWidgetItem(bride.star))
            self.table.setItem(row, 3, QTableWidgetItem(bride.padam))
            self.table.setItem(row, 4, QTableWidgetItem(bride.time))
            self.table.setItem(row, 5, QTableWidgetItem(bride.sign))
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AllDataWidget()
    window.show()
    app.exec_()

