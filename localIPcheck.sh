#!/bin/bash
# meant to be built into a script that can scan a network for valid IPs
declare -i ipEndOctet=1
deviceList=""

echo "Map of detectable devices on the current local network. "
echo "--------------------------------------------------------"
while [ $ipEndOctet -le 255 ]; do # Scans up to 255. Change the integer in the condition to change how many devices on the subnet are pinged.
	ping -c 1 192.168.1.$ipEndOctet > /dev/null 2>&1;
	if [ $? -ne 0 ]; then
		echo "scan result: 192.168.1.$ipEndOctet not detected"
	else
		deviceList+="192.168.1.$ipEndOctet\\n"
		echo "scan result: 192.168.1.$ipEndOctet detected"
	fi
	ipEndOctet=$((ipEndOctet + 1))
done
echo "----------------"
echo "List of devices:"
echo "----------------"
echo -e $deviceList;


