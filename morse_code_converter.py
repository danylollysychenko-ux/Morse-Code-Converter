import sys
morse_code = {"A": ".-",
              "B": "-...",
              "C": "-.-.",
              "D": "-..",
              "E": ".",
              "F": "..-.",
              "G": "--.",
              "H": "....",
              "I": "..",
              "J": ".---",
              "K": "-.-",
              "L": ".-..",
              "M": "--",
              "N": "-.",
              "O": "---",
              "P": ".--.",
              "Q": "--.-",
              "R": ".-.",
              "S": "...",
              "T": "-",
              "U": "..-",
              "V": "...-",
              "W": ".--",
              "X": "-..-",
              "Y": "-.--",
              "Z": "--..",
              "1": ".----",
              "2": "..---",
              "3": "...--",
              "4": "....-",
              "5": ".....",
              "6": "-....",
              "7": "--...",
              "8": "---..",
              "9": "----.",
              "0": "-----",
              " ": ""}

def encode(enter, messages, morse_code):
    "Encodes the message in morse code"
    if enter == "encode":
            message = input("What message do you want to encode?: ").upper()
            for char in message:
                if char in morse_code:
                    messages.append(morse_code[char])
                elif char not in morse_code:
                    print(f"[Warning] Character \"{char}\" not recongnized.Skipped.")

            for k in messages:
                print(k, end = " ")
            print()

def decode(enter, messages, morse_code):
    """Decodes the encrypted message"""
    if enter == "decode":
            message = input("What do you want to decode?: ").upper()
            message = message.split(" ")

            for char in message:
                found = False
                for key, value in morse_code.items():
                    if value == char:
                        messages.append(key)
                        found = True
                        break
                
                if not found:
                    print(f"[Warning] Sequence \"{char}\" not recongnized.Skipped.")
            
            for j in messages:
                print(j, end="")
            print()

def exceptional_conditions(enter):
    """This handles valid input and also quits the program."""
    if enter == 'q':
        print("Thank you for using my program.")
        sys.exit()
    
    elif enter != "encode" and enter != "decode" and enter != "q":
        print("Invalid input.")

def main():
    while True:
        enter = input("Do you want to (encode or decode) or (q to quit)?: ").strip()
        messages = []

        encode(enter, messages, morse_code)
        decode(enter, messages, morse_code)
        
        exceptional_conditions(enter)

if __name__ == "__main__":
    main()
