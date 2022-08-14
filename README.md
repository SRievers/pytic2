# PyTic2
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Getting started
`PyTic2` is a Python wrapper for the Pololu Tic Stepper Motor Controller series.
It is similar and inspired by the [PyTic](https://github.com/AllenInstitute/pytic) driver developed by the Allen Institute. The `PyTic2` driver is intended to be used on a Raspberry PI and uses the I2C interface for the communication with the Pololu Tic Stepper Motor Controllers. The API consists of the commands defined in the [Tic Stepper Motor Controller User’s Guide](https://www.pololu.com/docs/0J71)

### Prerequisites

The communication with Pololu Stepper driver is done over the I2C interface and the smbus2 driver is required. The smbus2 driver can be pip installed.

  ```sh
  pip install smbus2
  ```
Please refer to the Section [15.8](https://www.pololu.com/docs/0J73/15.8) in the Pololu documentation for more detailed information 

### Installation
TODO

```
pip install pytic2
```

## Usage
TODO

## License
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)



