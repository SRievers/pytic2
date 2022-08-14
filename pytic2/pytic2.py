import logging

from .pyi2c import pyi2c

TIC_SETTARGETPOSITION_CMD = 0xE0
TIC_SETTARGETVELOCITY_CMD = 0xE3
TIC_HALTANDSETPOSITION_CMD = 0xEC
TIC_HALTANDHOLD_CMD = 0x89
TIC_GOHOME_CMD = 0x97
TIC_RESETCOMMANDTIMEOUT_CMD = 0x8C
TIC_DEENERGIZE_CMD = 0x86
TIC_ENERGIZE_CMD = 0x85
TIC_EXITSAFESTART_CMD = 0x83
TIC_RESET_CMD = 0xB0
TIC_CLEARDRIVEERROR_CMD = 0x8A
TIC_SETMAXSPEED_CMD = 0xE6
TIC_SETSTARTTINGSPEED_CMD = 0xE5
TIC_SETMAXACCEL_CMD = 0xEA
TIC_SETMAXDECEL_CMD = 0xE9
TIC_SETSTEPMODE_CMD = 0x94
TIC_SETCURRENTLIMIT_CMD =  0x91
TIC_SETDECAYMODE_CMD = 0x92
TIC_GETVARIABLE_CMD = 0xA1
TIC_GETERROROCCURRED_CMD = 0xA2

TIC_OPERATIONSTATE_VAR = 0x00
TIC_MISCFLAG1_VAR = 0x01
TIC_ERRORSTATUS_VAR = 0x02
TIC_ERRORSOCCURRED_VAR = 0x04
TIC_PLANNINGMODE_VAR = 0x09
TIC_TARGETPOSTION_VAR = 0x0A
TIC_TARGETVELOCITY_VAR = 0x0E
TIC_STARTINGSPEED_VAR = 0x12
TIC_MAXSPEED_VAR = 0x16
TIC_MAXDECEL_VAR = 0x1A
TIC_MAXACCEL_VAR = 0x1E
TIC_CURRENTPOSITION_VAR = 0x22
TIC_CURRENTVELOCITY_VAR = 0x26
TIC_ACTINGTARGETPOSITION_VAR = 0x2A
TIC_TIMESINCELASTSTEP_VAR = 0x2E
TIC_DEVICERESET_VAR = 0x32
TIC_VINVOLTAGE_VAR = 0x33
TIC_UPTIME_VAR = 0x35
TIC_ENCODERPOSITION_VAR = 0x39
TIC_RCPULSEWIDTH_VAR = 0x3D
TIC_ANAREADSCL_VAR = 0x3F
TIC_ANAREADSDA_VAR = 0x41
TIC_ANAREADTX_VAR = 0x43
TIC_ANAREADRX_VAR = 0x45
TIC_DIGREAD_VAR = 0x47
TIC_PINSTATES_VAR = 0x48
TIC_STEPMODE_VAR = 0x49
TIC_CURRENTLIMIT_VAR = 0x4A
TIC_DECLAYMODE_VAR = 0x4B
TIC_INPUTSTATE_VAR = 0x4C
TIC_INPUTAVAR_VAR = 0x4D
TIC_INPUTHYST_VAR = 0x4F
TIC_INPUTSCALE_VAR = 0x51

