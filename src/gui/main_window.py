import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QWidget
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PixCodeOS')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('src/gui/resources/jujutsu_kaisen_icon.png'))
        
        # Load and apply the theme
        with open('src/gui/resources/jujutsu_kaisen_theme.qss', 'r') as file:
            self.setStyleSheet(file.read())
        
        # Create layout and central widget
        main_layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        # Add a label
        self.label = QLabel("Welcome to PixCodeOS", self)
        main_layout.addWidget(self.label)
        
        # Add a button
        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(self.on_click)
        main_layout.addWidget(self.button)
        
        # Add an input field
        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Type something here...")
        main_layout.addWidget(self.input)
        
        # Add a horizontal layout for additional buttons
        h_layout = QHBoxLayout()
        self.button1 = QPushButton("Button 1", self)
        self.button2 = QPushButton("Button 2", self)
        h_layout.addWidget(self.button1)
        h_layout.addWidget(self.button2)
        main_layout.addLayout(h_layout)

    def on_click(self):
        self.label.setText("Button Clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())