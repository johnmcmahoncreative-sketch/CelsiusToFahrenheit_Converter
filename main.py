class Temperature:
    def __init__(self, ctemp,ftemp):
        self.Ctemp = ctemp
        self.Ftemp = ftemp
    def C_to_f(self):
        return (1.8 * self.Ctemp) + 32
    def F_to_C(self):
        return (self.Ftemp- 32) / 1.8
try:
    from colorama import Fore,init
    init()
    import sys
    Celsius = int(input(Fore.GREEN+"[*]Type in The Temperature in Celsius:"))
    Fahrenheit = int(input(Fore.BLUE+"[*]Type in The Temperature in Fahrenheit:"))
    sys.stdout.write(Fore.BLUE+f"[#]You Typed:{int(Celsius)}")
    call = Temperature(Celsius,Fahrenheit)
    sys.stdout.write(Fore.LIGHTBLACK_EX+f"\n[+]The temperature in Fahrenheit is:{int(call.C_to_f())}")
    sys.stdout.write(Fore.LIGHTBLACK_EX+f"\n[+]The temperature in Celsius is:{int(call.F_to_C())}")
except ValueError as e:
    sys.stdout.write(Fore.RED+"[!]Please typein a number not an string!")
except KeyboardInterrupt:
    print(Fore.RED+"Keyboard Interrupt Detected!")