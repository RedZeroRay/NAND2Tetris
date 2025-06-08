from assembler import Assembler
from parser import Parser
from symbol_table import SymbolTable
import os

source_path = './06/input/'
output_path = './06/output/'

symbol_table = SymbolTable()
parser = Parser(symbol_table)
assembler = Assembler()

hack_code = []

for file in os.scandir(source_path):
    output = output_path + file.name.split('.')[0] + '.hack'

    instructions = parser.parse(file)
    hack_code = assembler.generate_code(instructions)

    with open(output, 'w') as o:
        for line in hack_code:
            o.write(f"{line}\n")