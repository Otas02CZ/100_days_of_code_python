# this is a simple programm demonstrating caesar cipher

from rich.prompt import IntPrompt, Prompt
from os import system
from art import logo

print(logo)
print("Welcome to the extended Caesar cipher Encryption/Decryption tool.")
input("Press Enter to continue: ")

alphabet : str = "V(0–IA'éĚlžP]Jď9v$mQ3RT4YÝa.[Č)×}7eá/ňNÍ pšdč,ÁŇh:tě¨zO{H÷jsýÉKBrZk\\u¸*yíŠgLĎwnqfCúxÚ-břGŮßU?WSŘD56;ů!18>E+2cioX<ŽMF"

def caesar(message : str, shift_key : int, operation : str) -> str:
    shifted_alphabet : str = ""
    for index in range(len(alphabet)):
        match operation:
            case "encode":
                shift_index : int = index + shift_key
                while shift_index >= len(alphabet):
                    shift_index -= len(alphabet)
                shifted_alphabet += alphabet[shift_index]
            case "decode":
                shift_index : int = index - shift_key
                while shift_index < 0:
                    shift_index += len(alphabet)
                shifted_alphabet += alphabet[shift_index]
    return "".join([shifted_alphabet[alphabet.find(char)] for char in message])

while 1:
    system("cls")
    operation : str = Prompt.ask("Do you wanna encode or decode?", choices=["encode", "decode"])
    message : str = Prompt.ask("Tell me the message (I won't tell anyone)")
    shift_key : int = 0
    while shift_key<=0:
        shift_key = IntPrompt.ask("Tell me the shift key")
    match operation:
        case "encode" : print(f"Your encoded message is:\n-\n{caesar(message, shift_key, operation)}\n-")
        case "decode" : print(f"Your decoded message is:\n-\n{caesar(message, shift_key, operation)}\n-")
    should_continue : str = Prompt.ask("Do you want to encode/decode another message?", choices=["yes", "no"])
    if should_continue == "no":
        print("Thank you for using our little programm. Bye Bye. :)")
        break
    