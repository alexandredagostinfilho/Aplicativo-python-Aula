print("*" * 20)
print(" Tabelador ")
print("*" *20)

def valida_campos(valor):
     valida = valor.isdigit()
     if valida == True:
        return float(valor)      
     else:
       return False


i = True

while i == True:
        while True:    
            print("É beneficiada ou bruta")
            print("[1] Beneficiada")
            print("[2] Bruta")
            QTmadeira = (input(":"))         
            if valida_campos(QTmadeira) > 2 or valida_campos(QTmadeira) < 0 or valida_campos(QTmadeira) == False:
                print("Digite somente as opções acima")       
                continue
            else:
                break
        while True:                 
                if QTmadeira == '1':
                    print('[1] metro quadrado')
                    print('[2] metro cubico')            
                    Tmetragem = (input(":"))     
                    if(valida_campos(Tmetragem) > 2 or valida_campos(Tmetragem) < 0 or valida_campos(Tmetragem) == False): 
                        print("Digite um numero entre as opções")  
                        continue 
                    else:
                        break                      
                elif QTmadeira == '2':
                    comprimento = (input("Digite o comprimento"))
                    largura = (input("Digite a largura"))
                    expessura = (input("Digite a expessura"))
                    if valida_campos(comprimento) == False or valida_campos(largura) == False or valida_campos(expessura) == False:
                        print("Digite um numero")
                        continue
                    else:                         
                         tamanho = valida_campos(comprimento) * valida_campos(largura) * valida_campos(expessura)
                         Tmetragem = "0"
                         break
                # else:                        
                #      tamanho = valida_campos(comprimento) * valida_campos(largura) * valida_campos(expessura)                     
                #      break
                                
        while True:                           
            if Tmetragem == '1':
                    comprimento = (input("Digite o comprimento"))
                    largura = (input("Digite a largura"))
                    if valida_campos(comprimento) == False or valida_campos(largura) == False:
                        print("Digite um numero")
                        continue
                    else:
                        tamanho = valida_campos(comprimento) * valida_campos(largura)
                        # Tmetragem = '0'                          
                        break     
                                 
            elif Tmetragem == '2':
                    comprimento = (input("Digite o comprimento"))
                    largura = (input("Digite a largura"))
                    expessura = (input("Digite a expessura"))

                    if valida_campos(comprimento) == False or valida_campos(largura) == False or valida_campos(expessura) == False:
                        print("Digite um numero")
                        continue
                    else:
                        tamanho = valida_campos(comprimento) * valida_campos(largura)
                        # Tmetragem = '0' 
                        break
            else:
                 break        
        while True:                       
            print("O tamanho é igual a {}".format(tamanho))   
            if(Tmetragem == '2'):
                print("Tipo da madeira")
                print("[1] tabuas")
                print("[2] barotes")
                Tipo = (input(":")) 
                if(valida_campos(Tipo) > 2 or valida_campos(Tipo) < 0 or valida_campos(Tipo) == False):
                    print("Digite um numero entre as opções")
                    continue 
                else:
                    Tipo = "1"
                    break
            else:
                break
        while True: 
            QuantTabuas = (input("Quantidade a ser comprada: "))
            if valida_campos(QuantTabuas) == False:
                print("Digite apenas numeros")
                continue
            else:
                break
        while True:    
            print("Digite a opção que voce gostaria de comprar")
            print("[1] Pinheiro araucaria")
            print("[2] Eucalipto")
            print("[3] Pinus ilhote")
            Qopção = str(input(":"))
            if(valida_campos(Qopção) > 3 or valida_campos(Qopção) < 0 or valida_campos(Qopção) == False):
                print("Digite apenas as opções acima")
                continue
            else:
                break
        while True:
            if(Qopção == '2'):
                    print("Qual tipo de eucalipto voce gostaria")
                    print("[1] Branco")
                    print("[2] Saligna")
                    print("[3] Cerejeira")
                    print("[4] Cerno")
                    OpEucalipto = str(input(":"))
                    if valida_campos(OpEucalipto) > 4 or valida_campos(OpEucalipto) < 0  or valida_campos(OpEucalipto) == False:
                        print("[1] primeira")
                        print("[2] Segunda")
                        print("[3] terceira")
                        print("[4] Quarta")
                        print("[5] Quinta") 
                        Qqualidade = str(input("Digite a qualidade da madeira"))
                        if valida_campos(OpEucalipto) > 5 or valida_campos(OpEucalipto) < 0 or valida_campos(OpEucalipto) == False:
                            print("Digite apenas as opções acima")
                            continue
                        else:
                            break 
                    else:
                        print("[1] primeira")
                        print("[2] Segunda")
                        print("[3] terceira")
                        print("[4] Quarta")
                        print("[5] Quinta")
                        Qqualidade = str(input("Digite a qualidade da madeira"))
                        if valida_campos(Qqualidade) > 5 or valida_campos(Qqualidade) < 0 or valida_campos(Qqualidade) == False:
                            print("Digite apenas as opções acima")
                            continue
                        else:
                            break   
            else:
                print("[1] primeira")
                print("[2] Segunda")
                print("[3] terceira")
                print("[4] Quarta")
                print("[5] Quinta") 
                Qqualidade = str(input("Digite a qualidade da madeira"))
                if valida_campos(Qqualidade) > 5 or valida_campos(Qqualidade) < 0 or valida_campos(Qqualidade) == False:
                    print("Digite apenas as opções acima")
                    continue
                else:
                    break       
        
            # else:                     
            #     print("[1] primeira")
            #     print("[2] Segunda")
            #     print("[3] terceira")
            #     print("[4] Quarta")
            #     print("[5] Quinta") 
            #     Qqualidade = str(input("Digite a qualidade da madeira"))     
            #     if valida_campos(Qqualidade) > 5 or valida_campos(Qqualidade) < 0 or valida_campos(Qqualidade) == False:
            #         print("Digite apenas as opções acima")
            #         continue
            #     else:
                    # break                       
        InfTam = ""
        QTmadeira = ""
        Tmetragem2 = ""
        Qinformação = ""

        i = False 
        
        while True:    
            print("Voce digitou essas informações")         
            print("Tipo de madeira {}".format(QTmadeira)) 
            print("Tipo da metragem {}".format(Tmetragem))
            print("Tamanho {}".format(tamanho))
            print("A madeira é {}".format(Qopção))
            print("A qualidade é {}".format(Qqualidade)) 
            # print("Tipo da madeira {}".format(Tipo))
            print("A quantidade é igual a {}".format(QuantTabuas))        

            while True:            
                informacao = str(input("Voce deseja alterar alguma informação[S/N]")).upper()
                if informacao == 'S' or informacao == 'N':
                    break
                else:
                    print("Digite apenas S ou N")
                    continue
            
            if informacao == "N":
                i = False 
                j = False
                break 
                                    
            if informacao == "S":        
                print("Digite a opção que deseja mudar")
                print("[1] Tipo da madeira")                
                print("[2] A madeira")
                print("[3] A qualidade da madeira")
                print("[4] Tipo da madeira")
                print("[5] Quantidade")
                Qinformação = str(input(":"))
                if valida_campos(Qinformação) > 5 or valida_campos(Qinformação) < 0 or valida_campos(Qinformação) == False:
                    print("Digite apenas as opções acima")
                    continue
                else:
                    break
        while True:        
            if Qinformação == '1':
                print("É beneficiada ou bruta")
                print("[1] Beneficiada")
                print("[2] Bruta")                
                QTmadeira = str(input(":"))
                if(valida_campos(QTmadeira) > 3 or valida_campos(QTmadeira) < 0 or valida_campos(QTmadeira) == False):
                    print("Digite apenas as opções acima")
                    continue
                else:
                    InfTam = str(input("Voce deseja alterar a unidade de medida [S/N]")).upper()
                    if InfTam == "N":
                        Tmetragem2 = '0'
                                     
                    if InfTam == 'S' or InfTam == 'N':
                         break            
                    else:
                         print("Digite apenas S ou N")
                         continue           
                                         
            else:
                break         

        while True:    
            if InfTam == "S" and QTmadeira == "1":
                print('[1] metro quadrado')
                print('[2] metro cubico')            
                Tmetragem2 = str(input(":"))
                if valida_campos(Tmetragem2) > 3 or valida_campos(Tmetragem2) < 0 or valida_campos(Tmetragem2) == False:
                    print("Digite apenas as opções acima")
                    continue
                else:
                    break
            else:
                break   
        while True:
            if Tmetragem2 == "1":
                comprimento = str(input("Digite o comprimento"))
                largura = str(input("Digite a largura"))
                if(valida_campos(comprimento) == False or valida_campos(largura) == False):
                    print("Digite apenas numeros")
                    continue
                else:
                    Tmetragem = Tmetragem2
                    tamanho = valida_campos(comprimento) * valida_campos(largura)
                    break
            else:
                break
        
        while True:        
            if Tmetragem2 == "2":
                comprimento = str(input("Digite o comprimento"))
                largura = str(input("Digite a largura"))
                expessura = str(input("Digite a expessura"))
                if valida_campos(comprimento) == False or valida_campos(largura) == False:
                    print("Digite apenas numeros")
                    continue
                else:
                    Tmetragem = Tmetragem2
                    tamanho = valida_campos(comprimento) * valida_campos(largura) * valida_campos(expessura)   
                    break
            else:
                break
        while True:      
            if InfTam == "S" and QTmadeira == "2":         
                comprimento = str(input("Digite o comprimento"))
                largura = str(input("Digite a largura"))
                expessura = str(input("Digite a expessura"))
                if valida_campos(comprimento) or valida_campos(largura) or valida_campos(expessura):
                    print("Digite apenas numeros")
                    continue
                else:
                    tamanho = valida_campos(comprimento) * valida_campos(largura) * valida_campos(expessura)                                  
                    break
            else:
                break
        
        while True:     
            if Qinformação == "2":
                print("Digite a opção que voce gostaria de comprar")
                print("[1] Pinheiro araucaria")
                print("[2] Eucalipto")
                print("[3] Pinus ilhote")
                Qopção = (input(":"))
                if(valida_campos(Qinformação) > 3 or valida_campos(Qinformação) < 0 or valida_campos(Qinformação) == False):
                    print("Digite apenas numeros")
                    continue
                else:
                    if Qopção == "2":                            
                        print("Qual tipo de eucalipto voce gostaria")
                        print("[1] Branco")
                        print("[2] Saligna")
                        print("[3] Cerejeira")
                        print("[4] Cerno")
                        OpEucalipto = (input(":"))
                        if valida_campos(OpEucalipto) > 4 or valida_campos(OpEucalipto) < 0 or valida_campos(OpEucalipto) == False:
                            print("Digite apenas as opções acimas")
                            continue
                        else:
                            break                    
            else:
                break     
                         
            if Qopção == "2":                            
                print("Qual tipo de eucalipto voce gostaria")
                print("[1] Branco")
                print("[2] Saligna")
                print("[3] Cerejeira")
                print("[4] Cerno")
                OpEucalipto = (input(":"))
                if valida_campos(OpEucalipto) > 4 or valida_campos(OpEucalipto) < 0 or valida_campos(OpEucalipto) == False:
                    print("Digite apenas as opções acimas")
                    continue
                else:
                    break
            else:
                break
              
        while True:
                if Qinformação == "4":
                    print("Tipo da madeira")
                    print("[1] tabuas")
                    print("[2] barotes")
                    Tipo = (input(":"))
                    if valida_campos(Tipo) > 2 or valida_campos(Tipo) < 0 or valida_campos(Tipo) == False:
                        print("Digite apenas as opções acima")
                        continue
                    else:
                        break
                else:
                    break
        while True:
                if Qinformação == '5':           
                    QuantTabuas = (input("Quantidade a ser comprada: "))
                    if valida_campos(QuantTabuas) == False:
                        print("Digite apenas numeros")
                        continue
                    else:
                        break  
                else: 
                    break


        while True:
                if Qinformação == '3':
                    print("[1] primeira")
                    print("[2] Segunda")
                    print("[3] terceira")
                    print("[4] Quarta")
                    print("[5] Quinta") 
                    Qqualidade = str(input("Digite a qualidade da madeira"))
                    if valida_campos(Qqualidade) > 5 or valida_campos(Qqualidade) < 0 or valida_campos(Qqualidade) == False:
                        print("Digite apenas as opções acima")
                        continue
                    else:
                        break  
                else:
                    break      
        i = False
                              
        while True:           
            if Tmetragem == '1':
                ValorMetragem = (input("Valor ao m²: "))
                if valida_campos(ValorMetragem) == False:
                    print("Digite apenas numeros") 
                else:
                    break
            elif Tmetragem == '2' or QTmadeira == '2':
                ValorMetragem = (input("Valor em m³: "))
                if valida_campos(ValorMetragem) == False:
                    print("Digite apenas numeros") 
                else:
                    break
            else:
                break
                

preco =  valida_campos(QuantTabuas) * tamanho
preco = preco * valida_campos(ValorMetragem)
print("O preço ficara igual a {:.2f}".format(preco))             
             
                   


        



