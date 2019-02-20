#!/usr/bin/env python3
'''
Made by Paul Ketner for the adventofcode 2018 day 3
'''
import re


def matrix_duplicate_finder():
    '''
    Build a matrix of the defined areas, and find the number of squares duplicated
    '''
    #Build the fabric claims matrix
    fabric_area = {}
    fabric_claims_file = open('fabric_claims', 'r')
    for fabric_claim in fabric_claims_file:
        #Convert the input lines into vars
        match = re.search('^#\d+ @ (\d+),(\d+): (\d+)x(\d+)', fabric_claim)
        if match:
            start_column = int(match.group(1))
            start_row = int(match.group(2))
            end_column = start_column + int(match.group(3))
            end_row = start_row + int(match.group(4))
        #Build the matrix
        for column in range(start_column, end_column):
            if not column in fabric_area:
                fabric_area[column] = {}
            for row in range(start_row, end_row):
                if not row in fabric_area[column]:
                    fabric_area[column][row] = 1
                else:
                    fabric_area[column][row] += 1
    #Find the number of squares with duplicate claims
    contested_area = 0
    for column in fabric_area:
        for row in fabric_area[column]:
            if fabric_area[column][row] > 1:
                contested_area += 1
    print('Duplicate claims exist in %s squares' % contested_area)


if __name__ == '__main__':
    matrix_duplicate_finder()
