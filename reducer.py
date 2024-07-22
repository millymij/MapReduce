#!/usr/bin/env python3
import sys

# Student ID: 2932358


def eprint(*args, **kwargs):
    print(args,file=sys.stderr,**kwargs)


current_genre = None
current_max_rating = 0
current_highest_rated_films = []
minVotes = 15


for line in sys.stdin:
    line = line.strip()
    genre, title, total_rating, total_count = line.split('\t')
    
    try:
        total_rating = float(total_rating)
        total_count = int(total_count)
    except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue
    
    if total_count < minVotes:
        continue

    avg_rating = total_rating / total_count
    
    # processing the same key
    if current_genre == genre:
        
        if avg_rating > current_max_rating:
            current_highest_rated_films = [(title, avg_rating)]
            # update max rating for that genre
            current_max_rating = avg_rating
        
        elif avg_rating == current_max_rating:
            # found another film with the same highest rating
            current_highest_rated_films.append((title, avg_rating))
    

    # processing a different key
    else:
         # current genre not none
        if current_genre:
            for film in current_highest_rated_films:
                print('%s\t%s\t%.1f' % (current_genre, film[0], film[1]))
        
        # clean up everything for new key
            current_highest_rated_films = []
            current_max_rating = 0
        current_genre = genre
    
if current_genre == genre:
    print('%s\t%s\t%.1f' % (current_genre, film[0], film[1]))