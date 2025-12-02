import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Моё первое приложение")

        button = QPushButton("Нажми меня!", self)
        button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Кнопка нажата!")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
