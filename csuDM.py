


def init(filename, header):
	
	fstring = filename[:-4] + "\n"
	for val in header:
		fstring = fstring + str(val) + ", "
	fstring = fstring[:-2] + "\n"
	f = open("Data/" + filename, 'w')
	f.write(fstring)
	f.close()

def write(filename, dArray):
	fstring = ""
	for val in dArray:
		fstring = fstring + str(val) + ', '
	fstring = fstring[:-2] + '\n'
	f = open("Data/" + filename, 'a')
	f.write(fstring)
	f.close()


def pad(dArray)
	i = 0
	padVals = [2, 7, 2, 5, 5, 6, 6]
	decVals = ["0.0", "0.4", "0.0", "0.2", "0.2", "0.3", "0.0"]
	for sArray in dArray:
		j = 0
		for val in sArray:
			dArray[i][j] = ((("%{}f").format(decVals[i])) % val).zfill(padVals[i])
			j += 1
		i += 1
	return dArray



def formatString(dArray):
	dArray = pad(dArray)
	txByteString = ""
	for sArray in dArray:
		for val in sArray:
			txByteString = txByteString + val
	return bytes(txByteString, "utf-8")
