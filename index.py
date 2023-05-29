import pickle
import json
print("\033[36m*\033[m" * 20)
print("\033[36m Tabelador\033[m ")
print("\033[36m*\033[m" * 20)
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
            nomeCliente = str(input("\033[32mDigite o nome do cliente\033[m"))
                      
            print("\033[36m===\033[m" * 20)    
            print("\033[32mÉ beneficiada ou bruta:\033[m")
            print("\033[33m[1] Beneficiada\033[m")
            print("\033[33m[2] Bruta\033[m")
            QTmadeira = (input("\033[36m:\033[m"))
            if QTmadeira == '1':
                s = 'Beneficiada'
            else:
                s = "bruta"
            print("\033[36m===\033[m" * 20)         
            if valida_campos(QTmadeira) > 2 or valida_campos(QTmadeira) < 0 or valida_campos(QTmadeira) == False:
                print("\033[91mDigite apenas as opções acima\033[m")    
                continue
            else:
                break
        while True:                 
                if QTmadeira == '1':
                    print("\033[36m===\033[m" * 20)
                    print("\033[32mQual metragem:\033[m") 
                    print("\033[33m[1] Metro quadrado\033[m")
                    print("\033[33m[2] Metro cubico\033[m")      
                    Tmetragem = (input("\033[36m:\033[m"))
                    if Tmetragem == '1':
                        t = 'm²'
                    else:
                        t = "m³"
                    print("\033[36m===\033[m" * 20)     
                    if(valida_campos(Tmetragem) > 2 or valida_campos(Tmetragem) < 0 or valida_campos(Tmetragem) == False): 
                        print("\033[91mDigite apenas as opções acima\033[m")    
                        continue 
                    else:
                        break                      
                elif QTmadeira == '2':
                    print("\033[36m===\033[m" * 20)
                    comprimento = (input("\033[32mDigite o comprimento:\033[m"))
                    largura = (input("\033[32mDigite o largura:\033[m"))
                    expessura = (input("\033[32mDigite o expessura:\033[m"))
                    print("\033[36m===\033[m" * 20)
                
                    t = "m³" 
                    if valida_campos(comprimento) == False or valida_campos(largura) == False or valida_campos(expessura) == False:
                        print("\033[91mDigite apenas numeros\033[m")    
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
                    print("\033[36m===\033[m" * 20) 
                    comprimento = (input("\033[32mDigite o comprimento:\033[m"))
                    largura = (input("\033[32mDigite o largura:\033[m"))
                    print("\033[36m===\033[m" * 20) 
                    if valida_campos(comprimento) == False or valida_campos(largura) == False:
                        print("\033[91mDigite apenas numeros\033[m")     
                        continue
                    else:
                        tamanho = valida_campos(comprimento) * valida_campos(largura)
                        Tmetragem = '0'                          
                        break     
                                 
            elif Tmetragem == '2' and QTmadeira == '1':
                    print("\033[36m===\033[m" * 20)
                    comprimento = (input("\033[32mDigite o comprimento:\033[m"))
                    largura = (input("\033[32mDigite o largura:\033[m"))
                    expessura = (input("\033[32mDigite o expessura:\033[m"))
                    print("\033[36m===\033[m" * 20) 
                    if valida_campos(comprimento) == False or valida_campos(largura) == False or valida_campos(expessura) == False:
                        print("\033[91mDigite apenas numeros\033[m")   
                        continue
                    else:
                        tamanho = valida_campos(comprimento) * valida_campos(largura) * valida_campos(expessura)
                        # Tmetragem = '0' 
                        break
            else:
                 break        
        while True:                       
            print("\033[33mO tamanho é igual a {}\033[m".format(tamanho))   
            if(Tmetragem == '2'):
                print("\033[36m===\033[m" * 20) 
                print("\033[32mTipo de madeira\033[m") 
                print("\033[33m[1] Tabuas\033[m")
                print("\033[33m[2] Barotes\033[m")
                print("\033[36m===\033[m" * 20) 
                Tipo = (input("\033[36m:\033[m"))
                if Tmetragem == '1':
                    q = 'Tabuas'
                else:
                    q = "Barotes" 
                if(valida_campos(Tipo) > 2 or valida_campos(Tipo) < 0 or valida_campos(Tipo) == False):
                    print("\033[91mDigite apenas as opções acima\033[m")   
                    continue 
                else:
                    Tipo = "1"
                    break
            else:
                break
        while True:
            print("\033[36m===\033[m" * 20)  
            QuantTabuas = (input("\033[32mQuantidade a ser comprada:\033[m"))
            print("\033[36m===\033[m" * 20) 
            if valida_campos(QuantTabuas) == False:
                print("\033[91mDigite apenas numeros\033[m")   
                continue
            else:
                break
        while True:
            print("\033[36m===\033[m" * 20)     
            print("\033[32mDigite o tipo de arvore:\033[m") 
            print("\033[33m[1] Pinheiro araucaria\033[m")
            print("\033[33m[2] Eucalipto\033[m")
            print("\033[33m[3] Pinus ilhote\033[m")
            Qopção = str(input("\033[36m:\033[m"))
            if Qopção == '1':
                u = 'Pinheiro araucaria'
            elif Qopção == '2':
                u = "Eucalipto"
            else:
                u = "Pinus Ilhote"
            print("\033[36m===\033[m" * 20)  
            if(valida_campos(Qopção) > 3 or valida_campos(Qopção) < 0 or valida_campos(Qopção) == False):
                print("\033[91mDigite apenas as opções acima\033[m")   
                continue
            else:
                break
        while True:
            print("\033[36m===\033[m" * 20)  
            if(Qopção == '2'):                    
                    print("\033[36m===\033[m" * 20)  
                    print("\033[32mDigite o tipo de eucalipto:\033[m") 
                    print("\033[33m[1] Branco\033[m")
                    print("\033[33m[2] Saligna\033[m")
                    print("\033[33m[3] Cerejeira\033[m")
                    print("\033[33m[4] Cerno\033[m")
                    OpEucalipto = str(input("\033[36m:\033[m"))
                    if OpEucalipto == '1':
                         u = 'Branco'
                    elif OpEucalipto == '2':
                        u = "Saligna"
                    elif OpEucalipto == '3':
                        u = "Cerejeira"
                    else:
                        u = "Cerno"
                    print("\033[36m===\033[m" * 20)  
                    if valida_campos(OpEucalipto) > 4 or valida_campos(OpEucalipto) < 0  or valida_campos(OpEucalipto) == False:
                        print("\033[36m===\033[m" * 20) 
                        print("\033[32mDigite a qualidade da madeira:\033[m") 
                        print("\033[33m[1] Primeira\033[m")
                        print("\033[33m[2] Segunda\033[m")
                        print("\033[33m[3] Terceira\033[m")
                        print("\033[33m[4] Quarta\033[m")
                        print("\033[33m[5] Quinta\033[m")
                        Qqualidade = str(input("\033[36m:\033[m"))
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
                        print("\033[36m===\033[m" * 20)
                        if valida_campos(OpEucalipto) > 5 or valida_campos(OpEucalipto) < 0 or valida_campos(OpEucalipto) == False:
                            print("\033[91mDigite apenas as opções acima\033[m")   
                            continue
                        else:
                            break 
                    else:
                        print("\033[36m===\033[m" * 20)
                        print("\033[33m[1] Primeira\033[m")
                        print("\033[33m[2] Segunda\033[m")
                        print("\033[33m[3] Terceira\033[m")
                        print("\033[33m[4] Quarta\033[m")
                        print("\033[33m[5] Quinta\033[m")
                        print("\033[36m===\033[m" * 20)
                        Qqualidade = str(input("\033[32mDigite a qualidade da madeira:\033[m"))
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
                            print("\033[91mDigite apenas as opções acima\033[m")   
                            continue
                        else:
                            break   
            else:
                print("\033[36m===\033[m" * 20) 
                print("\033[33m[1] Primeira\033[m")
                print("\033[33m[2] Segunda\033[m")
                print("\033[33m[3] Terceira\033[m")
                print("\033[33m[4] Quarta\033[m")
                print("\033[33m[5] Quinta\033[m") 
                Qqualidade = str(input("\033[32mDigite a qualidade da madeira:\033[m"))
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
                print("\033[36m===\033[m" * 20)  
                if valida_campos(Qqualidade) > 5 or valida_campos(Qqualidade) < 0 or valida_campos(Qqualidade) == False:
                    print("\033[91mDigite apenas as opções acima\033[m")   
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
       
        print("\033[36m===\033[m" * 20)     
        print("\033[32mVoce digitou essas informações\033[m")         
        print("\033[33mTipo de madeira {}\033[m - {}".format(QTmadeira, s)) 
        print("\033[33mTipo de metragem {}\033[m - {}".format(Tmetragem, t))
        print("\033[33mTamanho {}\033[m - {}".format(tamanho, t))
        print("\033[33mA madeira é {}\033[m - {}".format(Qopção, u))
        print("\033[33mA qualidade é {}\033[m - {}".format(Qqualidade, p)) 
        # print("Tipo da madeira {}".format(Tipo))
        print("\033[33mA quantidade é igual a {}\033[m - {}".format(QuantTabuas))  
        print("\033[33mTotal da metragem {}\033[m - {}".format(valida_campos(QuantTabuas) * tamanho, t)) 

        i = False 
        
        

        Qinformação = ""
        InfTam = ""
        
        Tmetragem2 = ""
        Qinformação = "" 
        while True:          
               
            print("\033[36m===\033[m" * 20)  
            while True:
                print("\033[36m===\033[m" * 20)              
                informacao = str(input("\033[32mVocê deseja alterar alguma informação?[S/N]\033[m")).upper()
                print("\033[36m===\033[m" * 20)  
                if informacao == 'S' or informacao == 'N':
                    break
                else:
                    print("\033[91mDigite apenas S ou N\033[m")   
                    continue
            
            if informacao == "N":                
                break
             
                                   
            if informacao == "S":
                print("\033[36m===\033[m" * 20)          
                print("\033[32mDigite a opção que deseja alterar:\033[m")
                print("\033[33m[1] Tipo de madeira\033[m")              
                print("\033[33m[2] A arvore\033[m")
                print("\033[33m[3] A qualidade da madeira\033[m")
                print("\033[33m[4] Tipo de madeira\033[m")
                print("\033[33m[5] Quantidade\033[m")
                Qinformação = str(input("\033[36m:\033[m"))
                print("\033[36m===\033[m" * 20) 
                if valida_campos(Qinformação) > 5 or valida_campos(Qinformação) < 0 or valida_campos(Qinformação) == False:
                    print("\033[91mDigite apenas as opções acima\033[m")   
                    continue
                else:
                    break
        while True:        
            if Qinformação == '1':
                print("\033[36m===\033[m" * 20) 
                print("\033[32mÉ beneficiada ou bruta:\033[m")
                print("\033[33m[1] Beneficiada\033[m")
                print("\033[33m[2] Bruta\033[m")               
                QTmadeira = str(input(":"))
                print("\033[36m===\033[m" * 20)  
                if(valida_campos(QTmadeira) > 3 or valida_campos(QTmadeira) < 0 or valida_campos(QTmadeira) == False):
                    print("\033[91mDigite apenas as opções acima\033[m")   
                    continue
                else:
                    print("\033[36m===\033[m" * 20)  
                    InfTam = str(input("\033[32mVocê deseja alterar alguma unidade de medida?[S/N]\033[m")).upper()
                    print("\033[36m===\033[m" * 20)  
                    if InfTam == "N":
                        Tmetragem2 = '0'
                        break
                                     
                    if InfTam == 'S' or InfTam == 'N':
                         break            
                    else:
                         print("\033[91mDigite apenas S ou N\033[m")   
                         continue          
                                         
            else:
                break         

        while True:    
            if InfTam == "S" and QTmadeira == "1":
                print("\033[36m===\033[m" * 20) 
                print("\033[33m[1] Metro quadrado\033[m")
                print("\033[33m[2] Metro cubico\033[m")            
                Tmetragem2 = str(input("\033[36m:\033[m"))
                print("\033[36m===\033[m" * 20)
                if valida_campos(Tmetragem2) > 3 or valida_campos(Tmetragem2) < 0 or valida_campos(Tmetragem2) == False:
                    print("\033[91mDigite apenas as opções acima\033[m")   
                    continue
                else:
                    break
            else:
                break   
        while True:
            if Tmetragem2 == "1":
                print("\033[36m===\033[m" * 20)  
                comprimento = str(input("\033[32mDigite o comprimento:\033[m"))
                largura = str(input("\033[32mDigite a largura:\033[m"))
                print("\033[36m===\033[m" * 20) 
                if(valida_campos(comprimento) == False or valida_campos(largura) == False):
                    print("\033[91mDigite apenas numeros\033[m")   
                    continue
                else:
                    Tmetragem = Tmetragem2
                    tamanho = valida_campos(comprimento) * valida_campos(largura)
                    break
            else:
                break
        
        while True:        
            if Tmetragem2 == "2":
                print("\033[36m===\033[m" * 20)  
                comprimento = str(input("\033[32mDigite o comprimento:\033[m"))
                largura = str(input("\033[32mDigite a largura:\033[m"))
                expessura = str(input("\033[32mDigite a expessura:\033[m"))
                print("\033[36m===\033[m" * 20) 
                if valida_campos(comprimento) == False or valida_campos(largura) == False:
                    print("\033[91mDigite apenas numeros\033[m")   
                    continue
                else:
                    Tmetragem = Tmetragem2
                    tamanho = valida_campos(comprimento) * valida_campos(largura) * valida_campos(expessura)   
                    break
            else:
                break
        while True:      
            if InfTam == "S" and QTmadeira == "2":
                print("\033[36m===\033[m" * 20)           
                comprimento = str(input("\033[32mDigite o comprimento:\033[m"))
                largura = str(input("\033[32mDigite a largura:\033[m"))
                expessura = str(input("\033[32mDigite a expessura:\033[m"))
                print("\033[36m===\033[m" * 20)
                if valida_campos(comprimento) == False or valida_campos(largura) == False or valida_campos(expessura) == False:
                    print("\033[91mDigite apenas numeros\033[m")   
                    continue
                else:
                    tamanho = valida_campos(comprimento) * valida_campos(largura) * valida_campos(expessura)                                  
                    break
            else:
                break
        
        while True:     
            if Qinformação == "2":
                print("\033[36m===\033[m" * 20) 
                print("\033[32mDigite o tipo de arvore:\033[m") 
                print("\033[33m[1] Pinheiro araucaria\033[m")
                print("\033[33m[2] Eucalipto\033[m")
                print("\033[33m[3] Pinus ilhote\033[m")
                Qopção = (input("\033[36m:\033[m"))
                print("\033[36m===\033[m" * 20) 
                if(valida_campos(Qinformação) > 3 or valida_campos(Qinformação) < 0 or valida_campos(Qinformação) == False):
                    print("\033[91mDigite apenas numeros\033[m")   
                    continue
                else:
                    if Qopção == "2": 
                        print("\033[36m===\033[m" * 20)                           
                        print("\033[32mDigite o tipo de eucalipto:\033[m") 
                        print("\033[33m[1] Branco\033[m")
                        print("\033[33m[2] Saligna\033[m")
                        print("\033[33m[3] Cerejeira\033[m")
                        print("\033[33m[4] Cerno\033[m")
                        OpEucalipto = (input("\033[36m:\033[m"))
                        print("\033[36m===\033[m" * 20) 
                        if valida_campos(OpEucalipto) > 4 or valida_campos(OpEucalipto) < 0 or valida_campos(OpEucalipto) == False:
                            print("\033[91mDigite apenas as opções acima\033[m")   
                            continue
                        else:
                            break                    
            else:
                break     
                         
            if Qopção == "2":  
                print("\033[36m===\033[m" * 20)                           
                print("\033[32mDigite o tipo de eucalipto:\033[m") 
                print("\033[33m[1] Branco\033[m")
                print("\033[33m[2] Saligna\033[m")
                print("\033[33m[3] Cerejeira\033[m")
                print("\033[33m[4] Cerno\033[m")
                OpEucalipto = (input("\033[36m:\033[m"))
                print("\033[36m===\033[m" * 20)
                if valida_campos(OpEucalipto) > 4 or valida_campos(OpEucalipto) < 0 or valida_campos(OpEucalipto) == False:
                    print("\033[91mDigite apenas as opções acima\033[m")
                    continue
                else:
                    break
                
            else:
                break
              
        while True:
                if Qinformação == "4":
                    print("\033[36m===\033[m" * 20) 
                    print("\033[32mTipo de madeira:\033[m") 
                    print("\033[33m[1] Tabuas\033[m")
                    print("\033[33m[2] Barotes\033[m")
                    Tipo = (input("\033[36m:\033[m"))
                    print("\033[36m===\033[m" * 20) 
                    if valida_campos(Tipo) > 2 or valida_campos(Tipo) < 0 or valida_campos(Tipo) == False:
                        print("\033[91mDigite apenas as opções acima\033[m")
                        continue
                    else:
                        break
                else:
                    break
        while True:
                if Qinformação == '5': 
                    print("\033[36m===\033[m" * 20)           
                    QuantTabuas = (input("\033[32mQuantidade a ser comprada:\033[m"))
                    print("\033[36m===\033[m" * 20) 
                    if valida_campos(QuantTabuas) == False:
                        print("\033[91mDigite apenas numeros\033[m")
                        continue
                    else:
                        break  
                else: 
                    break


        while True:
                if Qinformação == '3':
                    print("\033[36m===\033[m" * 20) 
                    print("\033[33m[1] Primeira\033[m")
                    print("\033[33m[2] Segunda\033[m")
                    print("\033[33m[3] Terceira\033[m")
                    print("\033[33m[4] Quarta\033[m")
                    print("\033[33m[5] Quinta\033[m")
                    Qqualidade = str(input("\033[32mDigite a qualidade da madeira:\033[m"))                    
                    print("\033[36m===\033[m" * 20) 
                    if valida_campos(Qqualidade) > 5 or valida_campos(Qqualidade) < 0 or valida_campos(Qqualidade) == False:
                        print("\033[91mDigite apenas as opções acima\033[m")
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
                print("\033[36m===\033[m" * 20)
                ValorMetragem = (input("\033[32mValor ao metro quadrado:\033[m"))
                print("\033[36m===\033[m" * 20)  
                if valida_campos(ValorMetragem) == False:
                    print("\033[91mDigite apenas numeros\033[m") 
                else:
                    break
            elif Tmetragem == '2' or QTmadeira == '2':
                    print("\033[36m===\033[m" * 20)  
                    ValorMetragem = (input("\033[32mValor ao metro cubico:\033[m"))
                    print("\033[36m===\033[m" * 20) 
                    if valida_campos(ValorMetragem) == False:
                        print("\033[91mDigite apenas numeros\033[m") 
                    else:
                        break
            else:
                break             
                
print("\033[36m===\033[m" * 20) 
preco =  valida_campos(QuantTabuas) * tamanho
preco = preco * valida_campos(ValorMetragem)
print("O preço ficara igual a {:.2f}".format(preco))             
print("\033[36m===\033[m" * 20) 

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
        



