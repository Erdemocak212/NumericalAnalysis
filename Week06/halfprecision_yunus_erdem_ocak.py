import struct

class HalfPrecision:
    def __init__(self, number):
        if not isinstance(number, float):
            raise TypeError("Input must be a float.")
        self.number = number

    def __str__(self):
        bits32 = struct.unpack('>I', struct.pack('>f', self.number))[0]

        sign = (bits32 >> 31) & 0x1
        exponent = (bits32 >> 23) & 0xFF
        mantissa = bits32 & 0x7FFFFF

       
        if exponent == 255: 
            exp16 = 31
            man16 = 0 if mantissa == 0 else 1  
        elif exponent == 0:  
            exp16 = 0
            man16 = 0
        else:
            exp16 = exponent - 127 + 15
            if exp16 <= 0:  
                exp16 = 0
                man16 = 0
            elif exp16 >= 31: 
                exp16 = 31
                man16 = 0
            else:
                man16 = mantissa >> 13  

        binary_str = f"{sign:01b}{exp16:05b}{man16:010b}"
        return binary_str


print(str(HalfPrecision(1.0)))      
print(str(HalfPrecision(float('inf')))) 
print(str(HalfPrecision(-2.5)))     
