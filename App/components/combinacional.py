import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSvg import *
from tablaTransicion import tablaTransicion
from entradas import entradas
import serial
import glob

def serial_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            on unsupported or unknown
        :returns:
            A list of the serial ports available on the system
    """

    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
        pass
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
        pass
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
        pass
    else:
        raise EnvironmentError('Unsupported platform')
        pass

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)     
        except (OSError,serial.SerialException):
            pass
        pass
    return result

puerto = serial_ports()

pinguino = serial.Serial(puerto[0], timeout=0.1, baudrate=9600)
pinguino.write(b"PinMode(7,OUTPUT)")
pinguino.write(b"PinMode(6,OUTPUT)")
pinguino.write(b"PinMode(5,OUTPUT)")
pinguino.write(b"PinMode(4,OUTPUT)")



    
class combinacional(QWidget):
    def __init__(self):
        super(combinacional, self).__init__()
        layoutI = QGridLayout()
        self.setLayout(layoutI)

        #widgets
        combTransicion = QPushButton('tabla de transición')
        entrada = QPushButton('entradas')
        start = QPushButton('start')
        output = QPushButton('Output')
        display = QLCDNumber()


        def _tablaTransicion():
            sw = tablaTransicion()
            sw.setWindowTitle("tabla de transicion")
            sw.exec_()
            pass

        def _output():

            s = entradas()
            sw = tablaTransicion()
            cont = 0
            for i in range(0, 4):
                if s.dato_entrada == sw.data_in[i]:
                    break
                    pass
                else:
                    cont = cont + 1
                    pass
                pass
            pass

            for k in range(0, 4):
                if sw.data_out[cont][k] == "x" or sw.data_out == "0":
                    sw.data_out[cont][k] = "0"
                    pass
                pass
            
            info = sw.data_out[cont]
            str1 = ''.join(info)
            display.display(str1)

            for j in range(0, 4):
                if j == 0:
                    if sw.data_out[cont][j] == "1":
                        pinguino.write(b"digitalWrite(4,HIGH)")
                        pass
                    else:
                        pinguino.write(b"digitalWrite(4,LOW)")
                        pass
                if j == 1:
                    if sw.data_out[cont][j] == "1":
                        pinguino.write(b"digitalWrite(5,HIGH)")
                        pass
                    else:
                        pinguino.write(b"digitalWrite(5,LOW)")
                        pass
                    pass
                if j == 2:
                    if sw.data_out[cont][j] == "1":
                        pinguino.write(b"digitalWrite(6,HIGH)")
                        pass
                    else:
                        pinguino.write(b"digitalWrite(6,LOW)")
                        pass
                    pass
                if j == 3:
                    if sw.data_out[cont][j] == "1":
                        pinguino.write(b"digitalWrite(7,HIGH)")
                        pass
                    else:
                        pinguino.write(b"digitalWrite(7,LOW)")
                        pass


        def _start():
            sw = tablaTransicion()
            for i in range(0, 4):
                info = sw.data_out[i]
                str1 = ''.join(info)
                for z in range(0,40000000):
                    pass
                display.display(str1)
                for j in range(0, 4):
                    if j == 0:
                        if sw.data_out[i][j] == "1":
                            pinguino.write(b"digitalWrite(4,HIGH)")
                            pass
                        else:
                            pinguino.write(b"digitalWrite(4,LOW)")
                            pass
                    if j == 1:
                        if sw.data_out[i][j] == "1":
                            pinguino.write(b"digitalWrite(5,HIGH)")
                            pass
                        else:
                            pinguino.write(b"digitalWrite(5,LOW)")
                            pass
                        pass
                    if j == 2:
                        if sw.data_out[i][j] == "1":
                            pinguino.write(b"digitalWrite(6,HIGH)")
                            pass
                        else:
                            pinguino.write(b"digitalWrite(6,LOW)")
                            pass
                        pass
                    if j == 3:
                        if sw.data_out[i][j] == "1":
                            pinguino.write(b"digitalWrite(7,HIGH)")
                            pass
                        else:
                            pinguino.write(b"digitalWrite(7,LOW)")
                            pass
                    pass
                
                    
                pass
            pass

        def _entrada():
            en = entradas()
            en.setWindowTitle('entradas')
            en.exec_()
            pass


        #signals 
        combTransicion.clicked.connect(_tablaTransicion)
        entrada.clicked.connect(_entrada)
        start.clicked.connect(_start)
        output.clicked.connect(_output)


        
        # svg
        svg = QSvgWidget()
        svg.renderer().load("automata\components\svgs\combinacional.svg")
        svg.show()




        # layouts

        layoutI.addWidget(svg, 0,1)
        layoutI.addWidget(entrada,0, 0)
        layoutI.addWidget(combTransicion, 4, 1)
        layoutI.addWidget(start, 5, 6)
        layoutI.addWidget(output, 5, 8)
        layoutI.addWidget(display,0,2)
        

        
        
