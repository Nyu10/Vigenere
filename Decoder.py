#!/usr/bin/python

#python Main.py Example.txt
#Example.txt should be a ciphertext 
import sys
import math

if (sys.argv[1]=="encode"):
   boolean=True
else:
   boolean=False
text = sys.argv[2]
key = sys.argv[3]
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def vigenere(text,key,boolean):
   expanded_key = key*(math.floor(len(text)/len(key))+1)
   answer=""
   #True == Decrypt Message
   if (boolean==True):
      for x in range(len(text)):
         #the 0-25 representation of the current letter of the text
         int_text = alphabet.index(text[x])
         #the 0-25 representation of the current letter of the key
         int_key = alphabet.index(expanded_key[x])
         #Encrypted letter index
         index = (int_text+int_key)%26
         answer+=alphabet[index]
   #False == Decrypt Message
   elif (boolean==False):
      for x in range(len(text)):
         #the 0-25 representation of the current letter of the text
         int_text = alphabet.index(text[x])
         #the 0-25 representation of the current letter of the key
         int_key = alphabet.index(expanded_key[x])
         #Decrypted letter index
         index = (int_text-int_key)%26
         answer+=alphabet[index]
   return answer

print(vigenere(text,key,boolean))
