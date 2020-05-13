#!/usr/bin/env python

#This makes many random sequences given  the number of sequences to make and
#the length of the sequences.

import random
import sys
import typing

def write_sequences(sequences: iter, title: str, out_file_name: str='') -> None:
    '''
    Writes the iter `sequences` to `out_file_name`. Prefixes each sequences
    with "> `title`_`i`" where i is index of sequence. If `out_file_name` is
    an empty string, will redirect to stdout.
    '''
    def writer():
        if out_file_name == '':
            out_file = sys.stdout
        else:
            out_file = open(out_file_name, 'w')
        return out_file

    with writer() as f:
      for i, sequence in enumerate(sequences):
          write_title = '> {0}_{1}\n'.format(title, i)
          write_sequence = '{0}\n'.format(sequence)

          f.write(write_title)
          f.write(write_sequence)

def generate_sequences(num_sequences: int, length: int, bases: str) -> typing.Generator[str, None, None]:
    '''
    Generates `num_sequences` sequences of length `length` from
    characters `bases`.
    '''
    sequences = []
    for i in range(num_sequences):
        sequence = generate_sequence(length, bases)
        yield sequence

def generate_sequence(length: int, bases: str) -> str:
    '''
    Returns 1 random sequence of length `length` from
    characters `bases`.
    '''
    sequence = ''
    for i in range(length):
        new_base = random.randint(0, 3)
        sequence += bases[new_base]
    return sequence

