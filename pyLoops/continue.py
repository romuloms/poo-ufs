while True:
    username = input("username: ")
    if username != "neo":
        print("Desconhecido")
        continue
    senha = input("senha: ")
    if senha == "1234":
        print("bem-vindo, {}".format(username))
        break