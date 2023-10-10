MI = 0b1000000000000000
RI = 0b0100000000000000
RO = 0b0010000000000000
AI = 0b0001000000000000
AO = 0b0000100000000000
EO = 0b0000010000000000
_ = 0b0000001000000000
_ = 0b0000000100000000
II = 0b0000000010000000
IO = 0b0000000001000000
BI = 0b0000000000100000
BO = 0b0000000000010000
CS = 0b0000000000001000
CI = 0b0000000000000100
CO = 0b0000000000000010

EEPRON = [
    [0,     0,     0,     0,     0, 0, 0, 0], # NOP
    [CS,    II,    IO|BI, EO|AI, 0, 0, 0, 0], # INC
    [CS,    II,    IO|BI, EO|AI, 0, 0, 0, 0], # DEC
    [IO|MI, RO|BI, EO|AI, 0,     0, 0, 0, 0], # ADD
    [IO|MI, RO|BI, EO|AI, 0,     0, 0, 0, 0], # SUB
    [IO|BI, EO|AI, 0,     0,     0, 0, 0, 0], # ASH
    [IO|MI, RO|BI, EO|AI, 0,     0, 0, 0, 0], # AND
    [IO|MI, RO|BI, EO|AI, 0,     0, 0, 0, 0], # OR
    [IO|MI, RO|BI, EO|AI, 0,     0, 0, 0, 0], # XOR
    [IO|MI, RO|BI, EO|AI, 0,     0, 0, 0, 0], # EQL
    [IO|MI, RO|BI, EO|AI, 0,     0, 0, 0, 0], # GRT
    [IO|MI, RO|AI, 0,     0,     0, 0, 0, 0], # LOAD
    [IO|MI, RO|BI, AO|RI, BO|AI, 0, 0, 0, 0], # SWP
    [CS,    II,    IO|CI, 0,     0, 0, 0, 0], # JMP
    [AI,    0,     0,     0,     0, 0, 0, 0], # CLR
    [IO|MI, AO|RI, 0,     0,     0, 0, 0, 0], # COPY
    ]
