from assembler import Assembler
from parser import Parser
import os

source_path = './input/'
output_path = './output/'

parser = Parser()
assembler = Assembler()

for file in os.scandir(source_path):
    output = output_path + file.name.split('.')[0] + '.hack'

    instructions = []

    with open(file, 'r') as f:
        for row in f:
            instruction = parser.parse(row)
            if instruction[0]:
                binary = assembler.translate(instruction)
                instructions.append(binary)

    with open(output, 'w') as o:
        for line in instructions:
            o.write(f"{line}\n")