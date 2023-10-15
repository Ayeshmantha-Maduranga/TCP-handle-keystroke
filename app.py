import sys
import socket
import threading
from multiprocessing import Process, freeze_support
import time
import json  

from PySide2 import QtWidgets, QtGui
import PySide2.QtGui
from PySide2.QtWidgets import QLabel, QWidget
from PySide2.QtCore import Qt
from ui_app import Ui_MainWindow


# ============================== VAR ==================================
data = {}
receivedData = "data"
keyStrokes = "a"

server = None
client_socket = None
runListeningThread = True

event = threading.Event()

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# ------------------------ TCP connection Function -----------------------

# <------------- handle incoming connections ------------>
def handle_client(client_socket, address):
    global runListeningThread
    try:
        while runListeningThread:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received data from {address[0]}:{address[1]}: {data.decode()}")

            # check for stop
            if event.is_set():
                break

    except Exception as e:
        print(f"Error in handle_client: {e}")
    finally:
        client_socket.close()

# <----------- Create a TCP server socket ------------->
def start_server():
    global server
    try:
        if server is None:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((HOST, PORT))
            server.listen()
            print(f"[*] Listening on {HOST}:{PORT}")

        while runListeningThread:
            client_socket, client_address = server.accept()
            print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
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
        print("terminate TCP server")


# ----------------------- ui funtions -------------------------------
def saveData():
    global data
    data['ipAddress'] = HOST
    data['port'] = PORT
    data['receivedData'] = receivedData
    data['keyStrokes'] = keyStrokes
    with open('data.json', 'w') as fp:
        json.dump(data, fp)

def TCP_Connect():
    ui.lineEdit_ip.setEnabled(False)
    ui.lineEdit_port.setEnabled(False)
    ui.pushButton_DisCon.setChecked(False)

    global listener_thread

    if not listener_thread.is_alive():
        listener_thread = Process(target=start_server)
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
        keyStrokes = event.key()
        key_name = QtGui.QKeySequence(keyStrokes).toString()
        print(f"Key pressed: {key_name}")
        ui.label_keyStroke.setText(key_name)
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

    # Remove the maximize button
    MainWindow.setWindowFlags(MainWindow.windowFlags() & ~Qt.WindowMaximizeButtonHint)
    # MainWindow.setFixedSize(310 , 200)
    ui.setupUi(MainWindow)
    MainWindow.show()

    # <----- load loacal JSON all Data file --------
    with open('data.json') as f:
        data = json.load(f)
        HOST = data['ipAddress']
        PORT = data['port']
        receivedData = data['receivedData']
        keyStrokes = data['keyStrokes']


    # <--------- load ui data ---------------
    ui.lineEdit_ip.setText(HOST)
    ui.lineEdit_port.setText(str(PORT))
    ui.lineEdit_Rdata.setText(receivedData)
    key_name = QtGui.QKeySequence(keyStrokes).toString()
    ui.label_keyStroke.setText(key_name)

    # <--------- run app funtons ------------
    ui.pushButton_connect.clicked.connect(TCP_Connect) 
    ui.pushButton_DisCon.clicked.connect(TCP_Disconnect)
    ui.lineEdit_ip.textChanged.connect(setIp)
    ui.lineEdit_port.textChanged.connect(setPort)
    ui.lineEdit_Rdata.textChanged.connect(setResData)
    ui.pushButton_keySet.clicked.connect(setKeyStoke)


    freeze_support()
    listener_thread = Process(target=start_server)
    # listener_thread.daemon = True

    

    # <---- waiting for exit
    app.exec_()