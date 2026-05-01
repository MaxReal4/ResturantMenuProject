from PyQt6.QtWidgets import *
from menu import *
from logic import *

import sys
def main():
    application = QApplication(sys.argv)
    window = Logic()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()