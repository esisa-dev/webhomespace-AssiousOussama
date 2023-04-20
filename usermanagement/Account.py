import subprocess
import os

from Authentication import Authentication
class Account : 
    
    def __init__(self) -> None:
        pass
    #Ajouter un utilisateur
    def adduser(self,username,password) -> bool:
        if username in os.listdir("/home"):
            return False
        try :
            cmd = f"sudo adduser {username} --gecos '' --disabled-password"
            subprocess.run(cmd.split(), check=True)
            cmd = f"echo '{username}:{password}' | sudo chpasswd"
            subprocess.run(cmd, shell=True, check=True)
        except :
            return False
        return True
    
    #Supprimer un utilisateur
    def deleteuser(self,username,password) -> bool:
        test = Authentication(username,password)
        try :
            if test.authenti() == False :
                return False
            command = f"sudo deluser {username}"
            os.system(command)
        except :
            return False
        return True
    
    #Changer le mot de passe d'un utilisateur   
    def changePasswprd(self,username,password,new_password)  -> bool:
        test = Authentication(username,password)
        if test.authenti() == False :
            return False
        try :
            command = f"echo '{username}:{new_password}' | sudo chpasswd"
            os.system(command)
        except : 
            return False
        return True
    
if __name__ == "__main__":
    a =  Account()
    # a.changePasswprd("asss","azertyu")
    # print(a.adduser("as","azerty"))
    #print(a.deleteuser("as","sdsdsd"))

 