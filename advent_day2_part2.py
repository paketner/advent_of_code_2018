#!/usr/bin/env python3
'''
Made by Paul Ketner for the adventofcode 2018 day 2
'''
import collections


def mostly_match_finder():
    '''
    The input file has two lines that have a difference of one letter in the same postion.
      Find the matching letters of those lines
    '''
    box_ids_list = []
    box_ids_file = open('box_ids', 'r')
    for box_id in box_ids_file:
        for compare_box_id in box_ids_list:
            diff_counter = 0
            same_letters = ''
            for i in range(0, len(box_id)):
                if box_id[i] == compare_box_id[i]:
                    same_letters += box_id[i]
                else:
                    diff_counter += 1
                if diff_counter > 1:
                    break
            if diff_counter == 1:
                print(same_letters)
        box_ids_list.append(box_id)


if __name__ == '__main__':
    mostly_match_finder()
