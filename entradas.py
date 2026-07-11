# nome_cliente = input("insira seu nome: ")
# idade_cliente = int(input("insira sua idade "))
# email_cliente = input("insira seu email ")
# idade_futura = 1 + idade_cliente

# print(f"O nome do cliente é {nome_cliente}. \nEle possui {idade_cliente} anos. \nO seu email é {email_cliente}. \nA idade do cliente, no ano que vem será {idade_futura} anos.")

# salario_funcionario = float(input("Digite o seu salário "))
# salario_com_decimo_terceiro = salario_funcionario * 2

# print(f"O salario com decimo terceiro é {salario_com_decimo_terceiro}")

valor_pizza = float(input("Digite o valor da pizza: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

valor_desconto = valor_pizza * (percentual_desconto / 100)
valor_final = valor_pizza - valor_desconto

print(f"O valor final da pizza com desconto é {valor_final}")