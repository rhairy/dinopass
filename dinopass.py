from urllib.request import urlopen

SIMPLE_URL = "http://www.dinopass.com/password/simple"
COMPLEX_URL = "http://www.dinopass.com/password/strong"

def GetSimplePassword():
	response = urlopen(SIMPLE_URL)
	bytes = response.readline()
	return bytes.decode()
	
def GetComplexPassword():
	response = urlopen(COMPLEX_URL)
	bytes = response.readline()
	return bytes.decode()