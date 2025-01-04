import hashlib

def sha512Hash(data: str) -> str:
    encoded_data = data.encode('utf-8')
    hash_object = hashlib.sha512(encoded_data)
    hex_digest = hash_object.hexdigest()
    return hex_digest

def writInFile(data : str):
    #TODO

def cryptFile(salt : str):
    #TODO
    
def decryptFile(Key : str):
    #TODO

if __name__ == "__main__":
    texte = input("Entrez le txt : ")
    print("Texte à hasher :", texte)
    print("SHA-512       :", sha512Hash(texte))