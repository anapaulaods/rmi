import Pyro4

#proxy = Pyro4.Proxy("PYRO:obj_c5721e1e92534b98beca7795f21d6cd0@localhost:59480")

ns = Pyro4.locateNS()
uri = ns.lookup('obj')
server = Pyro4.Proxy(uri)

opcao = ''
while(opcao != '4'):
    print("===== Digite o que deseja fazer:=====\n1 - Inserir valor na Fila\n2 - Ver tamanho da Fila\n3 - Remover valor da Fila\n4 - Sair")
    opcao = input("\nopção: ")
    if (opcao == '1'):
        valor = input("> ")
        print (server.push(valor))
    if (opcao == '2'):
        print (server.size())
    if (opcao == '3'):
        print (server.pop())
    if (opcao == '4'):
        break