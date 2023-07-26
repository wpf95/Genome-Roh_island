less roh_island.pos | uniq -c | awk '{$1=$1/60;print}' | awk -v OFS='\t' '{print $2,$3,$1}' > roh_island_indicine
