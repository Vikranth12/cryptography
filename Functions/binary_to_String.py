class bit_string:
    def __init__(self,inputString): 
        self.inputString = inputString
    
    def valuer(self,stringValue):
        if stringValue=="0000":
            return "0"
        if stringValue=="0001":
            return "1"
        if stringValue=="0010":
            return "2"
        if stringValue=="0011":
            return "3"
        if stringValue=="0100":
            return "4"
        if stringValue=="0101":
            return "5"
        if stringValue=="0110":
            return "6"
        if stringValue=="0111":
            return "7"
        if stringValue=="1000":
            return "8"
        if stringValue=="1001":
            return "9"
        if stringValue=="1010":
            return "A"
        if stringValue=="1011":
            return "B"
        if stringValue=="1100":
            return "C"
        if stringValue=="1101":
            return "D"
        if stringValue=="1110":
            return "E"
        if stringValue=="1111":
            return "F"

    
    def bit_StringConversion(self):
        list1 = []
        for i in range(0,len(self.inputString),8):
            list1.append(self.inputString[i:i+8])
        list2 = []
        for i in list1:
            textValue = ""
            j1 = str(i[0])+str(i[1])+str(i[2])+str(i[3])
            j2 = str(i[4])+str(i[5])+str(i[6])+str(i[7])
            textValue = self.valuer(j1)+self.valuer(j2)
            list2.append(textValue)
        textString = ""
        list3 = []
        for i in list2:
            list3.append(int(i,16))
        textDescription =""
        for i in list3:
            textDescription=textDescription+chr(i)
        return textDescription
        
            
