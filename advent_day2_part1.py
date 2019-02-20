#!/usr/bin/env python3
'''
Made by Paul Ketner for the adventofcode 2018 day 2
'''
import collections


def generate_checksum():
    '''
    Generate the checksum of all lines in a file by finding all lines with double and triple letters,
      then multiplying those totals together
    '''
    total_doubles = 0
    total_triples = 0
    box_ids_file = open('box_ids', 'r')
    for box_id in box_ids_file:
        (box_doubles, box_triples) = parse_box_id(box_id)
        if box_doubles:
            total_doubles += 1
        if box_triples:
            total_triples += 1
    total_checksum = total_doubles * total_triples
    print('Total checksum is %s' % total_checksum)


def parse_box_id(box_id):
    '''
    Determine if there are double and / or triple letter entries in the supplied string

    Args:
      box_id (str) - random(ish) string of letters

    Returns:
      double_letter (bool) - True if there are exactly two of any same letter found
      triple_letter (bool) - True if there are exaclty three of any same letter found
    '''
    counter = collections.Counter(list(box_id))
    double_letter = False
    triple_letter = False
    for key in counter:
        if counter[key] == 2:
            double_letter = True
        if counter[key] == 3:
            triple_letter = True
    return(double_letter, triple_letter)
            

if __name__ == '__main__':
    generate_checksum()
