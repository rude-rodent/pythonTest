import variables
import descriptions

while True:
    choice = input("What would you like to name your pet?\n")
    variables.petName = choice.title()
    choice = input("Would you like to give {} a head scratch?\n".format(variables.petName))
    if choice == "yes":
        print(descriptions.responses[0])
        break
    else:
        print(descriptions.responses[1])
        break
