import sys
import os
import socket
import threading
from multiprocessing import Process, freeze_support
from io import TextIOBase
import json  
import pyautogui

from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QLabel, QWidget
from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QIcon
from ui_app import Ui_MainWindow


# ============================== VAR ==================================
data = {}
receivedData = "data"
keyStrokes = "space"

server = None
client_socket = None
runListeningThread = True

event = threading.Event()

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
#<--------- Define the location where you want to check for data.json
file_location = os.path.expandvars('%APPDATA%\\TCP_Hkey\\')
json_file_path = os.path.join(file_location, "data.json")
# ------------------------ TCP connection Function -----------------------

# <------------- handle incoming connections ------------>
def handle_client(client_socket, address, _keyStrokes, _receivedData):
    global runListeningThread
    try:
        while runListeningThread:
            data = client_socket.recv(1024)
            if not data:
                break

            # <------ run keyboard control
            if(data.decode() == _receivedData):
                print(f"key name : {_keyStrokes}")
                pyautogui.press(_keyStrokes)
                print('keyboard press key success')

            #<----- print all incoming msg
            print(f"Received data from {address[0]}:{address[1]}: {data.decode()}")

            # check for stop
            if event.is_set():
                break

    except Exception as e:
        print(f"Error in handle_client: {e}")
    finally:
        client_socket.close()

# <----------- Create a TCP server socket ------------->
def start_server(_HOST, _PORT, _keyStrokes, _receivedData):
    global server
    try:
        if server is None:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((_HOST, _PORT))
            server.listen()
            print(f"[*] Listening on {_HOST}:{_PORT}")

        while runListeningThread:
            client_socket, client_address = server.accept()
            print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, _keyStrokes, _receivedData))
            client_thread.start()

            # check for stop
            if event.is_set():
                break

    except Exception as e:
        print("TCP Listening error" + str(e))
    finally:
        if server:
            server.close()


# ----------------- stop TCP connection function ----------------------
# Define a function to stop the server and clean up resources
def stop_server():
    global runListeningThread
    runListeningThread = False

    event.set()
    # listener_thread.join()

    if client_socket is not None:
        client_socket.close()
    
    if server is not None:
        server.close()

    if listener_thread.is_alive():
        listener_thread.terminate()
        print("TCP server disconnected!")


# ----------------------- ui funtions -------------------------------
def saveData():
    global data
    data['ipAddress'] = HOST
    data['port'] = PORT
    data['receivedData'] = receivedData
    data['keyStrokes'] = keyStrokes
    with open(json_file_path, 'w') as fp:
        json.dump(data, fp)
        print('-save data-')

def TCP_Connect():
    ui.lineEdit_ip.setEnabled(False)
    ui.lineEdit_port.setEnabled(False)
    ui.pushButton_DisCon.setChecked(False)

    global listener_thread

    if not listener_thread.is_alive():
        listener_thread = Process(target=start_server, args=(HOST, PORT, keyStrokes, receivedData))
        print("TCP server connection sucsses!")
        listener_thread.start()
    else:
        listener_thread.terminate()
        print("listener thread is still runnig")

def TCP_Disconnect():
    stop_server()
    ui.lineEdit_ip.setEnabled(True)
    ui.lineEdit_port.setEnabled(True)
    ui.pushButton_connect.setChecked(False)

def setIp():
    global HOST
    HOST = ui.lineEdit_ip.text()
    saveData()

def setPort():
    global PORT
    try:
        PORT = int(ui.lineEdit_port.text())
    except ValueError:
        print("Invalid port number. Please enter a valid integer.")
    saveData()

def setResData():
    global receivedData
    receivedData = ui.lineEdit_Rdata.text()
    saveData()

# <------- end ui funtions 


