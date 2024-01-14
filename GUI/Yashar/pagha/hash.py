import hashlib

def getPassHash(self, password):
        return hashlib.md5(bytes(password, "ascii")).hexdigest()
        