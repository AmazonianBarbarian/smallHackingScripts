#!/bin/bash
# meant to be built into a script that can scan a network for valid IPs
# Will add a more easily read list and give functionality to modify how many subnets it will scan.
declare -i ipEndOctet=1

while [ $ipEndOctet -le 255 ]; do
        ping -c 1 192.168.1.$ipEndOctet;
        ipEndOctet=$((ipEndOctet + 1))
done

