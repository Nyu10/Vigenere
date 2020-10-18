#! /bin/bash

#I left the answers to the discussion post and homework in Decoder.py
#make run ARGS="encode plaintext key"    
#make run ARGS="decode ciphertext key"  
# Examples : make run ARGS="encode HOTDOGSTAND BOAR"
#			make run ARGS="decode ICTUPUSKBBD BOAR"
Help:
$(info ARGS should be encode/decode, the text, the key)


run:
	py Decoder.py $(ARGS)


