from hex_dec import HexDecimal

class PexXorAlgorithm:
    
    def __init__(self) -> None:
        self.key="O"
    
    def Encryption(self,message):
        self.message = message
        keyGenerationobj = HexDecimal(self.key)
        keyGeneration = keyGenerationobj.HexDecimalConvertion()
        Keytext = ""
        for i in keyGeneration:
            Keytext=Keytext+i
        MessageGenerationobj = HexDecimal(self.message)
        MessageGeneration = MessageGenerationobj.HexDecimalConvertion()
        MessageText = ""
        for i in MessageGeneration:
            MessageText = MessageText + i
        if len(Keytext)==len(MessageText):
            i = 0
            j = len(MessageText)-1
            ptr = len(MessageText)-1
            c=[]
            for i1 in range(len(MessageText)):
                c.append(0)
            for m in range(0,len(MessageText)):
                if Keytext[j]==1:
                    c[j]=MessageText[ptr]
                    ptr=ptr-1
                    j=j-1
                else:
                    c[i]=MessageText[ptr]
                    ptr=ptr-1
                    i=i+1
                
            permutationText=""
            for i1 in c:
                permutationText=permutationText+i1
            cipher = []
            for i in range(len(MessageText)):
                cipher.append(0)
            for i in range(len(MessageText)):
                if permutationText[i]==Keytext[i]:
                    cipher[i]=0
                else:
                    cipher[i]=1
            cipherText = ""
            for i1 in cipher:
                cipherText=cipherText+str(i1)
            # print(cipherText)
            # print(type(cipherText))
            # print(len(cipherText))
            return cipherText
        else:
            if len(Keytext)>len(MessageText):
                NewMessage = [] 
                for i1 in range(len(Keytext)):
                    NewMessage.append(0)
                for i in range(len(MessageText)):
                    NewMessage[i]=MessageText[i]
                for i in range(len(MessageText),len(Keytext)):
                    NewMessage[i]="0"
                NewMessageText = ""
                for i in NewMessage:
                    NewMessageText=NewMessageText+i
                i = 0
                j = len(Keytext)-1
                ptr = len(Keytext)-1
                c=[]
                for i1 in range(len(Keytext)):
                    c.append(0)
                for m in range(0,len(MessageText)):
                    if Keytext[j]==1:
                        c[j]=NewMessageText[ptr]
                        ptr=ptr-1
                        j=j-1
                    else:
                        c[i]=NewMessageText[ptr]
                        ptr=ptr-1
                        i=i+1
                    
                permutationText=""
                for i1 in c:
                    permutationText=permutationText+str(i1)
                cipher = []
                for i in range(len(NewMessageText)):
                    cipher.append(0)
                for i in range(len(NewMessageText)):
                    if permutationText[i]==Keytext[i]:
                        cipher[i]=0
                    else:
                        cipher[i]=1
                cipherText = ""
                for i1 in cipher:
                    cipherText=cipherText+str(i1)
                # print(cipherText)
                # print(type(cipherText))
                # print(len(cipherText))
                return cipherText
            
            else:
                changedKey = []
                for i in range(len(MessageText)):
                    changedKey.append('0')
                for i in range(len(Keytext)):
                    changedKey[i]=Keytext[i]
                jValue = 0
                for i in range(len(Keytext),len(MessageText)):
                    changedKey[i]=Keytext[jValue]
                    jValue=jValue+1
                changedKeyTect = ""
                for i in changedKey:
                    changedKeyTect = changedKeyTect + str(i)
                newIvalue = 0
                newJvalue = len(changedKeyTect)-1
                ptr=len(changedKeyTect)-1
                c=[]
                for i in range(len(changedKeyTect)):
                    c[i]="0"
                for m in range(len(changedKeyTect)):
                    if changedKeyTect[ptr]=="1":
                        c[newJvalue]=MessageText[ptr]
                        ptr=ptr-1
                    else:
                        c[newIvalue]=MessageText[ptr]
                        ptr=ptr-1
                        newIvalue=newIvalue+1
                decrypted  = []
                for i in range(len(changedKeyTect)):
                    if c[i]==changedKeyTect[i]:
                        decrypted.append(0)
                    else:
                        decrypted.append(1)
                decryptedText = ""
                for i in decrypted:
                    decryptedText=decryptedText+str(i)
                return decryptedText
