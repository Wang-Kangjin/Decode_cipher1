import time
def getSample(filename):
	fp = open(filename)
	content = fp.readline()
	fp.close()
	contentList = content.split(',')
	return contentList

def decodeas(sample,first,second,third):
	count = 0
	decodestr=''
	returnResult=[]
	for item in sample:
		if count is 0:
			decodestr = decodestr+chr(first^int(item))
		elif count is 1:
			decodestr = decodestr+chr(second^int(item))
		elif count is 2:
			decodestr = decodestr+chr(third^int(item))
		count = (count + 1)%3
	
	return decodestr

def decode(sample):
	res={}
	for first in range(97,122):
		for second in range(97,122):
			for third in range(97,122):
				decoderes = decodeas(sample,first,second,third)
				key = chr(first)+chr(second)+chr(third)
				if decoderes.find('the') !=-1:
					res[key] = decoderes
	return res

def decoderesult(source,key):
	pass

def main():
	sample = getSample('data/cipher1.txt')
	decodedict= decode(sample[:120])

	for each in decodedict:
		print each
		print decodedict[each]
		time.sleep(1)

	print decodeas(sample, ord('g'), ord('o'), ord('d'))



main()