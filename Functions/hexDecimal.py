class HexDecimal:
    def __init__(self,inputString):
        self.inputString = inputString
        pass
    def HexDecimalConvertion(self):
        list1 = []
        for i in range(len(self.inputString)):
            list1.insert(i,hex(ord(self.inputString[i])))
        # print(list1)
        list2 = []
        for i in list1:
            text = ""
            for j in range(2,len(i)):
                if i[j]=="0":
                    text=text+"0000"
                if i[j]=="1":
                    text=text+"0001"
                if i[j]=="2":
                    text=text+"0010"
                if i[j]=="3":
                    text=text+"0011"
                if i[j]=="4":
                    text=text+"0100"
                if i[j]=="5":
                    text=text+"0101"
                if i[j]=="6":
                    text=text+"0110"
                if i[j]=="7":
                    text=text+"0111"
                if i[j]=="8":
                    text=text+"1000"
                if i[j]=="9":
                    text=text+"1001"
                if i[j]=="a" or i[j]=='A':
                    text=text+"1010"
                if i[j]=="b" or i[j]=='B':
                    text=text+"1011"
                if i[j]=="c" or i[j]=='C':
                    text=text+"1100"
                if i[j]=="d" or i[j]=='D':
                    text=text+"1101"
                if i[j]=="E" or i[j]=='e':
                    text=text+"1110"
                if i[j]=="F" or i[j]=='f':
                    text=text+"1111"
            list2.append(text)
        list3 = []
        for i in range(len(list2)):
            list3.append(0)
        r=0
        for i in range(len(list2)-1,-1,-1):
            list3[r]=list2[i]
            r=r+1    
        return list3