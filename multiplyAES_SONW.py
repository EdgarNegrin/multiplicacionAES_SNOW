#
# Autor: Edgar Negrin Gonzalez
# Email: alu0101210964@ull.edu.es
# Practica 5: Multiplicacion en SNOW 3G y AES
#
# Ejecucion: py multiplyAES_Snow.py
#   
#   Ejemplo:
# Primer byte: 57
# Segundo byte: 83
# Algoritmo(AES|SNOW): AES
#
# Primer byte: 01010111
# Seegundo byte: 10000011
# Byte Algoritmo: 00011011
# Multiplicacion: 11000001
#
import sys

## Bytes para XOR
AES = '00011011'
AES = AES[::-1]

SNOW = '10101001'
SNOW = SNOW[::-1]

## Operacion XOR
def xor(x, y):
  ans = ''
  for i in range(8):
    if (x[i] == y[i]):
      ans += '0'
    else:
      ans += '1'
  return ans

## Rotacion de byte
def rot(x):
  return '0' + x[:7]

## Multiplicacion de dos bytes dependiendo del byte A9 o 1B
def multiply(byte1, byte2, algorith):

  results = []

  if (byte2[0] == '1'):
    results.append(byte1)
  
  if (byte2[1] == '1'):
    results.append(rot(byte1))

  for i in range(6):
    if (byte2[i + 2] == '1'):
      results.append(sub_multiply(byte1, i + 2, algorith))
      byte2 = byte2[:(i + 1)] + '0' + byte2[(i + 2):]

  result = '00000000'
  for i in range(len(results)):
    result = xor(result, results[i])
  return result

## Suboperacion para la multiplicacion
def sub_multiply(byte1, j, algorith):
  sol = byte1
  for i in range (j):
    if (sol[7] == '1'):
      sol = rot(sol)
      if (algorith == 'AES'):
        sol = xor(sol, AES)
      else:
        sol = xor(sol, SNOW)
    else:
      sol = rot(sol)
  return sol

## ENTRADA
byte1 = bin(int(input("Primer byte: "), 16))[2:].zfill(8)
byte2 = bin(int(input("Segundo byte: "), 16))[2:].zfill(8)
algorith = input("Algoritmo(AES|SNOW): ")

if (algorith != "AES" and algorith != "SNOW"):
  print("Argumento no valido")
  sys.exit(-1)

byte1 = byte1[::-1]
byte2 = byte2[::-1]

## SALIDA
print()
print("Primer byte: " + byte1[::-1])
print("Segundo byte: " + byte2[::-1])
if (algorith == "AES"):
  print("Byte Algoritmo: " + AES[::-1])
else:
  print("Byte Algoritmo: " + SNOW[::-1])
print("Multiplicacion: " + multiply(byte1, byte2, algorith)[::-1])

sys.exit(0)
