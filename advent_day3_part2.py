#!/usr/bin/env python3
'''
Made by Paul Ketner for the adventofcode 2018 day 3
'''
import re


def find_uncontested_order_number():
    '''
    Find the order number(s) from the input file without contested areas of the matrix
    '''
    fabric_area = {}
    claims_list = []
    fabric_claims_file = open('fabric_claims', 'r')
    for fabric_claim in fabric_claims_file:
        #Split the lines into variables
        match = re.search('^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', fabric_claim)
        if match:
            claim_id = match.group(1)
            start_column = int(match.group(2))
            start_row = int(match.group(3))
            end_column = start_column + int(match.group(4))
            end_row = start_row + int(match.group(5))
        #Build the fabric claims matrix
        free_claim = True
        for column in range(start_column, end_column):
            if not column in fabric_area:
                fabric_area[column] = {}
            for row in range(start_row, end_row):
                if not row in fabric_area[column]:
                    fabric_area[column][row] = claim_id
                else:
                    if fabric_area[column][row] in claims_list:
                        claims_list.remove(fabric_area[column][row])
                    fabric_area[column][row] = 'X'
                    free_claim = False
        #Add all uncontested claims to a list
        if free_claim:
            claims_list.append(claim_id)
    print(claims_list)


if __name__ == '__main__':
    find_uncontested_order_number()
