
from PyQt5.QtWidgets import QWidget, QVBoxLayout,QTableWidget, QTableWidgetItem, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QApplication


import sqlite3
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel

class AllDataWidget(QWidget):
    def __init__(self, parent = None, flags = Qt.WindowFlags()):
        super().__init__(parent, flags)

        
        self.central_layout_vbox = QGridLayout(self)

        self.searchbar = QLineEdit(self)
        self.central_layout_vbox.addWidget(self.searchbar,0,0)

        self.filters_button = QPushButton("Filters", self)
        self.central_layout_vbox.addWidget(self.filters_button, 0, 1)

        self.table = QTableWidget(self)
        self.table.clicked.connect(self.on_cell_clicked)
        self.central_layout_vbox.addWidget(self.table, 2,0)

        self.image_label = QLabel(self)
        self.image_label.setScaledContents(True)
        self.image_label.setFixedSize(1000, 900)
        self.central_layout_vbox.addWidget(self.image_label, 2, 1)

    
        self.update_table()

    
    def on_cell_clicked(self, index):
        row = index.row()
        col = index.column()

        item = self.table.item(row, 0)
        if item:
            print(item.text()) 
            pixmap = QPixmap(f"renamed/{item.text()}.jpg")  # 🖼️ replace with your image path
            self.image_label.setPixmap(pixmap)

             


    def update_table(self):
        conn = sqlite3.connect('matrimony.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM brides WHERE dob >= ?",('1998-08-09',))    

        columns = [column[0] for column in cursor.description]
        self.table.setColumnCount(len(columns))
        self.table.setHorizontalHeaderLabels(columns)


        rows = cursor.fetchall()
        self.table.setRowCount(len(rows))

        for row, data in enumerate(rows):
            for col, value in enumerate(data):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))  

        conn.close()

    

    


    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AllDataWidget()
    window.showMaximized()
    app.exec_()

