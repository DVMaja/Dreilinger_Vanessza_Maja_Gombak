import Gomba


def harmadik():

    def gombak_szama():
        be_fajl = open("gombak.txt", "r", encoding="utf-8")
        # be_fajl.readline()

        adatok = be_fajl.readlines()
        index = 0

        while index < len(adatok):
            index += 1

        print(f"III/A, B:\n\tA gombák száma: {index}")

        be_fajl.close()

    ossz_gomba = gombak_szama()

    def papsapka():
        szamlalo = 0

        while szamlalo < ossz_gomba:
            # if Gomba.Gomba(nemzetiseg)[szamlalo] == "papsapka":
            pass


    ez_kell = "homoki papsapka"
    print(f"III/C:\n\tAz első papsapkagomba neve: {ez_kell}.")

    ez_is = "14"
    print(f"III/D:\n\tA tinóru gombák száma: {ez_is}.")




