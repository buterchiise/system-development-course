#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <csv_file>" >&2
    exit 1
fi
FILE="$1"
if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found" >&2
    exit 1
fi
awk -F',' 'NR > 1 && $4 >= 500 {count[$3]++} END {for (p in count) print count[p], p}' "$FILE" | sort -k1,1nr -k2,2 | head -n2 | awk '{print $2}'
awk -F',' 'NR > 1 {sum += $5; n++} END {printf "%.2f\n", sum/n}' "$FILE"
