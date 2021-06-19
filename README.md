# toggle-hyper-v
This tool automatically switch [Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/) on Windows 10 Pro.

## Installation
You can download the binary file from [this release page](https://github.com/takano536/toggle-hyper-v/releases).  

## Usage
ToggleHyperV.exe is a command line tool. Double-click to launch it. Run as administrator.  
The first line will show whether Hyper-V is now activated or not. The second line will ask if you want to switch Hyper-V.
```
Hyper-V is deactivated
Do you want to switch to Hyper-V? [Y/n] >
```
If you switch Hyper-V, you will be asked if you want to reboot, because Hyper-V will not switch completely without a reboot.
```
Hyper-V switching finished successfully
Do you want to reboot? [Y/n] >
```

## License
This software is released under the MIT License, see LICENSE.
