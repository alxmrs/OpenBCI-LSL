'''
Created April 25, 2015

@author: Alex Rosengarten
'''

# from pylink import *
import argparse # new in Python2.7
from pylsl import StreamInfo, StreamOutlet, local_clock
import open_bci_v3 as bci
import time


def sendData(sample):
        # get 8 channel sample from OpenBCI Board; this is converted into a pylsl.vectorf (the data type that is expected by push_sample)
        mysample = sample.channel_data
        # get a time stamp in seconds from OpenBCI hardware
        stamp = sample.getTime()
        # now send it, will wait for board to send next packet.
        outlet.push_sample(mysample,stamp)

        print((mysample,stamp)) # debug

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="OpenBCI 'user'")
    parser.add_argument('-p', '--port', required=True,
                help="Port to connect to OpenBCI Dongle " +
                "( ex /dev/ttyUSB0 or /dev/tty.usbserial-* )")
    parser.add_argument('-b', '--baud', default=115200, type=int,
                help="Baud rate (not currently used)")
    args = parser.parse_args()


    outlet = None
    try:
        # first create a new stream info (here we set the name to OpenBCI, the content-type to EEG, 8 channels, 250 Hz, and float-valued data)
        # The last value would be the serial number of the device or some other more or less locally unique identifier for the stream as far as available (you could also omit it but interrupted connections wouldn't auto-recover).
        info = StreamInfo('OpenBCI_32','EEG',8,250,'float32','usbserial-DN0093AG');

        # append some meta-data
        info.desc().append_child_value("manufacturer","OpenBCI")
        channels = info.desc().append_child("channels")
        for c in ["C3","C4","Cz","FPz","POz","CPz","O1","O2"]:
            channels.append_child("channel").append_child_value("name",c).append_child_value("unit","microvolts").append_child_value("type","EEG")

        # next make an outlet; we set the transmission chunk size to 32 samples and the outgoing buffer size to 360 seconds (max.)
        outlet = StreamOutlet(info,32,360)
        print "Established LSL outlet."
    except:
        print "Count not create LSL outlet."


    print "User serial interface enabled..."
    print "Connecting to ", args.port

    board = bci.OpenBCIBoard(port=args.port, baud=args.baud)

    try:
        print("Beginning data transmission.")
        board.startStreaming(sendData)
    except:
        print("A problem occured when transmitting data.")

