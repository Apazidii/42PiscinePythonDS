#!/bin/sh


RES=hh_uniq_positions.csv
FILE=../ex03/hh_positions.csv
echo '"name","count"' > $RES

echo -n '"Junior",' >> $RES 
grep -o -i "Junior" $FILE | wc -l >> $RES

echo -n '"Middle",' >> $RES 
grep -o -i "Middle" $FILE | wc -l >> $RES

echo -n '"Senior",' >> $RES 
grep -o -i "Senior" $FILE | wc -l >> $RES

