''' This program allows user to input any word(secret sentence) but then the trick is that you've probably been told 
how many times to shift the word and using functions like ord() and chr() you'll get different messages/ secret sentences or codes 
{Beware of cse as it is case-sensitive}'''
Enter_encrypted_word_or_code = input("Enter the Encrypted word or code : ")
Number_of_shifts = int(input("How many shifts do you want the code to make ? "))
for i in range (len(Enter_encrypted_word_or_code)):
    unicode_version = ord(Enter_encrypted_word_or_code[i])
    unicode_final = unicode_version + Number_of_shifts
    i+=1
Decoded_version = chr(unicode_final)
print(f"Your secret code is {Decoded_version}")