about = "I study Python at college and I like chess"
words = about.split()

print(len(words))                       
print(max(words, key=len))             
print(" ".join(words[::-1]))             

print(about.lower().count("a"))         

print(about.title())                    
print(about.replace(" ", "_"))           


def is_palindrome(text):
    t = text.lower().replace(" ", "")
    return t == t[::-1]

print(is_palindrome("Petrenko Ivan Olehovych"))   
print(is_palindrome("Never odd or even"))        

day = 14
alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar(text, shift):
    result = ""
    for ch in text:
        if ch.lower() in alphabet:
            pos = (alphabet.index(ch.lower()) + shift) % 26  
            new = alphabet[pos]
            result += new.upper() if ch.isupper() else new   
        else:
            result += ch                                     
    return result

encrypted = caesar("Petrenko Ivan Olehovych", day)
print(encrypted)
print(caesar(encrypted, -day))         