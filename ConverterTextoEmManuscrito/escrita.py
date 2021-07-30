#_*_ coding: utf-8 _*_

import pywhatkit as kit 

arq = open("arquivo.txt","r")
texto = arq.read()
arq.close()

print(texto)

kit.text_to_handwriting(texto,save_to="convertido.png",rgb =(0,0,0))
