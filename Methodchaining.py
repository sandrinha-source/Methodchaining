ovos=int(input("Há ovos? Se sim, digite 1, senão, digite 2: "))
if ovos == 1:
    bouv=int(input("Digite 1 se os ovos forem brancos ou 2 se forem vermelhos: "))
    if bouv == 1:
        print("Estou levando 6 ovos.")
    else:
        print("Estou levando 12 ovos.")
elif ovos == 2:
    leite=int(input("Há leite? Digite 1 p/ sim ou 2 p/ñ: "))
    if leite == 1:
        doui=int(input("Digite 1 p/ leite desnatado ou 2 p/ leite integral: "))
        if doui == 1:
            print("Estou levando um leite desnatado.")
        else:
            print("Estou levando um leite integral.")
    else:
        refrigerante=int(input("Há refrigerante? Digite 1 p/ sim ou 2 p/ñ: "))
        if refrigerante == 1:
            tipo=int(input("Digite 1 para Guaraná, 2 para Coca-Cola ou 3 para Fanta: "))
            if tipo == 1:
                print("Estou levando 1 Guaraná.")
            elif tipo == 2:
                print("Estou levando 1 Coca-Cola.")
            else:
                print("Estou levando 1 Fanta.")
        else:
            print("Não levei nada")
