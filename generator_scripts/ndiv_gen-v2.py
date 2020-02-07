#coding: utf-8
from multiprocessing import Pool


def generate(divfact):
	f = open("uni-divfact-"+str(divfact)+".csv","w")
	f.write("x0,x1,y\n")
	for i in range(1,1000000):
		print ("TASK:",divfact," ; ["+str(i/1000000.0*100.0)+"%]")
		number = (i/(divfact*1.00))
		if (number-int(number) == 0):
			f.write(str(divfact)+","+str(i)+","+str(1)+"\n")
		else:
			f.write(str(divfact)+","+str(i)+","+str(0)+"\n")
	f.close()
maxo=1024

if __name__ == '__main__':
	with Pool(20) as p:
		p.map(generate,range(1,1024))

	f = open("uni-divfact-all.csv","w")
	for i in range(1,1024):
		f2 = open("uni-divfact-"+str(divfact)+".csv","r")
		f.write(f2.read())
		f2.close()
		f.close()
