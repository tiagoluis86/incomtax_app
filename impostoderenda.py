faixa1 = 0000.00
faixa2 = 2500.01
faixa3 = 3200.01
faixa4 = 4250.01
faixa5 = 5300.01


while True:
    salariobruto = float(input('Informe o salário: '))
    if faixa1 <= salariobruto < faixa2:
        imposto = 0
        salarioliquido = salariobruto - imposto
        print('O salário líquido é R$ {:.2f} e o imposto é de R$ {:.2f}'.format(salarioliquido, imposto))
    elif faixa2 <= salariobruto < faixa3:
        imposto = ((salariobruto - faixa2) * 0.075)
        salarioliquido = salariobruto - imposto
        print('O salário líquido é R$ {:.2f} e o imposto é de R$ {:.2f}'.format(salarioliquido, imposto))
    elif faixa3 <= salariobruto < faixa4:
        imposto = ((faixa3 - faixa2) * 0.075) + ((salariobruto - faixa3) * 0.15)
        salarioliquido = salariobruto - imposto
        print('O salário líquido é R$ {:.2f} e o imposto é de R$ {:.2f}'.format(salarioliquido, imposto))
    elif faixa4 <= salariobruto < faixa5:
        imposto = ((faixa3 - faixa2) * 0.075) + ((faixa4 - faixa3) * 0.15) + ((salariobruto - faixa4) * 0.225)
        salarioliquido = salariobruto - imposto
        print('O salário líquido é R$ {:.2f} e o imposto é de R$ {:.2f}'.format(salarioliquido, imposto))
    else:
        imposto = ((faixa3 - faixa2) * 0.075) + ((faixa4 - faixa3) * 0.15) + ((faixa5 - faixa4) * 0.225) + ((salariobruto - faixa5) * 0.275)
        salarioliquido = salariobruto - imposto
        print('O salário líquido é R$ {:.2f} e o imposto é de R$ {:.2f}'.format(salarioliquido, imposto))
    continuar = int(input("Deseja continuar?\n 1 - Sim\n 2 - Não"))
    if continuar == 2:
        break
