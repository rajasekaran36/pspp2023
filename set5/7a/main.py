'''
7a) Write a Python Program to Calculate the Weight of the Motor Bike
'''

bike_parts = {
    'frame':1809,'wheelset':1658,'crankset':769,'discbrakes':526,
    'shifters':355,'rimbrakes':323,'handlebar':293,'seatpost':264,
    'chain':261,'cassette':254,'hub':247,'saddle':247,'derailleur':221,
    'pedals':220,'stem':142,'headset':111,'bottombracket':95,'seatclamp':25
}

total_weight = 0

for part in bike_parts:
    print(part,'=',bike_parts[part],'g')
    total_weight += bike_parts[part]

print('Total weight=',(total_weight/1000),'kg')