lista = [10, 9, 8, 7, 7.5, 6.5, 9.5, 6, 5.5, 8.5]
media = 6
total_aprovado = 0
total_reprovado = 0
soma_notas = 0

for nota in lista:
    
    soma_notas += nota
     
    if nota >= media:
        print("aluno APROVADO!")
        total_aprovado +=1
        
    else:
        print("aluno REPROVADO!")
        total_reprovado += 1
        
media_simples = soma_notas / len(lista)

print(f"total de Aprovados foi {total_aprovado}")
print(f"total de Reprovados foi {total_reprovado}")
print(f"A media da turma foi {media_simples}")

