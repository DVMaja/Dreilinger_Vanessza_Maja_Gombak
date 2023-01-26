class Gomba:
    def __init__(self, sor: str):
        tisztitott = sor.strip()
        szetszedett = tisztitott.split("@")

        self.gomba_neve = szetszedett[0]
        self.nemzetiseg = szetszedett[1]
        self.evszak = szetszedett[2]

    def __str__(self):
        return f"A gomba neve: {self.gomba_neve}, nemzetisége: {self.nemzetiseg}, évszaka: {self.evszak}"
