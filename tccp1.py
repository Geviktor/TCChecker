def checkTc(tc):
	#-------Check TC Syntaxi------- 
	hatali = [11111111110,22222222220,33333333330,44444444440,55555555550,66666666660,77777777770,88888888880,99999999990]	

	if len(tc) != 11: return False
	if int(tc[0]) == 0: return False	

	for i in hatali:
		if int(tc) == i:
			return False

	#-------Check index 9 int-------
	tek = int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])	
	tek = tek * 7

	cift = int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7])

	sonuc = abs(tek - cift)
	
	if (sonuc % 10) != int(tc[9]): return False

	#-------Check index 10 int-------
	TCToplam = 0
	for i in range(10):
		TCToplam += int(tc[i])
		
	if (TCToplam % 10) != int(tc[10]): return False
	
	#-------If TC is can be available return true-------
	return True

tc = input("Tc: ")
x = checkTc(tc)

print(x)
