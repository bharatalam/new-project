text1 = input("Enter the text:\n").lower()
shift_num = int(input("enter the shift code for feature1:\n"))
index1=0
index2=0

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' ,'v', 'w', 'x', 'y', 'z']

fnc = input("type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
def encrypt_text(text1):
    enc_word=""
    for x in text1:
        index1=alphabets.index(x)
        if index1+shift_num > 25:
            index2=index1+shift_num - 26
        else:   
            index2=index1 + shift_num
        enc_word = enc_word+alphabets[index2]  
    return(enc_word)

new_word=encrypt_text(text1)
print(new_word)

fnc = input("type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
def decrypt_text(new_word):
    enc_word=""
    for x in new_word:
        index1=alphabets.index(x)
        if index1+shift_num < 1:
            index2=index1-shift_num
        else:   
            index2=index1 - shift_num
        enc_word = enc_word+alphabets[index2]  
    print(enc_word)
decrypt_text(new_word)
    
    
    
     
