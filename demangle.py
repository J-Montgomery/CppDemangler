import subprocess

class ParseError(Exception):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

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
        process_results = subprocess.run("cpp_demangle {}".format(symbol), 
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if not process_results.returncode:
            return process_results.stdout.decode("utf-8").strip()
        else:
            raise ParseError("Parse failed: {}".format(process_results.stderr))
