import logging
from smbus2 import i2c_msg

class pyi2c():
    def __init__(self, bus):
        self.bus = bus
        self._logger = logging.getLogger(__name__)

    def writeQuick(self, address, cmd):
        '''Quick command: no data
        
        :param address: Address of the i2c slave device
        :param cmd: 8-bit command
        '''
        command = [cmd]
        write = i2c_msg.write(address, command)
        self.bus.i2c_rdwr(write)
        self._logger.debug('writeQuick: address= %d, cmd = %s', address, cmd)         

    def write7Bit(self, address, cmd, target):
        '''7-bit write command: writes a 7-bit data value
        
        :param address: Address of the i2c slave device
        :param cmd: 8-bit command
        :param target: 7-bit data value
        '''
        command = [cmd, target >> 0 & 0xFF]
        write = i2c_msg.write(address, command)
        self.bus.i2c_rdwr(write)
        self._logger.debug('write7Bit: address= %d, cmd = %s, target = %d', address, cmd, target)                

    def write32Bit(self, address, cmd, target):
        '''32-bit write command: writes a 32-bit data value

        :param address: Address of the i2c slave device
        :param cmd: 8-bit command
        :param target: 32-bit data value
        '''        
        command = [cmd,
            target >> 0 & 0xFF,
            target >> 8 & 0xFF,
            target >> 16 & 0xFF,
            target >> 24 & 0xFF]
        write = i2c_msg.write(address, command)
        self.bus.i2c_rdwr(write)
        self._logger.debug('write32Bit: address= %d, cmd = %s, target = %d', address, cmd, target)          

    def readBlock(self, address, offset, length):
        '''Block read command: reads a block of data;
        The block starts from the specified offset and can have a variable length.

        :param address: Address of the i2c slave device
        :param offset: The block offset
        :param length: The block length
        :return: A list of data
        '''

        write = i2c_msg.write(address, offset)
        read = i2c_msg.read(address, length)
        self.bus.i2c_rdwr(write, read)
        self._logger.debug('readBlock: address= %d, offset = %d, length = %d', address, offset, length) 

        return list(read)        