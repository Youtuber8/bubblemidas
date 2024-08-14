#se abre y hace una pregunta. pregunta cualquier nombre en ingles.despues el programa hace otra pregunta
#pregunta cuantas letras hay en tu nombre. despues el programa pcomprueba si el numero 
#has dado es correcto o no. si el numero es correcto el programa dice "felicidades has acertado"
#si no es correcto y el numero es mayor te dice "incorrecto has intoducido x letras de mas"
#y si es menor te dice "incorrecto has introducido x letras de menos"

# At the start we define the function and its parameters. The parameter name recieves info-
#mation about the name that the user puts. The parameter what recieves the answers  to
# the question about how many letters does your name have.

def answer(name,what):

#then I create a new variable called correct, which calculates information about how many
# letters are in your name.
    correct = len(name)
    # After that the program calculates if the answer is correct. If it is correct, then
    # it prints 'congratulations! you are correct'
    # If it is somehow not correct, it puts a message stating that you are unfortunately 
    # not correct
    
    if what == correct:
        print("congratulations! you are correct.")
    else : print('sorry, you are not correct.')

name = input("What is your name in English? ")
print('WARNING only put numbers from now on')
amount = int(input("How many letters does your name have? "))
answer(name,amount)









