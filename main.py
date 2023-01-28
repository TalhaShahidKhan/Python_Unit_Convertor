#Making an Unit Converter.
import Time
import Area
import Temprature
import Length
import Weight
TimeC=Time.Time()
TempC=Temprature.Temperature()
AreaC=Area.Area()
LenC=Length.Length()
WeC=Weight.Weight()
print("##### Talha's UNIT CONVERTER #####")
print("Select your Convert Topic =>")
print(" 1/ Temperature \n 2/ Time \n 3/ Area \n 4/ Length \n 5/ Weight")
InputTopic=int(input("Enter a Topic number: "))
if InputTopic==1:
    print("Temperature Conversion.")
    TEM_input=int(input("Convert => \n "
                    "1/Celsius--Fahrenheit \n 2/Fahrenheit--Kalvin \n 3/Kalvin--Celsius \n "
                    "4/Celsius--Kalvin \n 5/Fahrenheit--Celsius \n 6/Kalvin--Fahrenheit \n"))
    if TEM_input==1:
        Cel=int(input("Enter Celsius Temperature: "))
        result=TempC.Celcius_Farenhit(Cel)
        print(f"Your Output {result}")
    elif TEM_input==2:
        Fahr=int(input("Enter Fahrenheit Temperature: "))
        result=TempC.Farenhit_Kelvin(Fahr)
        print(f"Your Output {result}")
    elif TEM_input==3:
        Kal=int(input("Enter Kalvin Temperature: "))
        result=TempC.Kelvin_Celcius(Kal)
        print(f"Your Output {result}")
    elif TEM_input==4:
        Cel=int(input("Enter Celsius Temperature: "))
        result=TempC.Celcius_Kelvin(Cel)
        print(f"Your Output {result}")
    elif TEM_input==5:
        Farh=int(input("Enter Fahrenheit Temperature: "))
        result=TempC.Farenhit_Celcius(Farh)
        print(f"Your Output {result}")
    elif TEM_input==6:
        Kal=int(input("Enter Kalvin Temperature: "))
        result=TempC.Kelvin_Farenhit(Kal)
        print(f"Your Output {result}")
    else:
        print("You have done an ERROR! Please enter a valid input!")


elif InputTopic==2:
    print("Time Conversion.")
    Time_Input=int(input("Convert \n "
                     "1/Hour--Minute \n 2/Minute--Seconds \n 3/Seconds--Minute \n "
                     "4/Minute--Hour \n 5/Hour--Seconds \n 6/Seconds--Hours \n "))
    if Time_Input== 1:
        hour=int(input("Enter your Time in Hour Format: "))
        result=TimeC.H_M(hour)
        print(f"Your output is {result}")
    elif Time_Input==2:
        min=int(input("Enter your Time in Minute Format: "))
        result=TimeC.M_S(min)
        print(f"Your output is {result}")
    elif Time_Input== 3:
        sec=int(input("Enter your Time in Second Format: "))
        result=TimeC.S_M(sec)
        print(f"Your output is {result}")
    elif Time_Input==4:
        min=int(input("Enter your Time in Minute Format: "))
        result=TimeC.M_H(min)
        print(f"Your output is {result}")
    elif Time_Input==5:
        hour=int(input("Enter your Time in Hour Format: "))
        result=TimeC.H_S(hour)
        print(f"Your output is {result}")
    elif Time_Input==6:
        sec=int(input("Enter your Time in Second Format: "))
        result=TimeC.S_H(sec)
        print(f"Your output is {result}")
    else:
        print("You have done an ERROR! Please enter a valid input!")


elif InputTopic==3:
    print("Area Conversion")
    Are_Input=int(input("Convert => \n "
                        "1/m\u00b2--cm\u00b2  2/cm\u00b2--m\u00b2 3/km\u00b2--m\u00b2 \n "
                        "4/m\u00b2--km\u00b2 5/cm\u00b2--mm\u00b2 6/mm\u00b2--cm\u00b2 \n "
                        "7/m\u00b2--mm\u00b2 8/mm\u00b2--m\u00b2 9/km\u00b2--mm\u00b2 \n "
                        "10/mm\u00b2--km\u00b2 11/cm\u00b2--km\u00b2 12/km\u00b2--cm\u00b2 \n"))
    if Are_Input==1:
        m2=int(input("Enter Your area in m\u00b2: "))
        result=AreaC.M2_Cm2(m2)
        print(f"Your output is {result} cm\u00b2")
    elif Are_Input==2:
        cm2=int(input("Enter your area in cm\u00b2: "))
        result=AreaC.Cm2_M2(cm2)
        print(f"Your output is {result} m\u00b2")
    elif Are_Input==3:
        km2=int(input("Enter your area in km\u00b2: "))
        result=AreaC.Km2_M2(km2)
        print(f"Your output is {result} m\u00b2")
    elif Are_Input==4:
        m2=int(input("Enter your area in m\u00b2: "))
        result=AreaC.M2_Km2(m2)
        print(f"Your output is {result} km\u00b2")
    elif Are_Input==5:
        cm2=int(input("Enter your area in cm\u00b2: "))
        result=AreaC.Cm2_MM2(cm2)
        print(f"Your output is {result} mm\u00b2")
    elif Are_Input==6:
        mm2=int(input("Enter your area in mm\u00b2: "))
        result=AreaC.MM2_Cm2(mm2)
        print(f"Your output is {result} cm\u00b2")
    elif Are_Input==7:
        m2=int(input("Enter your area in m\u00b2: "))
        result=AreaC.M2_MM2(m2)
        print(f"Your output is {result} mm\u00b2")
    elif Are_Input==8:
        mm2=int(input("Enter your area in mm\u00b2: "))
        result=AreaC.MM2_M2(mm2)
        print(f"Your output is {result} m\u00b2")
    elif Are_Input==9:
        km2=int(input("Enter your input in km\u00b2: "))
        result=AreaC.Km2_MM2(km2)
        print(f"Your output is {result} mm\u00b2")
    elif Are_Input==10:
        mm2=int(input("Enter your area in mm\u00b2: "))
        result=AreaC.MM2_Km2(mm2)
        print(f"Your output is {result} km\u00b2")
    elif Are_Input==11:
        cm2=int(input("Enter your area in cm\u00b2: "))
        result=AreaC.Cm2_Km2(cm2)
        print(f"Your output is {result} km\u00b2")
    elif Are_Input==12:
        km2=int(input("Enter your area in km\u00b2: "))
        result=AreaC.Km2_Cm2(km2)
        print(f"Your output is {result} cm\u00b2")
    else:
        print("You have done an ERROR! Please Enter a valid input.")

