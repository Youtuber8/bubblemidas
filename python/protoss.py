#se abre y hace una pregunta. pregunta cualquier nombre en ingles.despues el programa hace otra pregunta
#pregunta cuantas letras hay en tu nombre. despues el programa pcomprueba si el numero 
#has dado es correcto o no. si el numero es correcto el programa dice "felicidades has acertado"
#si no es correcto y el numero es mayor te dice "incorrecto has intoducido x letras de mas"
#y si es menor te dice "incorrecto has introducido x letras de menos"

def answer(name,what):
    correct = len(name)
    print(correct)
    print(type(what))
    if what == correct:
        print("congratulations! you are correct.")
    

name = input("What is your name in English? ")
amount = int(input("How many letters does your name have? "))
answer(name,amount)









