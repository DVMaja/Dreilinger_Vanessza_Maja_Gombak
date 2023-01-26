def masodik():
    bekert_szamok = []

    for i in range(5):
        be_szam = int(input("Kérem adjon meg egy számot: "))
        bekert_szamok.append(be_szam)

    print(f"II/A, B, C:\n")
    for db in range(len(bekert_szamok) - 1):
        print(f"\t{bekert_szamok[db]}:", end="")
    print(bekert_szamok[len(bekert_szamok) - 1])

    def elso_idos():
        index = 0
        sorszam = 0
        while (index < len(bekert_szamok) - 1) and not(bekert_szamok[index] > 70):
            index += 1
        return index

    def konzolra_ir(indexe):
        print("II/D, E:")
        print(f"\tElső idős ember korának helye a listában: {indexe}")

    def fajl_ir(indexe):
        ki_fajl = open("oreg.txt", "w", encoding="utf-8")
        ki_fajl.write(f"II/F:\n\tElső idős ember korának helye a listában: {indexe}")
        ki_fajl.close()

    indexe = elso_idos()
    konzolra_ir(indexe)
    fajl_ir(indexe)
