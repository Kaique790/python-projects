nota1 = float(input("Digite a primeira nota do(a) aluno(a): "))
nota2 = float(input("Digite a segunda do(a) aluno(a): "))
nota3 = float(input("Digite a terceira do(a) aluno(a): "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f"O(a) aluno(a) foi aprovado(a) com média {media:.1f}!")
else:
    print(f"O(a) aluno(a) foi reprovado(a) com média {media:.1f}!")