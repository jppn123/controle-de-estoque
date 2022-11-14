import os, time
dici = {
    "the legends of zelda":[1986, "super nintendo, gameboy advanced", "ação e aventura", 56.20, 2], 
    "mario world":[1990, "super nintendo, gameboy advanced, wii", "jogo de plataforma", 60.00, 2], 
    "sonic the hedgehog":[1991, "Android, Mega Drive", "jogo de plataforma, corrida e aventura", 55.00, 2], 
    "donkey kong country":[1994, "super nintendo", "jogo de plataforma", 52.30, 2],
    "assassin's creed black flag":[2013, "pc, xbox one e 360, playstation 3 e 4, nintendo switch", "mundo aberto, jogo eletrônico de ação e aventura", 150.00, 2], 
    "dying light":[2015, "pc, playstation 4, xbox one", "survival horror", 89.90, 2],
    "sekiro: shadows die twice":[2019, "pc, playstation 4, xbox one", "RPG eletrônico, ação e aventura", 210.00, 2],
    "minecraft":[2011, "pc, xbox", "sandbox, sobrevivência", 130.00, 2],
    "no man's sky":[2016, "nintendo switch, playStation 4, xbox one", "aventura", 204.90, 2],
    "gta v":[2013, "pc, xbox one, playstation 4", "mundo aberto, tiro, ação", 70.00, 2]
}
dicisec = dict()
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

