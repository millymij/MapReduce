hadoop jar /home/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-files mapper.py,combiner.py,reducer.py,years.txt \
-mapper mapper.py \
-combiner combiner.py \
-reducer reducer.py \
-input /user/caa00106/filmcount/ratings.txt \
-output /user/caa00106/filmcount/results