import json

agenda_contatos = []

def salvar_contato():
    try:
        with open("agenda_contatos.json", "w") as arquivo_contatos:
            json.dump(agenda_contatos, arquivo_contatos)
            print("Agenda de contatos salva com sucesso!")
    except:
        print("Erro ao salvar a agenda de contatos.")

def carregar_contatos():
    try:
        with open("agenda_contatos.json", "r") as arquivo_contatos:
            agenda_contatos = json.load(arquivo_contatos)
            return agenda_contatos
    except:
        print("Erro ao carregar a agenda de contatos, iniciando uma nova agenda.")
        return []

def adicionar_contato():
    try:
        input_nome_contato = input("Digite o nome do contato: ")
        input_telefone_contato = input("Digite o telefone do contato: ")
        input_email_contato = input("Digite o email do contato: ")

        contatos = {
            "nome": input_nome_contato,
            "telefone": input_telefone_contato,
            "email": input_email_contato
        }

        agenda_contatos.append(contatos)
        print(f"Contato '{contatos['nome']}', '{contatos['telefone']}', '{contatos['email']}' adicionado com sucesso!")

    except:
        print("Erro ao adicionar o contato.")

def listar_contatos():
    try:
        if not agenda_contatos:
            print("Nenhum contato na agenda.")
            return
        
        for contato in agenda_contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    except:
        print("Erro ao listar os contatos.")

def alterar_contato():
    try:
        input_email_contato = input("Digite o email do contato que deseja alterar: ")
        for contato in agenda_contatos:
            if contato['email'] == input_email_contato:
                input_novo_nome = input("Digite o novo nome do contato: ")
                input_novo_telefone = input("Digite o novo telefone do contato: ")
                input_novo_email = input("Digite o novo email do contato: ")

                contato['nome'] = input_novo_nome
                contato['telefone'] = input_novo_telefone
                contato['email'] = input_novo_email

                print(f"Contato '{input_email_contato}' alterado com sucesso!")
                return
            else:
                print(f"Contato '{input_email_contato}' não encontrado.")
    except:
        print("Erro ao alterar o contato.")

def buscar_contato():
    try:
        input_email_contato = input("Digite o email do contato que deseja buscar: ")
        for contato in agenda_contatos:
            if contato['email'] == input_email_contato:
                print(f"Contato encontrado: Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
                return
        print(f"Contato '{input_email_contato}' não encontrado.")
    except:
        print("Erro ao buscar o contato.")

def excluir_contato():
    try:
        input_email_contato = input("Digite o email do contato que deseja excluir: ")
        for contato in agenda_contatos:
            if contato['email'] == input_email_contato:
                agenda_contatos.remove(contato)
                print(f"Contato '{input_email_contato}' excluído com sucesso!")
                return
            else:
                print(f"Contato '{input_email_contato}' não encontrado.")
    except:
        print("Erro ao excluir o contato.")

agenda_contatos = carregar_contatos()

while True:
    try:
        print("|-------------------------|")
        print("| Agenda de Contatos      |")
        print("|-------------------------|")
        print("| 1. Adicionar Contato    |")
        print("| 2. Listar Contatos      |")
        print("| 3. Alterar Contato      |")
        print("| 4. Buscar Contato       |")
        print("| 5. Excluir Contato      |")
        print("| 6. Salvar e Sair        |")
        print("|-------------------------|\n")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_contato()
        elif escolha == "2":
            listar_contatos()
        elif escolha == "3":
            alterar_contato()
        elif escolha == "4":
            buscar_contato()
        elif escolha == "5":
            excluir_contato()
        elif escolha == "6":
            salvar_contato()
            break
        else:
            print("Opção inválida, por favor tente novamente.")
    except:
        print("Erro no sistema, por favor tente novamente.")