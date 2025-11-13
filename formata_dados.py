# Solicita os dados do usuário
nome = input("Digite seu nome: ")
endereco = input("Digite seu endereço: ")
contato = input("Digite seu contato (telefone ou e-mail): ")
objetivos = input("Digite seus objetivos: ")
grau_escolar = input("Digite seu grau escolar: ")
cursos = input("Digite seus cursos: ")

# Coleta as 5 hard skills
hardskills = []
print("\nDigite suas 5 hard skills:")
for i in range(1, 6):
    skill = input(f"Hard skill {i}: ")
    hardskills.append(skill)

# Coleta as 5 soft skills
softskills = []
print("\nDigite suas 5 soft skills:")
for i in range(1, 6):
    skill = input(f"Soft skill {i}: ")
    softskills.append(skill)

# Monta a linha formatada no padrão solicitado
linha_config = (
    f"nome{{{nome}}}, "
    f"endereço{{{endereco}}}, "
    f"contato{{{contato}}}, "
    f"objetivos{{{objetivos}}}, "
    f"grau_escolar{{{grau_escolar}}}, "
    f"cursos{{{cursos}}}, "
    f"hardskills{{{', '.join(hardskills)}}}, "
    f"softskills{{{', '.join(softskills)}}}"
)

# Exibe a linha formatada
print("\n--- Linha de Configuração ---")
print(linha_config)
