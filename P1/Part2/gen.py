import subprocess

try:
	subprocess.run(['fastcoll', '-p', 'prefix', '-o', 'col1', 'col2'], stdout=subprocess.DEVNULL)
	subprocess.run(["cat col1 suffix > 1.py"], shell=True)
	subprocess.run(["cat col2 suffix > 2.py"], shell=True)
	output = subprocess.check_output(["python3 1.py"], shell="True", stderr=subprocess.DEVNULL)
	sha1 = output.decode('utf-8').rstrip()
	output = subprocess.check_output(["python3 2.py"], shell="True", stderr=subprocess.DEVNULL)
	sha2 = output.decode('utf-8').rstrip()
	assert(sha1 != sha2)
except Exception as error:
	print("ERROR: %s" % error)
	exit(1)

