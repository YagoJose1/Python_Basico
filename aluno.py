#Teste de idade para poder dirigir 

nome = str(input("Nome da pessoa: ") )
idade = int(input("Idade da pessoa: " ))
dif = 18 - idade

if (idade < 18) : 
  print(nome,", voce nao tem a idade adequada, volte daqui ", dif, " anos.")
else : 
  print(nome,", voce tem a idade adequada.")