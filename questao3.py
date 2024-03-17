def complete_sequencia (escolha):
    #sequecia de aumento de 2 em 2 
    if escolha == "a":
        return[1, 3, 5, 7, 9]
    #sequencia de muplicação por 2 do ultimo numero da lista
    elif escolha == "b":
        return[2, 4, 8, 16, 32, 64, 128]
    #sequencia de numeros naturais ao quadrado
    elif escolha == "c":
        return[0, 1, 4, 9, 16, 25, 36, 49]
    #sequencia de quadrado do indice mutiplicado por 4 
    elif escolha == "d":
        return[4, 16, 36, 64, 100]
    #sequncia fibonnaci que é a soma dos dois numero anteriores
    elif escolha == "e":
        fibonacci = [1, 1]
        while len (fibonacci) < 7:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci
    # a sequencia desse para mim não ficou muito clara a logica. mas acredito que seja, adição dos numeros, 8,2,4,1,1,1 e apos repete 
    elif escolha == "f" :
        return[2, 10, 12, 16, 17, 18, 19, 27]
    else:
        return "Sequência não reconhecido"
    
sequecias = input("Escolha uma sequencia (a , b , c , d , e, f): ").strip().lower()
print(complete_sequencia(sequecias))