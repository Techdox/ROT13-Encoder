
import codecs

def rotCHange():
    rinput = input("Enter in your phrase to convert.")
    enc = codecs.getencoder("rot-13")
    rot = enc(rinput)[0]
    print(rot)

if __name__ == "__main__":
    rotCHange()    