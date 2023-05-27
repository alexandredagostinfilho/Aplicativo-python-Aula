import pickle
import json
print("*" * 20)
print(" Tabelador ")
print("*" *20)
from pathlib import Path


def valida_campos(valor):
     valida = valor.isdigit()
     tipo = isinstance(valor, float)     
     if valida == True or tipo == False:
        return float(valor)
    
                   
     else:
       return False


i = True

while i == True:    
        while True:
            nomeCliente = str(input("Digite o nome do cliente"))
                      
            print("\033[36m===\033[m" * 20)    
            print("\033[32mÉ beneficiada ou bruta\033[m")
            print("\033[33m[1] Beneficiada\033[m")
            print("\033[33m[2] Bruta\033[m")
            QTmadeira = (input("\033[36m:\033[m"))
            if QTmadeira == '1':
                s = 'Beneficiada'
            else:
                s = "bruta"
            print("\033[36m===\033[m" * 20)         
            if valida_campos(QTmadeira) > 2 or valida_campos(QTmadeira) < 0 or valida_campos(QTmadeira) == False:
                print("Digite somente as opções acima")       
                continue
            else:
                break
        while True:                 
                if QTmadeira == '1':
                    print("===" * 20) 
                    print('[1] metro quadrado')
                    print('[2] metro cubico')            
                    Tmetragem = (input(":"))
                    if Tmetragem == '1':
                        t = 'm²'
                    else:
                        t = "m³"
                    print("===" * 20)      
                    if(valida_campos(Tmetragem) > 2 or valida_campos(Tmetragem) < 0 or valida_campos(Tmetragem) == False): 
                        print("Digite um numero entre as opções")  
                        continue 
                    else:
                        break                      
                elif QTmadeira == '2':
                    print("===" * 20) 
                    comprimento = (input("Digite o comprimento"))
                    largura = (input("Digite a largura"))
                    expessura = (input("Digite a expessura"))
                    print("===" * 20)
                
                    t = "m³" 
                    if valida_campos(comprimento) == False or valida_campos(largura) == False or valida_campos(expessura) == False:
                        print("Digite um numero")
                        continue
                    else:                         
                         tamanho = valida_campos(comprimento) * valida_campos(largura) * valida_campos(expessura)
                         Tmetragem = "2"
                         break
                # else:                        
                #      tamanho = valida_campos(comprimento) * valida_campos(largura) * valida_campos(expessura)                     
                #      break
                                
        while True:                           
            if Tmetragem == '1' and QTmadeira == '1':
                    print("===" * 20) 
                    comprimento = (input("Digite o comprimento"))
                    largura = (input("Digite a largura"))
                    print("===" * 20) 
                    if valida_campos(comprimento) == False or valida_campos(largura) == False:
                        print("Digite um numero")
                        continue
                    else:
                        tamanho = valida_campos(comprimento) * valida_campos(largura)
                        Tmetragem = '0'                          
                        break     
                                 
            elif Tmetragem == '2' and QTmadeira == '1':
                    print("===" * 20) 
                    comprimento = (input("Digite o comprimento"))
                    largura = (input("Digite a largura"))
                    expessura = (input("Digite a expessura"))
                    print("===" * 20) 
                    if valida_campos(comprimento) == False or valida_campos(largura) == False or valida_campos(expessura) == False:
                        print("Digite um numero")
                        continue
                    else:
                        tamanho = valida_campos(comprimento) * valida_campos(largura) * valida_campos(expessura)
                        # Tmetragem = '0' 
                        break
            else:
                 break        
        while True:                       
            print("O tamanho é igual a {}".format(tamanho))   
            if(Tmetragem == '2'):
                print("===" * 20) 
                print("Tipo da madeira")
                print("[1] tabuas")
                print("[2] barotes")
                print("===" * 20) 
                Tipo = (input(":"))
                if Tmetragem == '1':
                    q = 'Tabuas'
                else:
                    q = "Barotes" 
                if(valida_campos(Tipo) > 2 or valida_campos(Tipo) < 0 or valida_campos(Tipo) == False):
                    print("Digite um numero entre as opções")
                    continue 
                else:
                    Tipo = "1"
                    break
            else:
                break
        while True:
            print("===" * 20)  
            QuantTabuas = (input("Quantidade a ser comprada: "))
            print("===" * 20) 
            if valida_campos(QuantTabuas) == False:
                print("Digite apenas numeros")
                continue
            else:
                break
        while True:
            print("===" * 20)     
            print("Digite a opção que voce gostaria de comprar")
            print("[1] Pinheiro araucaria")
            print("[2] Eucalipto")
            print("[3] Pinus ilhote")
            Qopção = str(input(":"))
            if Qopção == '1':
                u = 'Pinheiro araucaria'
            elif Qopção == '2':
                u = "Eucalipto"
            else:
                u = "Pinus Ilhote"
            print("===" * 20)  
            if(valida_campos(Qopção) > 3 or valida_campos(Qopção) < 0 or valida_campos(Qopção) == False):
                print("Digite apenas as opções acima")
                continue
            else:
                break
        while True:
            if(Qopção == '2'):                    
                    print("===" * 20)  
                    print("Qual tipo de eucalipto voce gostaria")
                    print("[1] Branco")
                    print("[2] Saligna")
                    print("[3] Cerejeira")
                    print("[4] Cerno")
                    OpEucalipto = str(input(":"))
                    if OpEucalipto == '1':
                         u = 'Branco'
                    elif OpEucalipto == '2':
                        u = "Saligna"
                    elif OpEucalipto == '3':
                        u = "Cerejeira"
                    else:
                        u = "Cerno"
                    print("===" * 20)  
                    if valida_campos(OpEucalipto) > 4 or valida_campos(OpEucalipto) < 0  or valida_campos(OpEucalipto) == False:
                        print("===" * 20)  
                        print("[1] primeira")
                        print("[2] Segunda")
                        print("[3] terceira")
                        print("[4] Quarta")
                        print("[5] Quinta") 
                        Qqualidade = str(input("Digite a qualidade da madeira"))
                        if Qqualidade == '1':
                             u = 'primeira'
                        elif Qqualidade == '2':
                            u = "Segunda"
                        elif Qqualidade == '3':
                            u = "terceira"
                        elif Qqualidade == "4":
                            u = "Quarta"
                        else:
                            u = "Quinta"
                        print("===" * 20)  
                        if valida_campos(OpEucalipto) > 5 or valida_campos(OpEucalipto) < 0 or valida_campos(OpEucalipto) == False:
                            print("Digite apenas as opções acima")
                            continue
                        else:
                            break 
                    else:
                        print("===" * 20)  
                        print("[1] primeira")
                        print("[2] Segunda")
                        print("[3] terceira")
                        print("[4] Quarta")
                        print("[5] Quinta")
                        print("===" * 20)  
                        Qqualidade = str(input("Digite a qualidade da madeira"))
                        if Qqualidade == '1':
                             p = 'primeira'
                        elif Qqualidade == '2':
                            p = "Segunda"
                        elif Qqualidade == '3':
                            p = "terceira"
                        elif Qqualidade == "4":
                            p = "Quarta"
                        else:
                            p = "Quinta"
                        if valida_campos(Qqualidade) > 5 or valida_campos(Qqualidade) < 0 or valida_campos(Qqualidade) == False:
                            print("Digite apenas as opções acima")
                            continue
                        else:
                            break   
            else:
                print("===" * 20)  
                print("[1] primeira")
                print("[2] Segunda")
                print("[3] terceira")
                print("[4] Quarta")
                print("[5] Quinta") 
                Qqualidade = str(input("Digite a qualidade da madeira"))
                if Qqualidade == '1':
                    p = 'primeira'
                elif Qqualidade == '2':
                    p = "Segunda"
                elif Qqualidade == '3':
                    p = "terceira"
                elif Qqualidade == "4":
                    p = "Quarta"
                else:
                    p = "Quinta"
                print("===" * 20)  
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
                    # Qinformação = ""
        InfTam = ""
        
        Tmetragem2 = ""
        Qinformação = ""                    
       
        print("===" * 20)      
        print("Voce digitou essas informações")         
        print("Tipo de madeira {} - {}".format(QTmadeira, s)) 
        print("Tipo da metragem {} - {}".format(Tmetragem, t))
        print("Tamanho {} - {}".format(tamanho, t))
        print("A madeira é {} - {}".format(Qopção, u))
        print("A qualidade é {} - {}".format(Qqualidade, p)) 
        # print("Tipo da madeira {}".format(Tipo))
        print("A quantidade é igual a {}".format(QuantTabuas))  
        print("Total da metragem {} - {}".format(valida_campos(QuantTabuas) * tamanho, t)) 

        i = False 
        
        

        Qinformação = ""
        InfTam = ""
        
        Tmetragem2 = ""
        Qinformação = "" 
        while True:          
               
            print("===" * 20)  
            while True:
                print("===" * 20)              
                informacao = str(input("Voce deseja alterar alguma informação[S/N]")).upper()
                print("===" * 20)  
                if informacao == 'S' or informacao == 'N':
                    break
                else:
                    print("Digite apenas S ou N")
                    continue
            
            if informacao == "N":                
                break
             
                                   
            if informacao == "S":
                print("===" * 20)          
                print("Digite a opção que deseja mudar")
                print("[1] Tipo da madeira")                
                print("[2] A madeira")
                print("[3] A qualidade da madeira")
                print("[4] Tipo da madeira")
                print("[5] Quantidade")
                Qinformação = str(input(":"))
                print("===" * 20)  
                if valida_campos(Qinformação) > 5 or valida_campos(Qinformação) < 0 or valida_campos(Qinformação) == False:
                    print("Digite apenas as opções acima")
                    continue
                else:
                    break
        while True:        
            if Qinformação == '1':
                print("===" * 20)  
                print("É beneficiada ou bruta")
                print("[1] Beneficiada")
                print("[2] Bruta")                
                QTmadeira = str(input(":"))
                print("===" * 20)  
                if(valida_campos(QTmadeira) > 3 or valida_campos(QTmadeira) < 0 or valida_campos(QTmadeira) == False):
                    print("Digite apenas as opções acima")
                    continue
                else:
                    print("===" * 20)  
                    InfTam = str(input("Voce deseja alterar a unidade de medida [S/N]")).upper()
                    print("===" * 20)  
                    if InfTam == "N":
                        Tmetragem2 = '0'
                        break
                                     
                    if InfTam == 'S' or InfTam == 'N':
                         break            
                    else:
                         print("Digite apenas S ou N")
                         continue          
                                         
            else:
                break         

        while True:    
            if InfTam == "S" and QTmadeira == "1":
                print("===" * 20)  
                print('[1] metro quadrado')
                print('[2] metro cubico')            
                Tmetragem2 = str(input(":"))
                print("===" * 20)  
                if valida_campos(Tmetragem2) > 3 or valida_campos(Tmetragem2) < 0 or valida_campos(Tmetragem2) == False:
                    print("Digite apenas as opções acima")
                    continue
                else:
                    break
            else:
                break   
        while True:
            if Tmetragem2 == "1":
                print("===" * 20)  
                comprimento = str(input("Digite o comprimento"))
                largura = str(input("Digite a largura"))
                print("===" * 20)  
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
                print("===" * 20)  
                comprimento = str(input("Digite o comprimento"))
                largura = str(input("Digite a largura"))
                expessura = str(input("Digite a expessura"))
                print("===" * 20)  
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
                print("===" * 20)           
                comprimento = str(input("Digite o comprimento"))
                largura = str(input("Digite a largura"))
                expessura = str(input("Digite a expessura"))
                print("===" * 20)  
                if valida_campos(comprimento) == False or valida_campos(largura) == False or valida_campos(expessura) == False:
                    print("Digite apenas numeros")
                    continue
                else:
                    tamanho = valida_campos(comprimento) * valida_campos(largura) * valida_campos(expessura)                                  
                    break
            else:
                break
        
        while True:     
            if Qinformação == "2":
                print("===" * 20) 
                print("Digite a opção que voce gostaria de comprar")
                print("[1] Pinheiro araucaria")
                print("[2] Eucalipto")
                print("[3] Pinus ilhote")
                Qopção = (input(":"))
                print("===" * 20)  
                if(valida_campos(Qinformação) > 3 or valida_campos(Qinformação) < 0 or valida_campos(Qinformação) == False):
                    print("Digite apenas numeros")
                    continue
                else:
                    if Qopção == "2": 
                        print("===" * 20)                             
                        print("Qual tipo de eucalipto voce gostaria")
                        print("[1] Branco")
                        print("[2] Saligna")
                        print("[3] Cerejeira")
                        print("[4] Cerno")
                        OpEucalipto = (input(":"))
                        print("===" * 20)  
                        if valida_campos(OpEucalipto) > 4 or valida_campos(OpEucalipto) < 0 or valida_campos(OpEucalipto) == False:
                            print("Digite apenas as opções acimas")
                            continue
                        else:
                            break                    
            else:
                break     
                         
            if Qopção == "2":  
                print("===" * 20)                            
                print("Qual tipo de eucalipto voce gostaria")
                print("[1] Branco")
                print("[2] Saligna")
                print("[3] Cerejeira")
                print("[4] Cerno")
                OpEucalipto = (input(":"))
                print("===" * 20)  
                if valida_campos(OpEucalipto) > 4 or valida_campos(OpEucalipto) < 0 or valida_campos(OpEucalipto) == False:
                    print("Digite apenas as opções acimas")
                    continue
                else:
                    break
                
            else:
                break
              
        while True:
                if Qinformação == "4":
                    print("===" * 20)  
                    print("Tipo da madeira")
                    print("[1] tabuas")
                    print("[2] barotes")
                    Tipo = (input(":"))
                    print("===" * 20)  
                    if valida_campos(Tipo) > 2 or valida_campos(Tipo) < 0 or valida_campos(Tipo) == False:
                        print("Digite apenas as opções acima")
                        continue
                    else:
                        break
                else:
                    break
        while True:
                if Qinformação == '5': 
                    print("===" * 20)            
                    QuantTabuas = (input("Quantidade a ser comprada: "))
                    print("===" * 20)  
                    if valida_campos(QuantTabuas) == False:
                        print("Digite apenas numeros")
                        continue
                    else:
                        break  
                else: 
                    break


        while True:
                if Qinformação == '3':
                    print("===" * 20)  
                    print("[1] primeira")
                    print("[2] Segunda")
                    print("[3] terceira")
                    print("[4] Quarta")
                    print("[5] Quinta") 
                    Qqualidade = str(input("Digite a qualidade da madeira"))                    
                    print("===" * 20)  
                    if valida_campos(Qqualidade) > 5 or valida_campos(Qqualidade) < 0 or valida_campos(Qqualidade) == False:
                        print("Digite apenas as opções acima")
                        continue
                    else:
                        break  
                else:
                    break      
        


