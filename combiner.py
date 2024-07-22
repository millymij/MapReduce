#!/usr/bin/env python3

import sys
import string

# Student ID: 2932358


def eprint(*args, **kwargs):
    print(args,file=sys.stderr,**kwargs)


aggregation = {}

# process lines from mapper output
for line in sys.stdin:
    genre, title, rating, count = line.strip().split('\t')
    rating = float(rating)
    count = int(count)
    
    key = (genre, title)
    # eprint(currentKey)

    if key not in aggregation:
        # Initialize the dictionary entry for this key
        aggregation[key] = {'tot_rating': 0, 'tot_count': 0}

    aggregation[key]['tot_rating'] += rating
    aggregation[key]['tot_count'] += count



# output: genre, title, tot_rating, tot_count
for (genre, title), film_info in aggregation.items():
    print(f"{genre}\t{title}\t{film_info['tot_rating']}\t{film_info['tot_count']}")
    # eprint(film_info['tot_count'])