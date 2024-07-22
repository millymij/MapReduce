## Movie Recommendation System with Hadoop Map/Reduce (2023)

This project implements a Hadoop-based MapReduce solution (using Python) to identify the highest-rated film for a specific genre within a specified year range.

### Approach
Example implementation of a Hadoop based Map/Reduce solution that in a single run extracts the
highest ranked films for a given genre of movie filtered on the listed years in the 'years.txt' file. The code
should use data stored on HDFS. 
This solution has been implemented in a standard Python map/reduce streaming form.

### Project Structure
* mapper.py: Contains the mapper logic for processing input data, parsing lines, filtering by genre and year, and emitting key-value pairs.
* combiner.py: (Optional) Implements the combiner logic for local aggregation of ratings and counts.
* reducer.py: Contains the reducer logic for calculating average ratings and identifying the highest-rated film per genre.
* ratings.txt: (Sample input data) Contains movie data in the specified format (to replace with HDFS path).
* years.txt: (Required on HDFS) Contains a list of years to filter the data.
* results.txt: (Output file) Stores the results of the MapReduce job.

### Dependencies
* Python 3.11.9
* Hadoop
