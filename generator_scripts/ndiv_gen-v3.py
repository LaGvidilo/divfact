#coding: utf-8
from multiprocessing import Pool


def generate(divfact):
	f = open("uni-divfact-F.csv","a")
	f.write("x0,x1,y\n")
	for i in range(1,1000):
		print ("TASK:",divfact," ; ["+str(i/1000.0*100.0)+"%]")
		number = (i/(divfact*1.00))
		if (number-int(number) == 0):
			f.write(str(divfact)+","+str(i)+","+str(1)+"\n")
		else:
			f.write(str(divfact)+","+str(i)+","+str(0)+"\n")
	f.close()
maxo=1024

if __name__ == '__main__':
	with Pool(4) as p:
		p.map(generate,range(1,512))






"""
#THAT NEXT AFTER THIS COMMENT IS FOR PYTHON 2.7 !!!
def ptn1():
	BUFFER = ""
	for i in range(1,1024):
		with open("uni-divfact-"+str(i)+".csv", 'r') as content_file:
			BUFFER = BUFFER + "\n".join(content_file.read().strip().split("\n")[1:])+"\n"
		print (i, " - STEP OK.")
	return BUFFER

f = open("uni-divfact-all.csv","w")
f.write("x0,x1,y\n")
f.write(ptn1())
f.close()
"""