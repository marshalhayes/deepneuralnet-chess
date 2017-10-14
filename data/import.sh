while read line; do wget $line -P "/home/marshal/dnn-chess-bucket/lichess-datasets"; done < urllist.txt
