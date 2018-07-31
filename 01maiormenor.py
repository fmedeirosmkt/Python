# -*- coding: utf-8 -*-
maior=0
menor=0
numero=0
cont=0

while cont<10:
	numero=int(input())
	cont+=1
	if numero>maior:
		maior=numero
	if cont==1:
		menor=numero
	if numero<menor:
		menor=numero

print(maior)
print(menor)
