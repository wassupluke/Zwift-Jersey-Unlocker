from time import sleep
import keyboard

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
	keyboard.press_and_release('p')
	sleep(0.2)
	keyboard.write(code)
	keyboard.press_and_release('enter')
	sleep(0.2)
print('done')