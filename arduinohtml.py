def raw2arduino():
	i = open("raw.html", 'r')
	o = open("arduino.html", 'a')
	for line in i.readlines():
		o.write('client.println("')
		o.write(line.strip("\n"))
		o.write('");\n')
	i.close()
	o.close()
	print "Done!"

def arduino2raw():
	i = open("arduino.html", 'r')
	o = open("raw.html", 'a')
	for line in i.readlines():
		o.write(line[15:-3].strip('"'))
		o.write("\n")
	i.close()
	o.close()
	print "Done!"

if __name__ == '__main__':
	d = raw_input("Copy the files you want to convert in this folder as 'raw.html' and 'arduino.html' \n Which conversion do you wanna do? \n 1. HTML to Arduino \n 2. Arduino to HTML\n")
	if d == "1":
		raw2arduino()
	elif d == "2":
		arduino2raw()
	else:
		print "Invalid input"
