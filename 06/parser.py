class Parser:
    def __init__(self):
        self.instruction_type = None
        self.address = None
        self.computation = None
        self.jump = None

    @staticmethod
    def _clean_instruction(row):
        if row[0:2] == '//':
            return None
        return row.strip()

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

    def parse_instruction(self, row):
        instruction = self._clean_instruction(row)
        if not instruction:
            self.instruction_type = None
            self.address = None
            self.computation = None
            self.jump = None
            return

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

    def parse(self, row):
        self.parse_instruction(row)
        return self.instruction_type, self.address, self.computation, self.jump
