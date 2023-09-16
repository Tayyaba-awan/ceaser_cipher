import art
print(art.logo)
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
should_continue=True
while should_continue:
    direction=input("type 'encode' to encrpyt and 'decode' to decpyt:\n") 
    text=input("type your msg\n")
    shift=int(input("type the shift number\n"))
    shift=shift%26
    def caeser(plain_text,shift_amount,cipher_direction):
        cipher_text=""
        if cipher_direction=="decode": 
            shift_amount*=-1
        for char in plain_text: 
            if char in alphabet:   
                position=alphabet.index(char)
                new_position=position+shift_amount  
                cipher_text+=alphabet[new_position]
            else:
                cipher_text+=char 
        print(f"The {direction}d text is {cipher_text}")


    caeser(plain_text=text,shift_amount=shift,cipher_direction=direction)
    restart_cipher=input("if you want to restart again type 'yes' otherwise type 'no'")
    if restart_cipher=="no":
          should_continue=False
          print("goodbye") 