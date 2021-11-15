import sys
from PyQt5.QtWidgets import QApplication
from Class import StartMenuWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = StartMenuWindow()
    w.show()  # открытие+- 1 окна
    sys.exit(app.exec_())
