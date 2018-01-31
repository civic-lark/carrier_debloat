import os
from sys import argv, exit

def debloat_moto_e4(kill_file):
	try:
		with open(kill_file, 'rb') as AL:
			for app in AL.readlines():
				cmd = "adb shell pm uninstall -k --user 0 %s" % app.strip()
				os.system(cmd)

		return True

	except Exception as e:
		print e

	return False

if __name__ == "__main__":
	debloat = debloat_moto_e4(argv[1])
	exit(0 if debloat else -1)