# inf = str(input("Voce deseja alterar mais dados[S/N]")).upper()
# if inf == 'S':
#     editaDados(QTmadeira,Tmetragem,tamanho,Qopção,Qqualidade,QuantTabuas)
# else:   
        while True:
            if Tmetragem == '1':
                print("===" * 20)  
                ValorMetragem = (input("Valor ao m²: "))
                print("===" * 20)  
                if valida_campos(ValorMetragem) == False:
                    print("Digite apenas numeros") 
                else:
                    break
            elif Tmetragem == '2' or QTmadeira == '2':
                    print("===" * 20)  
                    ValorMetragem = (input("Valor em m³: "))
                    print("===" * 20)  
                    if valida_campos(ValorMetragem) == False:
                        print("Digite apenas numeros") 
                    else:
                        break
            else:
                break             
                
print("===" * 20) 
preco =  valida_campos(QuantTabuas) * tamanho
preco = preco * valida_campos(ValorMetragem)
print("O preço ficara igual a {:.2f}".format(preco))             
print("===" * 20) 

dados = [nomeCliente, QTmadeira, tamanho, Qopção, Qqualidade,valida_campos(QuantTabuas) * tamanho,  ValorMetragem,QuantTabuas]


# Dicionário de exemplo


# Serializa os dados em bytes
dados_serializados = pickle.dumps(dados)

# Salva os bytes serializados em um arquivo de bloco de notas
with open('dados.txt', 'wb') as arquivo:
    arquivo.write(dados_serializados)


# Abre o arquivo no modo de leitura binária (se existir)

    # Se o arquivo não existir, inicia com uma lista vazia
    dados_existentes = []

# Adiciona os novos dados aos dados existentes
dados_existentes.extend(dados)

# Salva os dados atualizados no arquivo de bloco de notas usando pickle
with open('dados.pkl', 'ab') as arquivo:
    pickle.dump(dados_existentes, arquivo)
# Exibe os objetos recuperados

with open('dados.pkl', 'rb') as arquivo:
    while True:
        try:
            objeto = pickle.load(arquivo)
            # Processar o objeto desserializado
            print(objeto)
        except EOFError:
            break


# Utilize os dados desserializados
# with open('dados.pkl', 'rb') as arquivo:
#     objetos = pickle.load(arquivo) 

# # Exibe cada objeto desserializado

# for objeto in objetos:
#     print(objeto)
    
    

# Exibe o conteúdo na saída

        



