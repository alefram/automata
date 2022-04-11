import sys
import glob
import serial

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


print(serial_ports())