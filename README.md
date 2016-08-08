# Incentives-Based Candy Dispenser

This is the source code of a machine to dispense candy when you have earned it.

## Features

* Dispenses candy
* Toggl
* IMAP
* Facebook, Reddit

## Hardware Requirements

* Raspberry Pi Zero
* Micro-SD card
* USB Wifi adapter
* Micro-USB-to-USB OTG adapter
* 180 degree servo motor

## Software

This system is intended to run in a Raspbian environment.

## Install

    sudo apt install git python-pip python-setuptools python-dev python-rpi.gpio
	git clone https://github.com/richardghirst/PiBits.git
	cd PiBits/ServoBlaster/user/
	make servod
	sudo cp servod /usr/local/sbin/
	sudo chown root:root /usr/local/sbin/servod
	sudo chmod u+s /usr/local/sbin/servod
	pip install -r requirements.txt

## How to get candy

* Start your first Toggl before 8:35
* Respond to e-mails within 10 working hours
* Toggl 1 hour work time with no Facebook or Reddit activity
* Your lunch break starts 11:20-12:45 and is 30-80 minutes long
* Have five Toggld hours at 15:00

## License

candycrush - Incentives-based candy cispenser

Copyright (C) 2016  Emil Vikström

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
