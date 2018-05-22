from DCTizer import DCTizer
from PyQt5.QtWidgets import QApplication
from tqdm import tqdm


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = DCTizer()
    sys.exit(app.exec_())
