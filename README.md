# pulseblaster
Python control code for Pulseblaster pulse generation hardware.

This code creates an object (PBInd) that relies on the [SpinCore spinapi.py wrapper](http://www.spincore.com/support/SpinAPI_Python_Wrapper/spinapi.py) to program individual pulseblaster pins independently.

# Installation

## Prerequisites

Spin Core Driver: http://www.spincore.com/support/spinapi/

## Python Install

```
> cd pulseblaster
> python -m pip install .
```

# Usage

## Examples

[pb_infinite_on_example.py](pb_infinite_on_example.py)
[pb_infinite_square_wave_example.py](pb_infinite_square_wave_example.py)
