#!/usr/bin/env python3

import sys
import string

# Student ID: 2932358

def eprint(*args, **kwargs):
    print(args,file=sys.stderr,**kwargs)


def get_years_from_file(file):
    years = {}
    try:
        with open(file, 'r') as f:
            for line in f:
                for year in line.strip().split(' '):
                    if year.isdigit():
                        # filling the dictionary with year and a value of 0 
                        years[year] = 0
    except FileNotFoundError:
        print("File not found.")
    return years


years_file = "years.txt"
years = get_years_from_file(years_file)


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading, trailing whitespace and force to lower case
    line = line.strip()
    #  Split up the line
    (uid,title,genres,year,rating) = line.split('\t')  

    # since in the dataset some films belong to multiple genres, split them
    # and include the film in all the genre categories it belongs to
    for genre in genres.split('|'):

        # discard film without year field
        if not year or not year.isdigit():
                continue
        
        # check if we are filtering by years. If the film's year is in the 'years' set, emit key-value pair.
        # key: genre
        # value: (title, rating, 1)
        
        if years and year in years:
            key = f"{genre}"
            print(f"{key}\t{title}\t{rating}\t1")

        # if 'years' is empty, we are not filtering by year, emit key-value pair regardless of the year.
        elif not years:
            key = f"{genre}"
            print(f"{key}\t{title}\t{rating}\t1")