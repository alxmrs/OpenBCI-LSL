import open_bci_v3 as bci
import os
import time

def printData(sample):
    #os.system('clear')
    print("----------------")
    print("%f" %(sample.id))
    print(sample.channel_data)

    (t1, t2) = (sample.getTime(), sample.systime)

    print("System time", t2)
    print("Hardware time", t1)
#    print("Diff: ", t1-t2)
    print("----------------")

if __name__ == '__main__':
  port = '/dev/tty.usbserial-DN0093AG'
  baud = 115200
  board = bci.OpenBCIBoard(port=port, baud=baud)
  board.startStreaming(printData)
