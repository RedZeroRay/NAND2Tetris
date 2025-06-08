class Assembler:
    def __init__(self):
        self.comp_table = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100",
            "A": "0110000",
            "!D": "0001101",
            "!A": "0110001",
            "-D": "0001111",
            "-A": "0110011",
            "D+1": "0011111",
            "A+1": "0110111",
            "D-1": "0001110",
            "A-1": "0110010",
            "D+A": "0000010",
            "D-A": "0010011",
            "A-D": "0000111",
            "D&A": "0000000",
            "D|A": "0010101",
            "M": "1110000",
            "!M": "1110001",
            "-M": "1110011",
            "M+1": "1110111",
            "M-1": "1110010",
            "D+M": "1000010",
            "D-M": "1010011",
            "M-D": "1000111",
            "D&M": "1000000",
            "D|M": "1010101"
            }
        
        self.dest_table = {
            "null": "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "ADM": "111"
        }

        self.jump_table = {
            "null": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111"
        }

    def _translate_a(self, instruction):
        integer = int(instruction[1])
        binary = format(integer, 'b').zfill(16)
        return binary

    def _translate_c(self, instruction):
        try:
            destination = self.dest_table.get(instruction[1])
            computation = self.comp_table.get(instruction[2])
            jump = self.jump_table.get(instruction[3])
            binary = '111' + computation + destination + jump
            return binary
        except Exception as e:
            print(instruction)
            print(e)

    def _translate(self, instruction):
        if instruction[0] == "A":
            return self._translate_a(instruction)
        else:
            return self._translate_c(instruction)

    def generate_code(self, instructions):
        hack_code = []
        for instruction in instructions:
            binary = self._translate(instruction)
            hack_code.append(binary)
        return hack_code
