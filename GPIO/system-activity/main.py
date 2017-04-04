#! /usr/bin/env python

from gpiozero import LED
from time import sleep
import psutil

rled = LED(26)
gled = LED(21)
bled = LED(20)
wled = LED(19)

disk = psutil.disk_usage("/")
dUsed = disk.used

network = psutil.net_io_counters(pernic = True)
nWlanSend = network['wlan0'].packets_sent
nWlanRecv = network['wlan0'].packets_recv

while True:

	# Check users
	ulist = psutil.users()
	for user in ulist:
		if user.terminal[:4] == "pts/":
			bled.on()

	# Check for disk usage
	disk = psutil.disk_usage("/")
	if dUsed != disk.used:
		dUsed = disk.used
		gled.on()

	# Check for wlan activity
	network = psutil.net_io_counters(pernic = True)
	sent = network['wlan0'].packets_sent
	recv = network['wlan0'].packets_recv
	if nWlanSend + 10 < sent:
		rled.on()
	if nWlanRecv + 10 < sent:
		wled.on()
	if nWlanSend != sent:
		nWlanSend = network['wlan0'].packets_sent
	if nWlanRecv != recv:
		nWlanRecv = network['wlan0'].packets_recv

	# Wait until off
	sleep(0.2)

	rled.off()
	gled.off()
	bled.off()
	wled.off()

	sleep(0.2)
