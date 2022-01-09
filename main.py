alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import os
import platform
from colorama import Fore,Back,Style
import colorama

colorama.init()


logo = Fore.GREEN+'''\n\n8888888b.                                 888                      d88P                                              888          
888  "Y88b                                888                     d88P                                               888          
888    888                                888                    d88P                                                888          
888    888  .d88b.   .d8888b .d88b.   .d88888  .d88b.           d88P          .d88b.  88888b.   .d8888b .d88b.   .d88888  .d88b.  
888    888 d8P  Y8b d88P"   d88""88b d88" 888 d8P  Y8b         d88P          d8P  Y8b 888 "88b d88P"   d88""88b d88" 888 d8P  Y8b 
888    888 88888888 888     888  888 888  888 88888888        d88P           88888888 888  888 888     888  888 888  888 88888888 
888  .d88P Y8b.     Y88b.   Y88..88P Y88b 888 Y8b.           d88P            Y8b.     888  888 Y88b.   Y88..88P Y88b 888 Y8b.     
8888888P"   "Y8888   "Y8888P "Y88P"   "Y88888  "Y8888       d88P              "Y8888  888  888  "Y8888P "Y88P"   "Y88888  "Y8888  
                                                                                                                                  

                                                  MADE BY Erupted_Lava                                                                     
                                                                                                                                  

'''+Fore.RESET

def encrypt(text,shift):
    text_list = list(text)

    for i in range(len(text_list)):

        if text_list[i] in alphabet:

            position = alphabet.index(text_list[i])+shift
            
            if position > len(alphabet)-shift:
                text_list[i] = alphabet[position-len(alphabet)]

            else:
                text_list[i] = alphabet[position]
        else:
            pass


    final = ''.join(text_list)
    print(f"\n The encoded text is : {Fore.GREEN+final+Fore.RESET}")


def decrypt(text,shift):
    text_list = list(text)


    for i in range(len(text_list)):

        if text_list[i] in alphabet:

            position = alphabet.index(text_list[i])-shift

            if position < 0:
                text_list[i] = alphabet[position+len(alphabet)]

            else:
                text_list[i] = alphabet[position]
        else:
            pass

    final = ''.join(text_list)
    print(f"\n The decoded text is : {Fore.BLUE+final+Fore.RESET}")


if __name__ == '__main__':

    should_continue = True
    while should_continue:
        if platform.system() == "Linux":
            os.system('clear')
        else:
            os.system('cls')
        print(logo)
        direction = input(Fore.LIGHTBLUE_EX+" Type 'encode' to encrypt, type 'decode' to decrypt:\n "+Fore.RESET)
        text = input(Fore.GREEN+" Type your message:\n "+Fore.RESET).lower()
        shift = int(input(Fore.GREEN+"\n Type the shift number:\n "+Fore.RESET))
        shift = shift % 26

        if direction == 'decode':
            decrypt(text,shift)
        elif direction == 'encode':
            encrypt(text,shift)

        choice = input("\n\n Type 'yes' if you want to go again. Otherwise, type 'no'  >> ")
        if choice =="no":
            print(" GoodByee")
            break
            
