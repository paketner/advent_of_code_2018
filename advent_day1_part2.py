#!/usr/bin/env python3
'''
Made by Paul Ketner for the adventofcode 2018 day 1
'''

import re


def find_first_frequency_duplicate():
    '''
    Find the first time a frequency is duplicated
    '''
    total_frequency_change = 0
    found_duplicate_frequency = False
    frequency_changes_list = []
    frequency_changes_list.append(0)
    #10 should be enough loops.  Otherwise arbitrary counter is arbitrary
    for i in range(10):
        frequency_changes_file = open('frequency_changes1', 'r')
        for new_frequency_change in frequency_changes_file:
            match = re.search('^([-+])(\d+)', new_frequency_change)
            if match:
                #Subtract the minuses, add the pluses
                if match.group(1) == '-':
                    total_frequency_change -= int(match.group(2))
                else:
                    total_frequency_change += int(match.group(2))
                #Check for duplicate frequency total
                if total_frequency_change in frequency_changes_list:
                    found_duplicate_frequency = True
                    print('First duplicate frequency is %s' % (total_frequency_change))
                    return()
                #This list should be all unique numbers
                else:
                    frequency_changes_list.append(total_frequency_change)


if __name__ == '__main__':
    find_first_frequency_duplicate()