while True:
    listanomes = list()

    with open("jogos.txt", "r") as rw:
        nomes = rw.readlines()
        for nome in nomes:
            for x in nome:
                if x == " ":
                    break
            listanomes.append(nome.split(x)[0])  
            
            
    x = input("1-Ver lista de jogos\n2-Buscar um jogo\n3-Salvar um novo jogo\n4-Retirar um jogo\n0-Fechar o sistema\n")
    if x not in "12340":
        clear()
        print()
        print("Por favor, insira um valor correspondente a lista!")
        print()
    elif x == "1":
        clear()
        print("-=" * 30)
        print("jogos cadastrados: ")
        print()
        for x in range(len(listanomes)):
                print(listanomes[x].replace("-", " "))
        print("-=" * 30)
   
    elif x == "0":
        print("-=" * 30)
        print("\t\t   saindo!")
        print("-=" * 30)
        time.sleep(0.5)
        clear()
        break
    elif x == "3":
        clear()
        nome = input("digite o nome do jogo a ser cadastrado: ")
        nome = nome.replace(" ","-")
        if nome in listanomes:
            print("-=" * 30)
            print("jogo já cadastrado!")
            print("-=" * 30)
            time.sleep(1)
            clear()
        else:
            dici[nome] = [
                          nome,
                          int(input("digite o ano: ")),
                          input("digite a plataformas(separe assim: valor1, valor2): ").replace(", ", "-"),
                          input("digite o generos(separe assim: valor1, valor2): ").replace(", ", "-"),
                          float(input("digite o preço: ")),
                          int(input("digite a quantidade: (até 999 produtos)"))
                          ]
            if dici[nome][5] == 0 or dici[nome][5] > 999 or dici[nome][2].find(", ") != -1 or dici[nome][3].find(", ") != -1:
                print()
                print("algo deu errado, preencha novamente!")
                print()
            else:
                with open("dictjogos.txt", "a") as da:
                    da.write(str(dici[nome]))
                    da.write("\n")
                print()
                
                with open("jogos.txt", "a") as rs:
                    
                    rs.write(nome)
                    rs.write(" ")
                    rs.write(str(dici[nome][5]))                        
                    rs.write("\n")
                clear()
                   
    elif x == "4":
        clear()
        nome = input("digite o nome do jogo a ser retirado: ")
        nome = nome.replace(" ","-")
        if nome not in listanomes:
            print("-=" * 30)
            print("jogo não cadastrado!")
            print("-=" * 30)
            time.sleep(1)
            clear()
        elif nome in listanomes:
            hp = listanomes.index(nome)
            
            with open("jogos.txt", "r") as rs:
                hd = rs.readlines()
                 
                if hd[hp][-2].isdigit() == True and hd[hp][-3].isdigit() == True and hd[hp][-4].isdigit() == True:
                    prod = hd[hp][-4] + hd[hp][-3] + hd[hp][-2]
                    prod = int(prod)
                    prod -= 1
                elif hd[hp][-2].isdigit() == True and hd[hp][-3].isdigit() == True:
                    prod = hd[hp][-3] + hd[hp][-2]
                    prod = int(prod)
                    prod -= 1  
                elif hd[hp][-2].isdigit() == True:
                    prod = hd[hp][-2]
                    prod = int(prod)
                    prod -= 1 
                                            
                hd[hp] = str(nome + " ") + str(prod) + '\n'
                with open("jogos.txt", "w") as rw:
                    rw.writelines(hd)
                    if prod != 0:
                        print()
                        print("-=" * 30)
                        print(f'o jogo: {nome.replace("-"," ")} foi excluido!')
                        print(f'restam {prod} copias')
                        print("-=" * 30)
                        print()
                        time.sleep(1)
                        clear()                          
                if prod == 0:
                    with open("dictjogos.txt", "r") as rd:
                        if nome in listanomes:
                            value = listanomes.index(nome)
                        dicts = rd.readlines()
                        dicts[value] = ""
                        with open("dictjogos.txt", "w") as rw:
                            for line in dicts: 
                                rw.write(line)
                    with open("jogos.txt", "r") as rs:
                        hd = rs.readlines()                                          
                        with open("jogos.txt", "w") as rw:
                            for line in hd: 
                                for z in range(0, len(hd)):
                                    for x in range(1, len(hd)):
                                        if (hd[z] is hd[x]) == False: 
                                            if line.find("0") == -1:   
                                                                                        
                                                rw.write(line)
                                                listanomes.clear()
                                                break
                                    break       
                            with open("jogos.txt", "r") as rw:
                                hd = rw.readlines()
                                for nome in hd:
                                    for x in nome:
                                        if x == " ":
                                            break
                                        listanomes.append(nome.split(x)[0])  
                    clear()            
                    print("=" * 30)
                    print(f'o jogo: {nome.replace("-"," ")} foi retirado do sistema!')
                    print("=" * 30)
                    print()
                    time.sleep(1)
                    clear()
    elif x == "2":
        clear()
        listadicts = list()
        listadict = list()
        nome = input("digite o nome do jogo: ")
        nome = nome.replace(" ","-")
        if nome not in listanomes:
            print()
            print("-=" * 30)
            print("jogo não cadastrado")
            print("-=" * 30)
            print()
            time.sleep(1)
            clear()
        else:
            hp = listanomes.index(nome)
            with open("jogos.txt", "r") as rr:
                linhas = rr.readlines()
                if linhas[hp][-1] == "\n":
                    if linhas[hp][-2].isdigit() == True and linhas[hp][-3].isdigit() == True and linhas[hp][-4].isdigit() == True:
                        prod = linhas[hp][-4] + linhas[hp][-3] + linhas[hp][-2]
                    elif linhas[hp][-2].isdigit() == True and linhas[hp][-3].isdigit() == True:
                        prod = linhas[hp][-3] + linhas[hp][-2]
                    elif linhas[hp][-2].isdigit() == True:
                        prod = linhas[hp][-2]
                with open("dictjogos.txt", "r") as rd:
                    dicts = rd.readlines()
                    val = listanomes.index(nome)    
                    for x in dicts:
                        if dicts.index(x) == val:
                            x = x.strip("\n")
                            x = x.strip("[]")
                            listadicts.append(x.split("[]"))                  
                            listadict.append(listadicts[0][0].split(", "))                 
                            print("-=" * 30)
                            print("\t", nome.upper().replace("-", " "))
                            print("ano: ", listadict[0][1])
                            print("plataformas: ", listadict[0][2].replace("-", ", ").replace("'", ''))
                            print("genero: ", listadict[0][3].replace("-", ", ").replace("'", ''))
                            print("preço: ", listadict[0][4], "reais")
                            print("estoque: ", prod, "jogos")
                            print("-=" * 30)   
                            break       