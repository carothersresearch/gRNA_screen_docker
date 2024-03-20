import sys
import os
#sys.path.append('/ViennaRNA-2.1.9/interfaces/Python/build/lib.macosx-10.6-x86_64-2.7/')
sys.path.append('/usr/local/lib/python2.7/site-packages/')
#sys.path.append('/gscratch/rna/compiled_binaries/ViennaRNA-2.2.9/interfaces/Python')
import RNA
import numpy as np
#from tqdm import tqdm

def tqdm(item):
    return item

def rev_comp(rna_seq):
    """Generates the reverse compliment of an RNA sequence."""

    seq = rna_seq[::-1]
    seq = seq.upper()
    seq = seq.replace("A", "y")
    seq = seq.replace("U", "A")
    seq = seq.replace("y", "U")
    seq = seq.replace("G", "Z")
    seq = seq.replace("C", "G")
    seq = seq.replace("Z", "C")
    return seq

def BP_content(structure):
    """
    Returns the fraction of bases in base-pairs within a given dotbracket
    secondary structure.
    """

    bp_count = 0.0
    for base in structure:
        if base != ".":
            bp_count += 1
    bp_content = bp_count / len(structure)
    return bp_content

def GC_content(sequence):
    """
    Returns the GC fraction of a given DNA or RNA sequence.
    """

    gc_count = 0.0
    sequence = sequence.upper()
    for base in sequence:
        if base == "G" or base == "C":
            gc_count += 1
    gc_content = gc_count / len(sequence)
    return gc_content

def RNAfold(seq, struct=None, temperature=37.0):
    if struct:
        RNA.cvar.fold_constrained = 1
    seq = seq.upper()
    RNA.cvar.temperature = temperature
    S,E = RNA.fold(seq, struct)
    RNA.cvar.fold_constrained = 0
    return float("{0:.2f}".format(E)),S

def RNAeval(seq, struct, temperature=37.0):
    seq = seq.upper()
    RNA.cvar.temperature = temperature
    return float("{0:.2f}".format(RNA.energy_of_struct(seq, struct)))

def RNAeval_dup(seq1, seq2, struct1, struct2, temperature=37.0):
    seq = ''.join([seq1, seq2])
    struct = struct1 + struct2
    seq = seq.upper()
    RNA.cvar.temperature = temperature
    RNA.cvar.cut_point = len(seq1) + 1
    energy = RNA.energy_of_struct(seq, struct)
    RNA.cvar.cut_point = -1
    return float("{0:.2f}".format(energy))


def RNAcofold(seq1, seq2, struct=None, temperature=37.0):
    seq = ''.join([seq1, seq2])
    seq = seq.upper()
    RNA.cvar.temperature = temperature
    RNA.cvar.cut_point = len(seq1) + 1
    if struct:
        struct_ref = ''.join([struct])
        RNA.cvar.fold_constrained = 1
    else:
        struct_ref = '.'*len(seq)
    energy = RNA.cofold(seq, struct_ref)
    RNA.cvar.fold_constrained = 0
    RNA.cvar.cut_point = -1
    return energy[1], energy[0][:len(seq1)], energy[0][len(seq1):]

'''def RNAduplex():
    '''
def RNAsubopt(seq, delta=1.0, temperature=37.0, sort=False, constraint=None, verbose=False):
    seq = seq.upper()
    RNA.cvar.temperature = temperature
    if sort:
        RNA.cvar.subopt_sorted = 1
    else:
        RNA.cvar.subopt_sorted = 0
    if constraint:
        RNA.cvar.fold_constrained = 1
    else:
        RNA.cvar.fold_constrained = 0
    subs = RNA.subopt(seq, constraint, int(100*delta), None)
    if not verbose:
        return [subs.get(num).structure for num in range(subs.size())]
    else:
        return [(subs.get(num).energy, subs.get(num).structure) for num in range(
        subs.size())]

def RNAdupstab(seq1, seq2, temperature=37.0):
    Edup, crap1, crap2 = RNAcofold(seq1, seq2, temperature=temperature)
    Eone, crap = RNAfold(seq1, temperature=temperature)
    Etwo, crap = RNAfold(seq2, temperature=temperature)
    return float("{0:.2f}".format(Edup - (Eone + Etwo)))

def BasePairDist(struct1, struct2):
    return RNA.bp_distance(struct1, struct2)

def findpath(seq, struct1, struct2, max_look=10000, multi=5, verbose=False, temperature=37.0):
    seq = seq.upper()
    RNA.cvar.temperature = temperature
    start = RNAeval(seq, struct1, temperature=temperature)
    lookahead = 1
    fsaddle = 0
    while (lookahead <= max_look):
        saddle = RNA.find_saddle(seq, struct1, struct2, lookahead)/100.0
        lookahead *= multi
        if fsaddle == saddle:
            break
    barrier = float("{0:.2f}".format(saddle - start))
    if verbose:
        path = RNA.get_path(seq, struct1, struct2, max_look)
        steps = [(path.get(l).s,path.get(l).en) for l in range(path.size())]
        return barrier, steps
    else:
        return barrier

def local_barriers(sequence, ref=None, gap=4.2,verbose=False, threshold=False, constraint=None, reverse=False):
    subs = RNAsubopt(sequence, delta=gap, sort=verbose, constraint=constraint, verbose=True)
    if not ref:
        ref =  RNAfold(sequence)[1]
    if reverse:
        bars = [findpath(sequence, ref, sub[1]) for sub in tqdm(subs)]
    else:
        bars = [findpath(sequence, sub[1], ref) for sub in subs]
    if threshold:
        active = 1.
        pf = pf_stab(sequence)[0]
        for bar, sub in zip(bars, subs):
            if bar > threshold:
                active -= pf_frac(sub[0], pf)
        return active

    elif reverse:
        if verbose:
            return min(bars), [(struct, barrier) for struct, barrier in zip(subs,bars)]
        return min(bars)
    else:
        if verbose:
            return max(bars), [(struct, barrier) for struct, barrier in zip(subs,bars)]
        return max(bars)

def pf_stab(seq, struct=None, temperature=37.0):
    if struct:
        RNA.cvar.fold_constrained = 1
    seq = seq.upper()
    RNA.cvar.temperature = temperature
    S,E = RNA.pf_fold(seq, struct)
    RNA.cvar.fold_constrained = 0
    return E,S

def pf_frac(correct_FE, ensemble_FE, temperature=37.0):
    kT = (temperature+273.15)*1.98717/1000.
    return np.exp(-(correct_FE - ensemble_FE)/kT)


"""
still need to add wrapper functions for inverse folding, centroid structure
identification.
"""

