#!/usr/bin/env python3
'''
Made by Paul Ketner for the adventofcode 2018 day 1
'''

import re


def analize_frequency_changes():
    '''
    Starting from 0, add or subtract all the frequency changes from the source file
    '''
    total_frequency_change = 0
    frequency_changes_file = open('frequency_changes', 'r')
    for new_frequency_change in frequency_changes_file:
        #Split the frequency mod from the number
        match = re.search('^([-+])(\d+)', new_frequency_change)
        #*Should* always find a match
        if match:
            #Subtract negatives, add positives
            if match.group(1) == '-':
                total_frequency_change -= int(match.group(2))
            else:
                total_frequency_change += int(match.group(2))
    print('Total frequency change is %s' % (total_frequency_change))


if __name__ == '__main__':
    analize_frequency_changes()
