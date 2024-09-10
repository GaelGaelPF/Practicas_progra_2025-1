#Práctica 1
#Integrantes:
#Héctor Vazquez Terreros
#Vanessa Valdez Vazquez
#Gael Peña Fonseca
print("******************")
print("* Bienvenido al programa que traduce operaciones * \n*    aritmeticas a notación polaca inversa       *")
print("******************")

print("Asegurese de que el numero de parentesis izquierdos coincida con los derechos\nademás cada caracter debe de estar separado por un espacio a excepcion del operador: **")
print("Ejemplo: 12 * ( 312 * 23 ) ** 4 + 2")
def polaca_inversa(expresion):#defiinimos nuestra nuestra funcion polaca inversa
  operadores = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
  pila = []
  salida = []
  indice = 0

  while indice < len(expresion):#mientras el indice sea menor a la longitud de la expresion lea la expresion
      caracter = expresion[indice] #declaramos la variable caracter como el indice de la expresion

      if caracter.isnumeric(): #si es caracter es un numero
        num = caracter
        while indice + 1 < len(expresion) and expresion[indice + 1].isnumeric(): #ciclo while para que lea si los caracteres a continuacion son numeros
              indice += 1
              num += expresion[indice] #agrega el siguiente numero a la variable num
        salida.append(num) #apila los numero en salida

      elif caracter == '(': #si el caracter es un parentesis izquierdo lo apila en la pila
          pila.append(caracter)

      elif caracter == ')': #En otro caso, si el caracter es un parentesis derecho
          while pila and pila[-1] != '(':
            #Retire los operadores de la pila para agregarlos a la cadena final.
              salida.append(pila.pop()) #Retire el paréntesis izquierdo de la pila.
          pila.pop()

      elif caracter in operadores: #En otro caso si el caracter esta en los operadores
          if caracter == '*' and indice + 1 < len(expresion) and expresion[indice + 1] == '*':
              caracter += '*' #Guarda el operador en la variable caracter
              indice += 1 #Lee el siguiente elemento
          while (pila and pila[-1] != '(' and operadores.get(pila[-1], 0) >= operadores[caracter]): #mientras pila y el ultimo caracter de la pila sean distintos a "("
              salida.append(pila.pop())
          pila.append(caracter)#agrega a la pila
      indice += 1 #lee el siuiente elemento

  while pila:
      salida.append(pila.pop())

  return salida


def main(): #definimos nuestro main aplicando la definicion anterior de polaca inversa
    print("Introduzca su operación aritmética con valores enteros:" )
    x = input()
    expresion = x #colocamos la expresion deseada a conocer en polaca inversa
    resultado = polaca_inversa(expresion) #apliacmos la formula
    print("La expresión en notación polaca inversa es: ")
    for c in resultado:
        print(c, end = " ")

if __name__ == "__main__":
    main()
print()
print("Fin.")
