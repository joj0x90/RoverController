#!/bin/bash

# Path for all GPIOs
BASE_GPIO_PATH=/sys/class/gpio

M1_l=2
M1_r=3
M2_l=4
M2_r=17

ON="1"
OFF="0"

exportPin()
{
	if [ ! -e $BASE_GPIO_PATH/gpio$1 ]; then
		echo "$1" > $BASE_GPIO_PATH/export
	fi
}

# export all Pins
exportPin $M1_l
exportPin $M1_r
exportPin $M2_l
exportPin $M2_r

# setting all pins as output
echo "out" > $BASE_GPIO_PATH/gpio$M1_l/direction
echo "out" > $BASE_GPIO_PATH/gpio$M1_r/direction
echo "out" > $BASE_GPIO_PATH/gpio$M2_l/direction
echo "out" > $BASE_GPIO_PATH/gpio$M2_r/direction
