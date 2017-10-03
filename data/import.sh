mkdir lichess 

while read line; do wget -E -H --directory-prefix=lichess -k -p $line; done < urllist.txt