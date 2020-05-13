#!/usr/bin/python3

import sys
import argparse
import sequence_evolution.random_sequences as randoseq


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument('-n',
                        '--number',
                        action='store',
                        dest='num_sequences',
                        type=int,
                        required=True,
                        help='Number of sequences to generate')

    parser.add_argument('-l',
                        '--length',
                        action='store',
                        dest='length',
                        type=int,
                        required=True,
                        help='Length of sequences to generate')

    parser.add_argument('-t',
                        '--title',
                        action='store',
                        dest='title',
                        type=str,
                        default='Sequence',
                        help='Prefixed title of sequences')

    parser.add_argument('-o',
                        '--out-file',
                        action='store',
                        dest='out_file_name',
                        default='',
                        type=str,
                        help='File in which to save sequences. If not specified, defaults to stdout.')

    parser.add_argument('-c',
                        '--characters',
                        action='store',
                        dest='characters',
                        default='UAGC',
                        type=str,
                        help='Specify bases to make sequences')

    args = parser.parse_args(sys.argv[1:])

    sequences = randoseq.generate_sequences(args.num_sequences, args.length, args.characters)
    randoseq.write_sequences(sequences, args.title, args.out_file_name)

if __name__ == '__main__':
    main()

