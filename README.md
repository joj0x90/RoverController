# Rover Controller:
## This repo contains a controlling software for a robot with two motors, similiar to a model tank.

The Rover is controlled by a Raspberry Pi 2 B+.  
As this repo is for a model tank, you may have to modify the code to fit your needs and your vehicle.  
--  
The Rover's motors are controlled by a Dual H-Bridge (in this case I used a *L298N*)  
**PLEASE NOTE: The shell-script: *gpio_init.sh* should be executed before starting the python-program.**  
Otherwise the GPIOs are not set as output, which may cause overheating, which can damage the H-Bridge. (Trust me, I learned this the hard way)  
Best would be to place the according command to execute the shell-script inside the autostart of your Pi (e.g. */etc/rc.local*)  
