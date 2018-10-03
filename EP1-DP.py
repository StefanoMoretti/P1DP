"""
Created on Thu Sep 13 11:01:36 2018

@author: ricar
"""

comandas = {1 : {}}
cardapio = {}

rodandogeral =  True
while rodandogeral:
    
    escolha_1 = input("O que deseja acessar? (Menu, Comanda ou 0 para sair) :  ")
   
    if escolha_1 == "Comanda": 
        Comanda = int(input("Digite o numero da comanda:  "))
        if Comanda < 1:
            print('Numero de comanda inválido')
            break
        else:
            if Comanda not in comandas:
                comandas[Comanda] = 0
            
        rodando = True
        while rodando:
                
            print("0: Sair")
            print("1: Adicionar item")
            print("2: Remover item")
            print("3: Imprimir comanda")
                
    
            escolha = int(input("Faça a sua escolha: "))
    
    
            if escolha == 0:
                rodando = False
    
            elif escolha == 1:
                novo_produto = input("Novo Produto: ")
                novo_produto = novo_produto.lower()
        
                if novo_produto not in cardapio:
                    print("Não temos este item no cardápio.")
                else:
                    quantidade = int(input("Quantidade: "))
                    preco_unitario = cardapio[novo_produto]
                    preco_total = quantidade*preco_unitario
                    comandas[Comanda][novo_produto] = preco_total
                    print("Item Adicionado")  
                        
                        
            elif escolha == 2:
                            
                remove_produto = input("Retirar o Produto: ")
                remove_produto = remove_produto.lower()
                if remove_produto not in comandas[Comanda]:
                    print("Produto não encontrado!")
                else:
                    del comandas[Comanda][remove_produto]
                    print("Item removido")
        
       
            elif escolha == 3:
                if len(comandas[Comanda]) <= 0:
                    print("Nemnhum item na comanda.")
                else:

                    Total = 0
                    for e in comandas[Comanda]:
                        
                        print("")
                        print("Produto: {0}".format(e))
                        print("Quantidade: {0}".format(comandas[Comanda][e]))
                        print("")
                
                    for i in cardapio:
                        if i == e:
                            print("Preço unitário: {0}".format(cardapio[e]))
                            print("Preço total: {0}" .format(cardapio[e]*quantidade))
                            print("")
        
                    for produto in cardapio:
                        if produto in comandas[Comanda]:
                            Total = Total + preco_total
                            
                            Taxa = Total*0.10
                            Total_com_taxa = Total + Taxa
                            print("Total: {0}".format(Total))
                            print("Total com 10%: {0}".format(Total_com_taxa))
        

    if escolha_1 == "Menu":

        rodando2 = True
        while rodando2:
        
            print('0: Sair')
            print("1: Imprimir cardápio")
            print("2: Adcionar item ao cardápio")
            print("3: Modificar preço de produto")
            print("4: Remover produto")
            c = int(input("O que deseja fazer?:  "))
            
            if c == 0:
                rodando2 = False
            
            if c == 1:
                for i in cardapio:
                    if i == None:
                        print ('Cardápio Vazio')
                    else:
                        print("{0} (R$ {1})".format(i, cardapio[i]))
                    
            
            elif c == 2:
                novo_item = input("Qual produto deseja adicionar?: ")
                if novo_item in cardapio:
                    print('Produto já existente')
                else:
                    preco_novo_item = float(input("Qual o preço unitário?: "))
                    if preco_novo_item > 0:
                        cardapio[novo_item] = preco_novo_item
                        print("Produto adcionado ao cardapio.") 
                    
                    else:
                        print('Valor negativo inválido')
                    
            elif c == 3:
                product = input("Qual produto você deseja alterar?: ")
                if product not in cardapio:
                    print ('Produto não disponível')
                else:
                    novo_preco = int(input("Qual o novo preço?: "))
                    if novo_preco > 0:
                        cardapio[product] = novo_preco
                        print('Valor alterado')
                    else:
                        print('Valor negativo inválido')
                        
            elif c == 4:
                rem = input('Qual produto deseja remover?:  ')
                if rem not in cardapio:
                    print('Produto não disponível')
                else:
                    cardapio.__delitem__(rem)
                    print('Produto removido')
                    
        
    else:
        if escolha_1 == '0':
            break
        else:
            print("Escolha inválida")

            
        

    


            
            
            
                    
             
            

    
    
         
            
    
 
     
    