from hex_dec import HexDecimal


class Inverse_Per_XOR:
    
    def __init__(self):
        self.key="O"
    
    def Encryption(self,message):
        
        self.message=message
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
            for i1 in range(len(MessageText)):
                if Keytext[i1]==MessageText[i1]:
                    c[i1]=0
                else:
                    c[i1]=1
            Newc=[]
            for i1 in range(len(MessageText)):
                Newc.append(0)
            for m in range(len(MessageText)):
                if Keytext[ptr]==1:
                    Newc[ptr]=c[j] 
                    ptr=ptr-1
                j=j-1
                if Keytext[ptr]!=1:
                    Newc[ptr]=c[i]
                    ptr=ptr-1
                i=i+1 
            permutationText=""
            for i1 in Newc:
                permutationText=permutationText+str(i1)
            return permutationText
        
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
                c=[]
                for i1 in range(len(Keytext)):
                    c.append(0)
                for i1 in range(len(Keytext)):
                    if Keytext[i1]==NewMessageText[i1]:
                        c[i1]=0
                    else:
                        c[i1]=1
                i = 0
                j = len(Keytext)-1
                ptr = len(Keytext)-1
                c=[]
                for i1 in range(len(Keytext)):
                    c.append(0)
                Newc=[]
                for i1 in range(len(NewMessageText)):
                    Newc.append(0)
                for m in range(len(NewMessageText)):
                    if Keytext[ptr]==1:
                        Newc[ptr]=c[j] 
                        ptr=ptr-1
                    j=j-1
                    if Keytext[ptr]!=1:
                        Newc[ptr]=c[i]
                        ptr=ptr-1
                    i=i+1 
                permutationText=""
                for i1 in Newc:
                    permutationText=permutationText+str(i1)
                return permutationText
            
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
                
                c=[]
                for i1 in range(len(changedKeyTect)):
                    c.append(0)
                for i1 in range(len(changedKeyTect)):
                    if Keytext[i1]==MessageText[i1]:
                        c[i1]=0
                    else:
                        c[i1]=1
                i = 0
                j = len(Keytext)-1
                ptr = len(Keytext)-1
                c=[]
                for i1 in range(len(changedKeyTect)):
                    c.append(0)
                Newc=[]
                for i1 in range(len(changedKeyTect)):
                    Newc.append(0)
                for m in range(len(changedKeyTect)):
                    if Keytext[ptr]==1:
                        Newc[ptr]=c[j] 
                        ptr=ptr-1
                    j=j-1
                    if Keytext[ptr]!=1:
                        Newc[ptr]=c[i]
                        ptr=ptr-1
                    i=i+1 
                permutationText=""
                for i1 in Newc:
                    permutationText=permutationText+str(i1)
                return permutationText
                
        