# ================= STATUS BAR UPDATE CLASS =======================
class StatusBarStream(TextIOBase):
    def __init__(self, status_bar):
        super(StatusBarStream, self).__init__()
        self.status_bar = status_bar
        self.current_message = ""
        self.message_timer = QTimer()
        self.message_timer.timeout.connect(self.clear_message)

    def write(self, text):
        self.current_message += str(text)
        self.status_bar.showMessage(self.current_message)
        self.message_timer.start(1000)  # Display the message for 3 seconds

    def clear_message(self):
        self.current_message = ""
        self.message_timer.stop()

    def flush(self):
        pass

# ================== CUSTOM UI CLASS ==============================
class ui_keySet(QtWidgets.QDialog):
    
    def __init__(self, parent=None):
        super(ui_keySet, self).__init__(parent)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowTitle('set keystoke')
        self.resize(200, 100)
        self.setModal(True)

        # Create a QLabel and set its text and alignment
        label = QtWidgets.QLabel("Press any key", self)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, 0, self.width(), self.height()) 
    
    def keyPressEvent(self, event):
        global keyStrokes
        keyStrokes = QtGui.QKeySequence(event.key()).toString().lower()
        print(f"Key pressed: {keyStrokes}")
        ui.label_keyStroke.setText(keyStrokes)
        saveData()
        self.close()

def setKeyStoke():
    keySetWin.show()


# ============================= MAIN ===============================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()   
    ui = Ui_MainWindow()
    keySetWin = ui_keySet(MainWindow)

    # <--- Remove the maximize button
    MainWindow.setWindowFlags(MainWindow.windowFlags() & ~Qt.WindowMaximizeButtonHint)
    # Create a QIcon object with the path to your icon file
    icon = QIcon("TCP_Hkey.ico")
    # Set the window icon
    MainWindow.setWindowIcon(icon)
    # MainWindow.setFixedSize(310 , 200)
    ui.setupUi(MainWindow)
    MainWindow.show()

    # <--------- status bar sys out setting ------------
    # Redirect sys.stdout to the custom StatusBarStream
    status_bar_stream = StatusBarStream(ui.statusBar)
    sys.stdout = status_bar_stream #<--- change to direction

    # <----------- init listener thread ------
    freeze_support()
    listener_thread = Process(target=start_server, args=(HOST, PORT, keyStrokes, receivedData))

    # <--------- load configtion data file --------------
    # <----- Check if data.json exists at the specified location
    if os.path.exists(json_file_path):
        print("fount config file.")
    else:
        print("data.json file does not exist. Creating the file...")
        # <----- Create the directory if it doesn't exist
        if not os.path.exists(file_location):
            os.makedirs(file_location)

        # <----- Define the parameters you want to store in the JSON file
        _data = {"ipAddress": "127.0.0.1", "port": 65434, "receivedData": "data", "keyStrokes": "a"}

        # <----- Write the data to data.json
        with open(json_file_path , "w") as json_file:
            json.dump(_data, json_file, indent=4)
    
    print("| load data")

     # <----- load loacal JSON all Data file --------
    with open(json_file_path) as f:
        data = json.load(f)
        HOST = data['ipAddress']
        PORT = data['port']
        receivedData = data['receivedData']
        keyStrokes = data['keyStrokes']


    # <--------- load ui data ---------------
    ui.lineEdit_ip.setText(HOST)
    ui.lineEdit_port.setText(str(PORT))
    ui.lineEdit_Rdata.setText(receivedData)
    ui.label_keyStroke.setText(keyStrokes)

    # <--------- run app funtons ------------
    ui.pushButton_connect.clicked.connect(TCP_Connect) 
    ui.pushButton_DisCon.clicked.connect(TCP_Disconnect)
    ui.lineEdit_ip.textChanged.connect(setIp)
    ui.lineEdit_port.textChanged.connect(setPort)
    ui.lineEdit_Rdata.textChanged.connect(setResData)
    ui.pushButton_keySet.clicked.connect(setKeyStoke)
    ui.statusBar.showMessage("Ready")  # Initial status message

    # <---- waiting for exit
    app.exec_()