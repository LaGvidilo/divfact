#coding: utf-8

def generate(divfact=2):
	f = open("divfact-"+str(divfact)+".csv","w")
	f.write("divfact,x0,y\n")
	for i in range(1,10000000):
		print divfact/(maxo*1.0)*100.0," ; ["+str(i/10000000.0*100.0)+"%]"
		number = (i/(divfact*1.00))
		if (number-int(number) == 0):
			f.write(str(divfact)+","+str(i)+","+str(1)+"\n")
		else:
			f.write(str(divfact)+","+str(i)+","+str(0)+"\n")
	f.close()
maxo=129
for i in range(2,129):
	generate(i)
