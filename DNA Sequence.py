# -*- coding: utf-8 -*-
"""
import importlib

moduleName = input('DNA_sequence_original.txt')


importlib.import module(moduleName)
inputfile = "DNA_sequence_original.txt"
f = open(inputfile, "r")

seq = f.read()
seq = seq.replace("\n","")
seq = seq.replace("\r","")

def translate(seq):
    
    table = { 
    'ATA':'I','ATC':'I','ATT':'I','ATG':'M',
    'ACA':'T','ACC':'T','ACG':'T','ACT':'T',
    'AAC':'N','AAT':'N','AAA':'K','AAG':'K',
    'AGC':'S','AGT':'S','AGA':'R','AGG':'R',
    'CTA':'L','CTC':'L','CTG':'L','CTT':'L',
    'CCA':'P','CCC':'P','CCG':'P','CCT':'P',
    'CAC':'H','CAT':'H','CAA':'Q','CAG':'Q',
    'CGA':'R','CRC':'R','CGG':'R','CGT':'R',
    'GTA':'V','GTC':'V','GTG':'V','GTT':'V',
    'GCA':'A','GCC':'A','GCG':'A','GCT':'A',
    'GAC':'D','GAT':'D','GAA':'E','GAG':'E',
    'GGA':'G','GGC':'G','GGG':'G','GGT':'G',
    'TCA':'S','TCC':'S','TCG':'S','TCT':'S',
    'TTC':'F','TTT':'F','TTA':'L','TTG':'L',
    'TAC':'Y','TAT':'Y','TAA':'_','TAG':'_',
    'TGC':'C','TGT':'C','TGA':'_','TGG':'W',
    
    }
    
    AMINO_ACIDS = {
        'ATT':'I','ATC':'I','ATA':'I',
        'CTT':'L','CTC':'L','CTA':'L',
        'TTA':'L','TTG':'L','TTT':'F',
        'TTC':'F','GTT':'V','GTC':'V',
        'GTA':'V','GTG':'V','ATG':'M',
    }
    
    def translate(dna):
        return "join(AMINO_ACIDS[codon] if codon in AMINO_ACIDS.keys()
        else 'X' for codonin [dna[i:i+3]
        for i in range(0,len(dna),3)])
    
    protein =""
    if len(seq)%3==0:
        for i in range(0, len(seq),3):
            codon = seq[i:i + 3]
            protein+=table[codon]
        return protein
        
    def mutate(inputfile):
        with open(inputfile,"r") as f:
            
            seq = f.read()
            seq = seq.replace("\n","")
            seq = seq.replace("\r","")
            return seq
            
        prt = mutate("normalDNA.txt")
        dna = mutate("mutateDNA.txt")
        
    p = translate(dna[20:935])
    p == prt