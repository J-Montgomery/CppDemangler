
class Demangler():
    def __init__(self, abi="itanium"):
        self.abi = abi

    def parse(self, symbol):
        print(symbol)
        if hasattr(self, 'parse_' + self.abi):
            return getattr(self, 'parse_' + self.abi)(symbol)
        else:
            raise Exception("ABI {} not implemented".format(self.abi))

    def parse_itanium(self, symbol):
        print("Parsing {symbol} with ABI {abi}".format(symbol=symbol, abi=self.abi))

        return ""

