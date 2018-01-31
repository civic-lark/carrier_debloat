import os
from sys import argv, exit

def debloat_phone(kill_file):
	try:
		with open(kill_file, 'rb') as KF:
			for app in KF.readlines():
				os.system("adb shell pm uninstall -k --user 0 %s" % app.strip())

		return True

	except Exception as e:
		print e

	return False

if __name__ == "__main__":
	debloat = debloat_phone(argv[1])
	exit(0 if debloat else -1)