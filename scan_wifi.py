import subprocess
import time

commander_ssid = "Villa"

while True:
	results = subprocess.check_output(["netsh", "wlan", "show", "networks"])
	results = results.decode("ascii") # needed in python 3
	results = results.replace("\r","")
	ls = results.split("\n")
	ls = ls[4:]
	ssids = []
	x = 0
	while x < len(ls):
		if x % 5 == 0:
			ssids.append(ls[x][9:])
		x += 1
	parasable_ssids = []
	for x in ssids:
		if x:
			parasable_ssids.append(x)
		else:
			print("Malformed SSID Ignored")
			

	for network_ssids in parasable_ssids:
		broken_pieces = network_ssids.split(" ")
		if broken_pieces[0] == commander_ssid:
			ssid_cmd_check = len(network_ssids.split(" "))
			if ssid_cmd_check > 1:
				command = network_ssids.split(" ", 1)[1]
				print("SSID Found : New Command : " + command)
			else:
				print("SSID Found : No Command")
	time.sleep(1)