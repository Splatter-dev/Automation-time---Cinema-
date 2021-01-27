import modules.colours as colour


def option_selected(option=""):
    while True:
        try:
            option_input = int(input(colour.purple("Digite uma opção: ")))
        except(ValueError, TypeError):
            print (colour.red("Digite um valor correto!"))
            break
        if option_input not in(1,2,3,4):
            print(colour.red("Selecione uma opção valida!"))
            break
        return option_input