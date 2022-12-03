from Functions import PexXorAlgorithm
from Functions import HexDecimal
from Functions import bit_string
from Functions import Inverse_Per_XOR

obj1 = PexXorAlgorithm()
ValueInBits = obj1.Encryption("T")
print(ValueInBits)

obj2 = bit_string(ValueInBits)
ValueInCipher = obj2.bit_StringConversion()
print(ValueInCipher)

obj3=Inverse_Per_XOR()
ValueInCiPherBits = obj3.Encryption(ValueInCipher)
print(ValueInCiPherBits)

obj4 = bit_string(ValueInCiPherBits)
ValueInCipher = obj4.bit_StringConversion()
print(ValueInCipher)
