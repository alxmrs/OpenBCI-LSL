# OpenBCI-LSL
SCCN's Lab Streaming Layer + Drivers to work with OpenBCI

## How to use
1. Make sure OpenBCI firmware is installed:
http://docs.openbci.com/tutorials/02-Upload_Code_to_OpenBCI_Board
2. Run the OBCI.py file:

> python OBCI.py -p 'port-goes-here'

To look up which port to use [on OSX], type:
> ls /dev/tty.*

Check out all the apps that work with LSL here: ftp://sccn.ucsd.edu/pub/software/LSL/Apps/

## Do I have to upgrade the firmware?
The default OpenBCI firmware, as of writing, doesn't send the timestamp of when the EEG sample data was recorded. All timestamps for the channel data are calculated at the time they are received by the computer. This is problematic because accurate timestamps are crucially important for EEG signal processing. This update sends a milliseconds count over the auxiliary data array instead of accelerometer data.


