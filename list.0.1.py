#list_practice


BIR = []
Y = input('what is your year of birth?: ')
M = input('what is your month of birth?: ')
D = input('what is your date of birth?: ')

BIR.append(Y)
BIR.append(M)
BIR.append(D)


print('     ')
print(BIR[0], BIR[1], BIR[2], 'is your birthday!')
#print('2009' in BIR)
#print(len(BIR))
while True:
    if '2009' in BIR:
        print('You and I were born in the same year')
        if '03' in BIR:
            print('You and I were born in the same month')
            if '16' in BIR:
                print('You and I were born in the same day')
                break
    if '16' in BIR:
	    print('You and I were born in the same date')
	    break
    if '3' in BIR:
	    print('You and I were born in the same month')	
	    break	