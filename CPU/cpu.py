#Alex Shapovalov
#CS 5220
#Programming Assignment #1, Instruction Processing

class CPU:
    def __init__(self, pc, next_pc, memory, regs):
        pc = 0
        next_pc = 0
        memory = [0] * 65536
        regs = [0] * 16


class Instruction:
    def __init__(self, opcode, Rd, Rs1, Rs2, immed):
        opcode = 0
        Rd = 0
        Rs1 = 0
        Rs2 = 0
        immed = 0