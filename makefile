#! /bin/bash

#make run ARGS="encode plaintext key"    
#make run ARGS="decode ciphertext key"  
Help:
$(info ARGS should be encode/decode, the text, the key)


run:
	py Decoder.py $(ARGS)


