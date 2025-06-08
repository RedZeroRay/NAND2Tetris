class Parser:
    def __init__(self, symbol_table):
        self.instructions = []
        self.instruction_type = None
        self.address = None
        self.computation = None
        self.jump = None
        self.symbol_table = symbol_table

    @staticmethod
    def _read_file(file):
        instructions = []
        with open(file, 'r') as f:
            for row in f:
                instructions.append(row)
        return instructions

    @staticmethod
    def _clean_instructions(instructions):
        clean_instructions = []
        for instruction in instructions:
            instruction = instruction.strip()
            if instruction[0:2] == '//':
                continue
            if len(instruction) == 0:
                continue
            clean_instructions.append(instruction)
        return clean_instructions

    @staticmethod
    def _parse_a_instruction(instruction):
        return instruction.strip('@')
    
    @staticmethod
    def _parse_c_instruction(instruction):
        if '=' not in instruction and ';' not in instruction:
            instruction = 'null=null;' + instruction
        elif '=' not in instruction:
            instruction = 'null=' + instruction
        elif ';' not in instruction:
            instruction = instruction + ';null'

        fields = instruction.replace('=',';').split(';')
        destination = fields[0]
        computation = fields[1]
        jump = fields[2]

        return destination, computation, jump
    
    def _process_pointers(self, instructions):
        clean_instructions = []
        index_offset = 0
        for index, instruction in enumerate(instructions):
            if instruction.startswith('('):
                symbol = instruction.replace('(','').replace(')','')
                self.symbol_table.add_symbol(symbol, index - index_offset)
                index_offset += 1
                continue
            if instruction.startswith('@') and not instruction.strip('@').isdigit():
                self.symbol_table.add_variable(instruction.strip('@'))
            clean_instructions.append(instruction)
        return clean_instructions
                

    def _process_variables(self, instructions):
        clean_instructions = []
        for instruction in instructions:
            if instruction.startswith("@"):
                instruction = '@' + str(self.symbol_table.table.get(instruction.strip('@'), instruction.strip('@')))
            clean_instructions.append(instruction)
        return clean_instructions
    
    def _process_symbols(self, instructions):
        instructions = self._process_pointers(instructions)
        instructions = self._process_variables(instructions)
        return instructions
            

    def _parse_instructions(self, instructions):

        instructions = self._clean_instructions(instructions)
        instructions = self._process_symbols(instructions)

        for instruction in instructions:

            if instruction.startswith('@'):
                self.instruction_type = 'A'
                self.address = instruction.strip('@')
                self.computation = None
                self. jump = None
            
            else:
                self.instruction_type = 'C'
                address, computation, jump = self._parse_c_instruction(instruction)
                self.address = address
                self.computation = computation
                self.jump = jump

            self.instructions.append((self.instruction_type, self.address, self.computation, self.jump))

    def parse(self, file):
        self.instructions = []
        file_instructions = self._read_file(file)
        self._parse_instructions(file_instructions)
        return self.instructions