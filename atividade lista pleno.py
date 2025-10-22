#Faça um algoritmo que receba uma lista de nomes [“Gabriel”,”Juliano”,”Anna”,”Marcos”] e conte a quantidade de nomes que tem a letra “a”. Mostre no terminal com uma mensagem clara e intuitiva
#Ainda com a lista do exercício acima, conte quantos nomes começam com a letra “A” e exiba no terminal uma mensagem 
#Crie uma lista numérica de 1 a 10, após isso percorra ela, e exiba cada um dos números elevado ao quadrado.



nomes = ["Gabriel" , "Juliano" , "Anna" , "Marcos"]
nomes_cmç_letra_a = sum(1 for nome in nomes if 'a' in nome.lower())
print (input(quantidade de nomes  que começam com a letra 'a':))