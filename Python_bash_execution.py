import os
import subprocess

# for raspberry

def usb_name():
    rpistr = "ls /media/pi/"   #command in bash
    proc = subprocess.Popen(rpistr, shell=True, preexec_fn=os.setsid, stdout=subprocess.PIPE)

    # Odczytaj wszystkie linie z wyj�cia procesu
    # for line in proc.stdout:
    #     print(line.decode().strip())  # Dekoduj bajty na ci�g znak�w i usu� znak nowej linii
    line = proc.stdout.readline()
    dysk_name = str(line.decode().strip())
    return dysk_name


print(usb_name())
