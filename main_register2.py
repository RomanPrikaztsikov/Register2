from Register2 import *

while True:
    print("VALIK:")
    print("1. Registreerimine")
    print("2. Sisse logimine")
    print("3. Parooli muutmine")
    print("4. Parooli taastamine")
    print("5. Välja logimine")
    
    if sees:
        print(f"Tere, {user}!")
    
    v=input("Valik: ")
    
    if v=="1":
        reg()
    elif v=="2":
        login()
    elif v=="3":
        parool()
    elif v=="4":
        taasta()
    elif v=="5":
        logout()
        break
    else:
        print("Vale valik")
