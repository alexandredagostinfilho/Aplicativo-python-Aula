print("*" * 20)
print(" Tabelador ")
print("*" *20)

i = True
while i == True:
    print("É beneficiada ou bruta")
    print("[1] Beneficiada")
    print("[2] Bruta")
    QTmadeira = int(input(":"))
    if(QTmadeira == 1):
        print('[1] metro quadrado')
        print('[2] metro cubico')            
        Tmetragem = int(input(":"))
    elif QTmadeira == 2:
        comprimento = float(input("Digite o comprimento"))
        largura = float(input("Digite a largura"))
        expessura = float(input("Digite a expessura"))
        tamanho = comprimento * largura * expessura
        Tmetragem = 0
    if Tmetragem == 1:
        comprimento = float(input("Digite o comprimento"))
        largura = float(input("Digite a largura"))
        tamanho = comprimento * largura
    elif Tmetragem == 2:
        comprimento = float(input("Digite o comprimento"))
        largura = float(input("Digite a largura"))
        expessura = float(input("Digite a expessura"))
        tamanho = comprimento * largura * expessura   
    print("O tamanho é igual a {}".format(tamanho))   
    print("Tipo da madeira")
    print("[1] tabuas")
    print("[2] barotes")
    Tipo = int(input(":"))
    QuantTabuas = float(input("Quantidade a ser comprada: "))
    print("Digite a opção que voce gostaria de comprar")
    print("[1] Pinheiro araucaria")
    print("[2] Eucalipto")
    print("[3] Pinus ilhote")
    Qopção = int(input(":"))
    if(Qopção == 2):
        print("Qual tipo de eucalipto voce gostaria")
        print("[1] Branco")
        print("[2] Saligna")
        print("[3] Cerejeira")
        print("[4] Cerno")
        OpEucalipto = int(input(":"))
        print("[1] primeira")
        print("[2] Segunda")
        print("[3] terceira")
        print("[4] Quarta")
        print("[5] Quinta") 
        Qqualidade = int(input("Digite a qualidade da madeira")) 
    else:     
        print("[1] primeira")
        print("[2] Segunda")
        print("[3] terceira")
        print("[4] Quarta")
        print("[5] Quinta") 
        Qqualidade = int(input("Digite a qualidade da madeira"))     
    
        
    print("Voce digitou essas informações")     
    
    while True:         
        print("Tipo de madeira {}".format(QTmadeira)) 
        print("Tipo da metragem {}".format(Tmetragem))
        print("Tamanho {}".format(tamanho))
        print("A madeira é {}".format(Qopção))
        print("A qualidade é {}".format(Qqualidade)) 
        print("Tipo da madeira {}".format(Tipo))
        print("A quantidade é igual a {}".format(QuantTabuas))        
       
        informacao = str(input("Voce deseja alterar alguma informação[S/N]")).upper()             
        if informacao == "N":
            i = False
            break   
        if informacao == "S":        
            print("Digite a opção que deseja mudar")
            print("[1] Tipo da madeira")                
            print("[2] A madeira")
            print("[3] A qualidade da madeira")
            print("[4] Tipo da madeira")
            print("[5] Quantidade")
            Qinformação = int(input(":"))
            if Qinformação == 1:
                print("É beneficiada ou bruta")
                print("[1] Beneficiada")
                print("[2] Bruta")                
                QTmadeira = int(input(":"))                
                InfTam = str(input("Voce deseja alterar a unidade de medida [S/N]")).upper()
                if InfTam == "S" and QTmadeira == 1:
                    print('[1] metro quadrado')
                    print('[2] metro cubico')            
                    Tmetragem = int(input(":"))     
                    if Tmetragem == 1:
                        comprimento = float(input("Digite o comprimento"))
                        largura = float(input("Digite a largura"))
                        tamanho = comprimento * largura
                    elif Tmetragem == 2:
                        comprimento = float(input("Digite o comprimento"))
                        largura = float(input("Digite a largura"))
                        expessura = float(input("Digite a expessura"))
                        tamanho = comprimento * largura * expessura   
                elif InfTam == "S" and QTmadeira == 2:         
                     comprimento = float(input("Digite o comprimento"))
                     largura = float(input("Digite a largura"))
                     expessura = float(input("Digite a expessura"))
                     tamanho = comprimento * largura * expessura                                   
            elif Qinformação == 2:
                print("Digite a opção que voce gostaria de comprar")
                print("[1] Pinheiro araucaria")
                print("[2] Eucalipto")
                print("[3] Pinus ilhote")
                Qopção = int(input(":"))
                if(Qopção == 2):
                    print("Qual tipo de eucalipto voce gostaria")
                    print("[1] Branco")
                    print("[2] Saligna")
                    print("[3] Cerejeira")
                    print("[4] Cerno")
                    OpEucalipto = int(input(":"))
            if Qinformação == 3:
                print("[1] primeira")
                print("[2] Segunda")
                print("[3] terceira")
                print("[4] Quarta")
                print("[5] Quinta") 
                Qqualidade = int(input("Digite a nova qualidade da madeira"))        
            if Qinformação == 4:
                print("Tipo da madeira")
                print("[1] tabuas")
                print("[2] barotes")
                Tipo = int(input(":"))
            if Qinformação == 5:
                QuantTabuas = float(input("Quantidade a ser comprada: "))   
                                                    
preco =  QuantTabuas * tamanho 
print("O preço ficara igual a {:.2f}".format(preco))             
             
                   


          
         






