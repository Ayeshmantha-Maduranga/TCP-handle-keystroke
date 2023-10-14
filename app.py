import sys
import socket
import threading
import time

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from ui_app import Ui_MainWindow


# ============================== VAR ==================================
sock = None
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
runListeningTread = True

# ----------------- start TCP connection Function --------------------
def init_server():
    global sock
    try:
        if sock is None:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('127.0.0.1', 65432))
            sock.listen()
            return True
        else :
            return False

    except Exception as e:
        # print("Serial port open error" + str(e))
        # ui.SerialCOM_labale.setText("transmitter not found")
        # ui.SerialCOM_labale.setStyleSheet(u"color:red")
        serOpen = False
        return False

# ----------------- stop TCP connection function ----------------------
def set_thread_close():
    global runListeningTread
    runListeningTread = False

def close():
    if(sock):
        sock.close()
    time.sleep(0.2)


# ------------------------ Tread Listening ----------------------------
def Listening(): 
    # try:
    global runListeningTread  
    conn = None 
    addr = None

    if not init_server():
        # print("Serial open not working")
        time.sleep(10)
    else:
        conn, addr = sock.accept()    

    with conn:
        while runListeningTread:
            data = conn.recv(1024)
            print(data)
            if not data:
                print("TCP data pack is empty") 
                break
                
    # except Exception as e:
    print("serial Listening error" + str(e)) 
    close()
    IntTCP_Listening()           


# ------------------- Int Tread Listening ---------------------------
listen_Tread = threading.Thread(target=Listening)

def IntTCP_Listening():
    global listen_Tread
    try:
        listen_Tread.start()
    except RuntimeError:  # occurs if thread is dead
        # create new instance if thread is dead
        listen_Tread = threading.Thread(target=Listening)
        listen_Tread.start()  # start thread

#  ============================ MAIN ===============================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()   
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # <--------- run app funtons ------------
    IntTCP_Listening()

    # <---- waiting for exit
    app.exec_()