class KB:
    def __init__(self,bytes):
        self.bytes = bytes 
        print("KB class constructor called")
    def getKB(self):
        kb = self.bytes / 1024
        return kb 
class MB(KB):
    def __init__(self, bytes):
        super().__init__(bytes)
        print("MB class constructor called")
    def getMB(self):
        #calculate MB = KB / 1024
        mb = super().getKB() / 1024
        return mb 
#leaf class
class GB(MB):
    def __init__(self, bytes):
        super().__init__(bytes)
        print("GB class constructor called")
    def getGB(self):
        #calculate GB = MB / 1024
        gb = super().getMB() / 1024
        return gb
bytes = int(input("Enter bytes "))
g1 = GB(bytes)
print("Giga bytes ",g1.getGB())
print("Mega bytes ",g1.getMB())
print("Kilo bytes ",g1.getKB())