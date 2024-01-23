from time import sleep
from pynput.keyboard import Key, Controller

codes = [
'Goalienware',
'ATOC2015',
'GOAMGENTOC',
'Athlonia',
'GOBATTENKILL',
'BICYCLINGMAG',
'BIKERADAR',
'BIKEANDBEER',
'CANBERRACCKIT',
'GOCIS',
'CRCANYC',
'D.CYCLE4GOOD',
'DoCoMo',
'GOELITE',
'GOFREESPEED',
'GoGCN',
'GEARPATROL',
'GEELONGCCKIT',
'GOLDCOAST',
'GOLONGRIDERS',
'GOVISION',
'GOINGAMBA',
'Hikkit32616',
'JENSIE',
'LAFUGA.CC',
'LAVA',
'Dynamo',
'MTSKIT',
'MGCCKit',
'NCCMAKIT',
'PCGKIT32516',
'GOPEARSON',
'RIDEPOWERTAP',
'RIDEQUARQ',
'RADAVIST',
'RIDEAUSTRALIA',
'ROAD.CC',
'GOSKRYE',
'SIGMASPORT',
'SLOWTWITCH',
'SOIGNEURDK',
'STKILDA2015KIT',
'SYDNEYCCKIT',
'GOTACX',
'TDP2015',
'GOTRAINSHARP',
'TRIATHLETEMAG',
'TSBIKES',
'GOUSMES',
'VCGHKIT',
'WAHOOFITNESS',
'GOWBR',
'GOWSR',
'ZTHKIT'
]

sleep(5)
for code in codes:
	keyboard = Controller()

	keyboard.press('p')
	keyboard.release('p')
	sleep(0.2)
	keyboard.type(code)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)

	sleep(0.2)
print('done')