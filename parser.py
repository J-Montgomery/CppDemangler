import argparse
from demangle import Demangler


def main():
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument('-i', '--input', help='input filename', default='in.perf')
    cli_parser.add_argument('-o', '--output', help='Output filename', default='out.stack')
    cli_parser.add_argument('-c', '--collect', help='Sum run-times of all identically named functions together, regardless of call stack order', action='store_true')
    cli_parser.add_argument('-p', '--print-times', help='Print the total run-times taken by all identically named functions', action='store_true')
    cli_parser.add_argument('-d', '--demangle-names', help='Demangle c++ symbol names', action='store_true')
    ns_args = cli_parser.parse_args()
    print(ns_args)
    d = Demangler()
    print(d.parse("_ZGR1bIvE1_"))
    return

if __name__ == "__main__":
    main()