class pytic2():
    def __init__(self, bus, address):
        self._interface = pyi2c(bus)
        self.address = address 
        self._logger = self._initialize_logger()     

    def _initialize_logger(self):
        # - Logging - 
        self._log_level = logging.DEBUG
        _logger = logging.getLogger('PyTic2({})'.format(self.address))
        _logger.setLevel(self._log_level)
        # _formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # # Console Logging
        # _ch = logging.StreamHandler()
        # _ch.setLevel(self._log_level)
        # _ch.setFormatter(_formatter)
        # _logger.addHandler(_ch)
        return _logger        

    def setTargetPosition(self, target):
        '''Sets the target position in microsteps.

           target position, signed integer
           Range: −2,147,483,648 to +2,147,483,647 = −0x8000 0000 to +0x7FFF FFFF
           Units: microsteps'''

        self._interface.write32Bit(self.address, TIC_SETTARGETPOSITION_CMD, target)

    def setTargetVelocity(self, target):
        '''Sets the target velocity in microsteps per 10,000 seconds.
  
           target velocity, signed integer
           Range: −500,000,000 to +500,000,000
           Units: microsteps per 10,000 s'''

        self._interface.write32Bit(self.address,TIC_SETTARGETVELOCITY_CMD, target)

    def haltAndSetPosition(self, target):
        '''Stops the motor abruptly without respecting the deceleration limit and
           sets the “Current position” variable, which represents what position
           the Tic currently thinks the motor is in.
  
           current position, signed integer
           Range: −2,147,483,648 to +2,147,483,647 = −0x8000 0000 to +0x7FFF FFFF
           Units: microsteps'''

        self._interface.write32Bit(self.address,TIC_HALTANDSETPOSITION_CMD, target)

    def haltAndHold(self):
        '''Stops the motor abruptly without respecting the deceleration limit.'''

        self._interface.writeQuick(self.address,TIC_HALTANDHOLD_CMD)

    def goHome(self, direction):
        '''Starts the Tic’s homing procedure.
  
           0: Go home in the reverse direction
           1: Go home in the forward direction'''

        self._interface.write7Bit(self.address,TIC_GOHOME_CMD, direction)

    def resetCommandTimeout(self):
        '''If the command timeout is enabled, this command resets it and prevents 
           the “command timeout” error from happening for some time.'''

        self._interface.writeQuick(self.address,TIC_RESETCOMMANDTIMEOUT_CMD)

    def deenergize(self):
        '''Causes the Tic to de-energize the stepper motor coils by disabling its 
           stepper motor driver.'''

        self._interface.writeQuick(self.address,TIC_DEENERGIZE_CMD)

    def energize(self):
        '''Requests for the Tic to energize the stepper motor coils by enabling its 
           stepper motor driver.'''
        self._logger.debug('energize - {}'.format(self.address))
        self._interface.writeQuick(self.address,TIC_ENERGIZE_CMD)

    def exitSafeStart(self):
        '''Causes the “safe start violation” error to be cleared for 200 ms. If there 
           are no other errors, this allows the system to start up.'''

        self._interface.writeQuick(self.address,TIC_EXITSAFESTART_CMD)

    def reset(self):
        '''Makes the Tic forget most parts of its current state.'''

        self._interface.writeQuick(self.address,TIC_RESET_CMD)

    def clearDriveError(self):
        '''Attempts to clear a motor driver error.'''

        self._interface.writeQuick(self.address,TIC_CLEARDRIVEERROR_CMD)

    def setMaxSpeed(self, target):
        '''Temporarily sets the Tic’s maximum allowed motor speed in units of 
           steps per 10,000 seconds'''

        self._interface.write32Bit(self.address,TIC_SETMAXSPEED_CMD, target)

    def setStartingSpeed(self, target):
        '''Temporarily sets the Tic’s starting speed in units of steps per 10,000 seconds'''

        self._interface.write32Bit(self.address,TIC_SETSTARTTINGSPEED_CMD, target)

    def setMaxAccel(self, target):
        '''Temporarily sets the Tic’s maximum allowed motor acceleration in units of 
           steps per second per 100 seconds.'''

        self._interface.write32Bit(self.address,TIC_SETMAXACCEL_CMD, target)

    def setMaxDecel(self, target: int):
        '''Temporarily sets the Tic’s maximum allowed motor deceleration in units of
           steps per second per 100 seconds'''

        self._interface.write32Bit(self.address,TIC_SETMAXDECEL_CMD, target)

    def setStepMode(self, target):
        '''Temporarily sets the step mode (also known as microstepping mode) of 
           the driver on the Tic'''

        self._interface.write7Bit(self.address,TIC_SETSTEPMODE_CMD, target)

    def setCurrentLimit(self, target):
        '''Temporarily sets the stepper motor coil current limit of the driver on 
           the Tic in units of 32 milliamps.'''

        self._interface.write7Bit(self.address,TIC_SETCURRENTLIMIT_CMD, target)

    def setDecayMode(self, target):
        '''Temporarily sets the decay mode of the driver on the Tic.'''

        self._interface.write7Bit(self.address,TIC_SETDECAYMODE_CMD, target)

    def getVariable(self, offset, length):
        '''Gets one or more variables from the Tic.'''

        return self._interface.readBlock(self.address, [TIC_GETVARIABLE_CMD, offset ], length)
 
    def getErrorsOccurred(self, offset, length):
        '''Identical to the getVariable command, except that it also clears 
           the “Errors occurred” variable.'''

        return self._interface.readBlock(self.address, [TIC_GETERROROCCURRED_CMD, offset ], length)

    def _getVariable8(self, offset):
        b = self.getVariable(offset, 1)

        return b[0]

    def _getVariable16(self, offset):
        b = self.getVariable(offset, 2)

        return b[0] + (b[1] << 8)

    def _getVariable32(self, offset):
        b = self.getVariable(offset, 4)

        return b[0] + (b[1] << 8) + (b[2] << 16) + (b[3] << 24)

    def _getVariable32s(self, offset):
        b = self.getVariable(offset, 4)
        value = b[0] + (b[1] << 8) + (b[2] << 16) + (b[3] << 24)
        if value >= (1 << 31):
            value -= (1 << 32)

        return value  

    def getOperationState(self):
        '''The overall state of the Tic.
        
           0: Reset
           2: De-energized
           4: Soft error
           6: Waiting for ERR line
           8: Starting up
           10: Normal'''
        
        return self._getVariable8(TIC_OPERATIONSTATE_VAR)

    def getMiscFlags1(self):
        '''The set bits of this variable provide additional information about
           the Tic’s status.

           Bit 0: Energized – The Tic’s motor outputs are enabled and if 
                  a stepper motor is properly connected, its coils are 
                  energized (i.e. electrical current is flowing).
           Bit 1: Position uncertain – The Tic has not received external 
                  confirmation that the value of its “current position” 
                  variable is correct (see Section 5.4).
           Bit 2: Forward limit active – One of the forward limit switches
                  is active.
           Bit 3: Reverse limit active – One of the reverse limit switches
                  is active.
           Bit 4: Homing active – The Tic’s homing procedure is running.
           Bits 5–7: reserved'''
        
        return self._getVariable8(TIC_MISCFLAG1_VAR)

    def getErrorStatus(self):
        '''The set bits of this variable indicate the errors that are currently
           stopping the motor. The motor can only be controlled normally when
           this variable has a value of 0.

           Bit 0: Intentionally de-energized
           Bit 1: Motor driver error
           Bit 2: Low VIN
           Bit 3: Kill switch active
           Bit 4: Required input invalid
           Bit 5: Serial error
           Bit 6: Command timeout
           Bit 7: Safe start violation
           Bit 8: ERR line high
           Bits 9–15: reserved'''
        
        return self._getVariable16(TIC_MISCFLAG1_VAR)

    def getErrorOccurred(self):
        '''The set bits of this variable indicate the errors that have occurred
           since this variable was last cleared with the “get variable and
           clear errors occurred” command.

           Bits 0–15: These bits correspond to the same errors as those of 
                      the “error status” variable documented above.
           Bit 16: Serial framing
           Bit 17: Serial RX overrun
           Bit 18: Serial format
           Bit 19: Serial CRC
           Bit 20: Encoder skip
           Bits 21–31: reserved'''
        
        return self._getVariable32(TIC_ERRORSOCCURRED_VAR)

    def getPlanningMode(self) -> int:
        '''The kind of step planning algorithm the controller is currently using.

           0: Off (no target; not sending steps)
           1: Target position
           2: Target velocity'''
        
        return self._getVariable8(TIC_PLANNINGMODE_VAR)

    def getTargetPosition(self):
        '''Motor target position (−2,147,483,648 to +2,147,483,647 = −0x8000 0000
           to +0x7FFF FFFF). This value is only meaningful if the “planning mode” 
           variable indicates “target position”.
        
           units: microsteps'''
        
        return self._getVariable32s(TIC_TARGETPOSTION_VAR)

    def getTargetVelocity(self):
        '''Motor target velocity (−500,000,000 to +500,000,000). This value is
           only meaningful if the “planning mode” variable indicates
           “target velocity”.
        
           units: microsteps per 10,000 s'''
        
        return self._getVariable32s(TIC_TARGETVELOCITY_VAR)

    def getStartingSpeed(self):
        '''Maximum speed at which instant acceleration and deceleration are
           allowed (0 to 500,000,000).

           units: microsteps per 10,000 s'''

        return self._getVariable32(TIC_STARTINGSPEED_VAR)

    def getMaxSpeed(self):
        '''Maximum allowed motor speed (0 to 500,000,000).

           units: microsteps per 10,000 s'''

        return self._getVariable32(TIC_MAXSPEED_VAR)

    def getMaxDeceleration(self):
        '''Maximum allowed motor deceleration (100 to 2,147,483,647 = 0x64
           to 0x7FFF FFFF).

           units: microsteps per 10,000 s'''

        return self._getVariable32(TIC_MAXDECEL_VAR)

    def getMaxAcceleration(self):
        '''Maximum allowed motor acceleration  (100 to 2,147,483,647 = 0x64
           to 0x7FFF FFFF).

           units: microsteps per 10,000 s'''

        return self._getVariable32(TIC_MAXACCEL_VAR)

    def getCurrentPosition(self):
        '''Current position of the motor (−2,147,483,648 to +2,147,483,647 =
           −0x8000 0000 to +0x7FFF FFFF). Note that this just tracks steps that
           the Tic has commanded the stepper driver to take; it could be 
           different from the actual position of the motor for various reasons.
        
           units: microsteps'''
        
        return self._getVariable32s(TIC_CURRENTPOSITION_VAR)    

    def getCurrentVelocity(self):
        '''Current velocity of the motor (−500,000,000 to +500,000,000). 
           Note that this is just the step rate and direction the Tic is sending
           to the driver, and it might not correspond to the actual velocity of
           the motor for various reasons.

           units: microsteps'''
        
        return self._getVariable32s(TIC_CURRENTVELOCITY_VAR) 

    def getActingTargetPosition(self):
        '''This is a variable used in the Tic’s target position step planning 
           algorithm. It is accessible mainly for getting insight into 
           the algorithm or for troubleshooting.This value could be invalid
           while the motor is stopped.

           units: microsteps'''
        
        return self._getVariable32s(TIC_ACTINGTARGETPOSITION_VAR)  

    def getTimeSinceLastStep(self):
        '''This is a variable used in the Tic’s step planning algorithms.
           It is accessible mainly for getting insight into the algorithms or
           for troubleshooting. This value could be invalid while the motor is stopped.

           units: 1/3 us'''
        
        return self._getVariable32(TIC_TIMESINCELASTSTEP_VAR)  

    def getDeviceReset(self):
        '''The cause of the Tic’s last full microcontroller reset.

           0: Power up
           1: Brown-out reset
           2: Reset line (RST) pulled low by external source
           4: Watchdog timer reset (should never happen; this could indicate a firmware bug)
           8: Software reset (by firmware upgrade process)
           16: Stack overflow (should never happen; this could indicate a firmware bug)
           32: Stack underflow (should never happen; this could indicate a firmware bug)
           
           A “reset” command does not affect this variable.'''
        
        return self._getVariable8(TIC_DEVICERESET_VAR) 

    def getVinVoltage(self):
        '''Measured voltage on the VIN pin.

           units: mV'''
        
        return self._getVariable16(TIC_VINVOLTAGE_VAR) 

    def getUpTime(self):
        '''Time since the Tic’s microcontroller last experienced a full reset or 
           was powered up.

           units: ms
           
           A “reset” command does not affect this variable.'''
        
        return self._getVariable16(TIC_UPTIME_VAR) 

    def getEncoderPosition(self):
        '''Raw encoder count measured from the quadrature encoder inputs (TX and RX).

           units: ticks'''
        
        return self._getVariable32s(TIC_ENCODERPOSITION_VAR)

    def getRCPulseWidth(self):
        '''Reading from the RC pulse input. 0xFFFF means the reading is not available
           or invalid.

           units: 1/12 us'''
        
        return self._getVariable16(TIC_RCPULSEWIDTH_VAR)

    def getAnalogReadingSCL(self):
        '''Analog reading from the SCL pin, if analog readings are enabled for it. 
           0xFFFF means the reading is not available.

           units: 0 = 0 V,
                  0xFFFE ≈ voltage on 5V pin'''
        
        return self._getVariable16(TIC_ANAREADSCL_VAR)

    def getAnalogReadingSDA(self):
        '''Analog reading from the SDA pin, if analog readings are enabled for it.
           0xFFFF means the reading is not available.

           units: 0 = 0 V,
                  0xFFFE ≈ voltage on 5V pin'''
        
        return self._getVariable16(TIC_ANAREADSDA_VAR)

    def getAnalogReadingTX(self):
        '''Analog reading from the TX pin, if analog readings are enabled for it.
           0xFFFF means the reading is not available.

           units: 0 = 0 V,
                  0xFFFE ≈ voltage on 5V pin'''
        
        return self._getVariable16(TIC_ANAREADTX_VAR)

    def getAnalogReadingRX(self):
        '''Analog reading from the RX pin, if analog readings are enabled for it.
           0xFFFF means the reading is not available.
        
           units: 0 = 0 V,
                  0xFFFE ≈ voltage on 5V pin'''
        
        return self._getVariable16(TIC_ANAREADRX_VAR)

    def getDigitalReading(self):
        '''Digital readings from the Tic’s control pins. A set bit indicates that
           the pin is high.

           Bit 0: SCL
           Bit 1: SDA
           Bit 2: TX
           Bit 3: RX
           Bit 4: RC
           Bits 5–7: reserved'''
        
        return self._getVariable8(TIC_DIGREAD_VAR)

    def getPinStates(self):
        '''States of the Tic’s control pins, i.e. what kind of input or output
           each pin is.

           Bits 0–1: SCL
           Bits 2–3: SDA
           Bits 4–5: TX
           Bits 6–7: RX

           Each group of two bits encodes a number that represents one of
           the following states:

           0: High impedance
           1: Pulled up
           2: Output low
           3: Output high

           Note that the reported state might be misleading if the pin is being 
           used as a TTL serial or I²C pin. The state of the RC pin cannot be set.'''
        
        return self._getVariable8(TIC_PINSTATES_VAR)

    def getStepMode(self):
        '''Step mode of the Tic’s stepper driver (also known as microstepping mode), 
           which defines how many microsteps correspond to one full step.

           0: Full step
           1: 1/2 step
           2: 1/4 step
           3: 1/8 step'''

        return self._getVariable8(TIC_STEPMODE_VAR)

    def getCurrentLimit(self):
        '''Stepper motor coil current limit of the Tic’s stepper driver (0 to 124).'''

        return self._getVariable8(TIC_CURRENTLIMIT_VAR)

    def getDecayMOde(self):
        '''Decay mode of the Tic’s stepper driver.

           0: Automatic
           1: Slow
           2: Fast'''

        return self._getVariable8(TIC_DECLAYMODE_VAR)

    def getInputState(self):
        '''State of the Tic’s main input.

           0: Not ready
           1: Invalid
           2: Halt
           3: Target position
           4: Target velocity'''

        return self._getVariable8(TIC_INPUTSTATE_VAR)

    def getInputAfterAveraging(self):
        '''This variable is used in the process that converts raw RC and analog
           values into a motor position or speed. They are mainly for debugging 
           your input scaling settings in an RC or analog mode. 0xFFFF means 
           the reading is not available.'''

        return self._getVariable16(TIC_INPUTAVAR_VAR)

    def getInputAfterHysteresis(self):
        '''This variable is used in the process that converts raw RC and analog
           values into a motor position or speed. They are mainly for debugging 
           your input scaling settings in an RC or analog mode. 0xFFFF means 
           the reading is not available.'''

        return self._getVariable16(TIC_INPUTHYST_VAR)

    def getInputAfterScaling(self):
        '''Value of the Tic’s main input after scaling has been applied. 
           If the input is valid, this number is the target position or 
           target velocity specified by the input.

        units: Position: microsteps
               Velocity: microsteps per 10,000 s'''

        return self._getVariable32s(TIC_INPUTSCALE_VAR)      

if __name__ == '__main__':
    from smbus2 import SMBus

    #Open a handle to "/dev/i2c-3", representing the I2C bus.
    bus = SMBus(3)
 
    # Select the I2C address of the Tic (the device number).
    address = 14
 
    tic = pytic2(bus, address)
 
    position = tic.getCurrentPosition()
    print("Current position is {}.".format(position))