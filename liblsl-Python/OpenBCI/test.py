import open_bci_v3 as bci
import os
import time

def printData(sample):
    #os.system('clear')
    print("----------------")
    print("%f" %(sample.id))
    print(sample.channel_data)
    # arr = sample.aux_data
    # hw_time = shortArrToLong(arr)

    # print(arr[0] & 0xFFFF, arr[1] & 0xFFFF, arr[2] & 0xFFFF)
    # print(toLittleEndian(arr[0] & 0xFFFF),
    #     toLittleEndian(arr[1] & 0xFFFF),
    #     toLittleEndian(arr[2] & 0xFFFF))

    # print("Hardware Time milliseconds: %d" %(hw_time))
    # print("Hardware Time seconds: %f" %(hw_time * 0.001))

    (t1, t2) = (sample.getTime(), sample.systime)
    #t2 = sample.timestamp
#    print("Time from this program: ", t1)
    print("System time", t2)
    print("Hardware time", t1)
#    print("Diff: ", t1-t2)
    print("----------------")


def shortArrToLong(arr):
    return (long)((toLittleEndian(arr[0] & 0xFFFF) << 16) + toLittleEndian(arr[1] & 0xFFFF))

def toLittleEndian(n):
    return n >> 8 | ((n & 0x00FF) << 8)

def hex2(n):
    return hex(n &  0xffffffff)[:-1]

if __name__ == '__main__':
  port = '/dev/tty.usbserial-DN0093AG'
  baud = 115200
  board = bci.OpenBCIBoard(port=port, baud=baud)
  board.startStreaming(printData)
