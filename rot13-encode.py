import codecs
     
def rotEncode(rotInput):  
    rot = codecs.encode(rotInput, "rot-13")
    print(rot)

def rotDecode(rotInput):
    unrot = codecs.decode(rotInput, "rot-13")
    print(unrot)

if __name__ == "__main__":
    while True:
        choiceEncode = input("[E]ncode or [D]ecode: ").strip()
        rinput = input("Enter in your phrase to convert: ")
        if choiceEncode == "e":
            rotEncode(rinput)
        elif choiceEncode == "d":
            rotDecode(rinput)
        else:
            print("Error! You did not make a correct choice: ")
            exit
        