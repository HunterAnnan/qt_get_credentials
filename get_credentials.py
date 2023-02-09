import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    # QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
            super().__init__()

            self.setWindowTitle("Credentials")
            self.resize(300,120)

            layout_Outer = QVBoxLayout()
            layout_Inner_line1 = QHBoxLayout()
            layout_Inner_line2 = QHBoxLayout()
            
            self.edit_Username = QLineEdit()
            
            self.edit_Password = QLineEdit()
            self.edit_Password.setEchoMode(QLineEdit.Password)
            self.edit_Password.returnPressed.connect(self.submit_clicked)
            
            self.button_Submit = QPushButton("Submit")
            self.button_Submit.clicked.connect(self.submit_clicked)
            
            layout_Inner_line1.addWidget(QLabel("Username:"))
            layout_Inner_line1.addWidget(self.edit_Username)
            
            layout_Inner_line2.addWidget(QLabel("Password:"))
            layout_Inner_line2.addWidget(self.edit_Password)
            
            layout_Outer.addLayout(layout_Inner_line1)
            layout_Outer.addLayout(layout_Inner_line2)
            layout_Outer.addWidget(self.button_Submit)
            

            widget = QWidget()
            widget.setLayout(layout_Outer)

            # Set the central widget of the Window. Widget will expand
            # to take up all the space in the window by default.
            self.setCentralWidget(widget)
            
    def submit_clicked(self):
        self.stored_username = self.edit_Username.text()
        self.stored_password = self.edit_Password.text()
        self.close()
        

def get_credentials():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec_()
    
    return window.stored_username, window.stored_password
            
if __name__ == '__main__':
    db_username, db_password = get_credentials()
    
    print(db_username + " " + db_password)