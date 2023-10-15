import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QStatusBar
from io import StringIO

class StatusBarStream(StringIO):
    def __init__(self, status_bar):
        super(StatusBarStream, self).__init__()
        self.status_bar = status_bar

    def write(self, text):
        self.status_bar.showMessage(text)

    def flush(self):
        pass

app = QApplication(sys.argv)
window = QMainWindow()

# Create a status bar and set it to the main window
status_bar = QStatusBar()
window.setStatusBar(status_bar)

# Redirect sys.stdout to the custom StatusBarStream
status_bar_stream = StatusBarStream(status_bar)
sys.stdout = status_bar_stream

print("Hello, this will be displayed in the status bar!")

window.show()
sys.exit(app.exec_())