#ISA Values
ISA_Temp = float(15)
Laps_Rate = float(-1.98)
ISA_pressure=float(1013.25)

#input fields
Alt=float(input("Airfiel Altitude: "))
QNH=float(input("Airfield QNH: "))
Temp=float(input("Airfield Temprature: "))

#calculations
AltTemp=(((Alt * Laps_Rate) / float(1000))+15)
PA=(Alt-((QNH-ISA_pressure)*30))
DA=(PA+(((Temp-(((PA * Laps_Rate)/float(1000))+15))*float(120))))


#Outputs
#print("------Tempratures--------")
#print("ISA Airfield Temp: " "%0.2f" % AltTemp)
#print("Airfield Temp: " "%0.2f"%Temp)
print ("------Airfield Altitudes-------")
print("Airfield Pressure Alt: " "%0.2f" % PA,"ft")
print("Airfield Density Altitude :" "%0.2f" % DA,"ft")