elif InputTopic== 4:
    print("Length Conversion.")
    Len_Input = int(input("Convert => \n "
                          "1/m--cm  2/cm--m 3/km--m \n "
                          "4/m--km 5/cm--mm 6/mm--cm \n "
                          "7/m--mm 8/mm--m 9/km--mm \n "
                          "10/mm--km 11/cm--km 12/km--cm \n"))
    if Len_Input==1:
        m=int(input("Enter your Length in Meter Format: "))
        result=LenC.M_Cm(m)
        print(f"Your output is {result}")
    elif Len_Input==2:
        cm=int(input("Enter your Length in Centi-meter Format: "))
        result=LenC.Cm_M(cm)
        print(f"Your output is {result}")
    elif Len_Input==3:
        km=int(input("Enter your Length in Kilo-meter Format: "))
        result=LenC.Km_M(km)
        print(f"Your output is {result}")
    elif Len_Input==4:
        m=int(input("Enter your Length in Meter Format: "))
        result=LenC.M_Km(m)
        print(f"Your output is {result}")
    elif Len_Input==5:
        cm=int(input("Enter your Length in Centi-meter Format: "))
        result=LenC.Cm_MM(cm)
        print(f"Your output is {result}")
    elif Len_Input==6:
        mm=int(input("Enter your Length in Mile-meter Format: "))
        result=LenC.MM_Cm(mm)
        print(f"Your output is {result}")
    elif Len_Input==7:
        m=int(input("Enter your Length in Meter Format: "))
        result=LenC.M_MM(m)
        print(f"Your output is {result}")
    elif Len_Input==8:
        mm=int(input("Enter your Length in Mile-meter Format: "))
        result=LenC.MM_M(mm)
        print(f"Your output is {result}")
    elif Len_Input==9:
        km=int(input("Enter your Length in Kilo-meter Format: "))
        result=LenC.Km_MM(km)
        print(f"Your output is {result}")
    elif Len_Input==10:
        mm=int(input("Enter your Length in Mile-meter Format: "))
        result=LenC.MM_Km(mm)
        print(f"Your output is {result}")
    elif Len_Input==11:
        cm=int(input("Enter your Length in Centi-meter Format: "))
        result=LenC.Cm_Km(cm)
        print(f"Your output is {result}")
    elif Len_Input==12:
        km=int(input("Enter your Length in Kilo-meter Format: "))
        result=LenC.Km_Cm(km)
        print(f"Your output is {result}")
    else:
        print("You have done an ERROR! Please enter a valid input.")


elif InputTopic== 5:
    print("Weight Conversion.")
    Wei_Input=int(input("Convert =>"
                        "1/kg--g \n 2/g--kg \n 3/g--mg \n 4/mg--g \n 5/kg--mg \n 6/mg--kg \n"))
    if Wei_Input==1:
        kg=int(input("Enter your Weight in Kilogram: "))
        reslut=WeC.KG_G(kg)
        print(f"Your output is {reslut}")
    elif Wei_Input==2:
        g=int(input("Enter your Weight in Gram: "))
        reslut=WeC.G_KG(g)
        print(f"Your output is {reslut}")
    elif Wei_Input==3:
        g=int(input("Enter your Weight in Gram: "))
        result=WeC.G_MlG(g)
        print(f"Your output is {result}")
    elif Wei_Input==4:
        mg=int(input("Enter your Weight in Milegram: "))
        result=WeC.MlG_G(mg)
        print(f"Your output is {result}")
    elif Wei_Input==5:
        kg=int(input("Enter your Weight in Kilogram: "))
        result=WeC.KG_MlG(kg)
        print(f"Your output is {result}")
    elif Wei_Input==6:
        mg=int(input("Enter your Weight in Milegram: "))
        reslut=WeC.MlG_KG(mg)
        print(f"Your output is {reslut}")