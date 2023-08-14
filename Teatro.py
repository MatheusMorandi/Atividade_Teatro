
tamanho_teatro = []

valor_ingre = 0.0

ingre_vend = 0

ingre_reserv = 0

val_total = 0.0

teatro_ativo = False

while True:

  menu_teatro = int(input ("""Bem-Vindo ao menu do espetáculo,
  selecione dentre as opções abaixo o que gostaria de fazer:
  [1] Iniciar o teatro.
  [2] Reservar lugar.
  [3] Comprar lugar.
  [4] Liberar lugar.
  [5] Listar poltronas.
  [6] Encerrar o espetáculo.
  [7] Reiniciar o espetáculo.
  [0] Encerrar o programa.

  """))

  if str(menu_teatro) in ["1","2","3","4","5","6","7","0"]:

    if teatro_ativo == False:

      if menu_teatro == 1:

        teatro_ativo = True

        print ()

        linhas_espetaculo = int(input("Digite quantas linhas serão ocupadas: "))

        print ()

        colunas_espetaculo= int(input("Digite quantas colunas serão ocupadas: "))

        print ()

        tamanho_espetaculo =  linhas_espetaculo * colunas_espetaculo

        if tamanho_espetaculo <= 90000:

          for i in range(linhas_espetaculo):

            tamanho_teatro.append([])

            for j in range(colunas_espetaculo):

              tamanho_teatro[i].append(0)

          for k in range(len(tamanho_teatro)):

              print(tamanho_teatro[k])

          print()

          print(f"Espetáculo com {tamanho_espetaculo} poltronas cadastrado com sucesso!!!")

          print()

          valor_ingre = float(input("Digite o valor que será cobrado por ingresso R$ "))

          print()

        else:

          print()

          print("Valores não aceitos por favor insira valores menores!!!")

          print()

      elif menu_teatro == 0:

        print()

        print("Programa encerrado com sucesso!!!")

        print()

        break

      else:

        print()

        print("Por favor crie um espetáculo primeiro!!!")

        print()

    if teatro_ativo == True:

      if menu_teatro == 1:

        print()

        print("Você não pode criar dois espetáculos em simultâneo!!!")

        print()

      elif menu_teatro == 2:

        print()

        for k in range(len(tamanho_teatro)):

          print(tamanho_teatro[k])

        l = int(input("Informe a fileira desejada para reservar a poltrona: "))
        
        l -= 1

        print()

        c = int(input("Informe a coluna desejada para reservar a poltrona: "))

        c -= 1

        if tamanho_teatro[l,c] == 0:

          print()

          escolha = str(input("A poltrona está disponível! Deseja fazer a reserva? [S/N]"))

          if escolha.upper() in ["S","SIM"]:

            tamanho_teatro[l,c] = 1

            print()
            
            print(f"O valor a ser pago é R${valor_ingre * (30/100)}")

            val_total = val_total + (valor_ingre * (30/100))

            ingre_reserv += 1

        else:

          print()

          print("Não é possível realizar a operação, pois a poltrona em questão já esta reservada!!!")

        print()

      elif menu_teatro == 3:

        print()

        for k in range(len(tamanho_teatro)):

          print(tamanho_teatro[k])

        print()

        l = int(input("Informe a fileira desejada para comprar a poltrona: "))
        
        l -= 1

        print()

        c = int(input("Informe a coluna desejada para comprar a poltrona: "))

        c -= 1

        if tamanho_teatro[l,c] == 0:

          print()

          escolha = str(input("A poltrona está disponível! Deseja efetuar a compra? [S/N] "))

          if escolha.upper() in ["S","SIM"]:

            tamanho_teatro[l,c] = 2

            print()
            
            print(f"O valor a ser pago é R${valor_ingre}")

            val_total = val_total + valor_ingre

            ingre_vend += 1

        elif tamanho_teatro[l,c] == 1:

          print()

          escolha = str(input("A poltrona está reservada! Deseja efetuar a compra? [S/N]"))

          if escolha.upper() in ["S","SIM"]:

            tamanho_teatro[l,c] = 2

            print()
            
            print(f"O valor a ser pago é R${valor_ingre * (70/100)}")

            val_total = val_total + (valor_ingre * (70/100))

            ingre_reserv -= 1

            ingre_vend += 1


      elif menu_teatro == 4:

        print()

        for k in range(len(tamanho_teatro)):

          print(tamanho_teatro[k])

        print()

        l = int(input("Informe a fileira desejada para liberar a poltrona: "))
        
        l -= 1

        print()

        c = int(input("Informe a coluna desejada para liberar a poltrona: "))

        c -= 1

        if tamanho_teatro[l,c] == 1:

          print("Poltrona Liberada!!!")

          print(f"R${valor_ingre * (30/100)} foram devolvidos!!!")

          tamanho_teatro[l,c] = 0

          val_total = val_total - (valor_ingre * (30/100))

          ingre_reserv -= 1

        elif tamanho_teatro[l,c] == 2:

          print()

          print("Poltrona Liberada!!!")

          print(f"R${valor_ingre} foram devolvidos!!!")

          tamanho_teatro[l,c] = 0

          val_total = val_total - valor_ingre

          ingre_vend -= 1

        print()

      elif menu_teatro == 5:

        print()

        for k in range(len(tamanho_teatro)):

          print(tamanho_teatro[k])

        print()

      elif menu_teatro == 6:

        print()

        if ingre_vend > ((tamanho_espetaculo * (60/100)) + 1):

          print(f"""Espetáculo encerrado com sucesso!!!

Total Geral de Cadeiras: {tamanho_espetaculo}

Total de Cadeiras Vazias: {tamanho_espetaculo - (ingre_reserv + ingre_vend)}

Total de Cadeiras Reservadas: {ingre_reserv}

Total de Cadeiras Vendidas: {ingre_vend}

Total do Espetáculo em R$: {val_total}

Total não recebido em R$: {(ingre_reserv * (valor_ingre * (70/100))) + ((tamanho_espetaculo - (ingre_reserv + ingre_vend)) * valor_ingre)}

Total em reservas R$: {ingre_reserv * (valor_ingre * (30/100))}
                
""")

        print()

      elif menu_teatro == 7:

        print()

        print("Reiniciando o Menu do Espetáculo!!!")

        tamanho_teatro = []

        valor_ingre = 0.0

        ingre_vend = 0

        ingre_reserv = 0

        val_total = 0.0

        teatro_ativo = False

        print()        

      else:

        print()

        print("Programa encerrado com sucesso!!!")

        print()

        break


  else:

    print()

    print("Por favor escolha uma das opções listadas!!!")

    print()
