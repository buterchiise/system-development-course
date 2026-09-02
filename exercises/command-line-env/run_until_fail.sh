#!/usr/bin/env bash

count=0

while true; do
    count=$((count + 1))
    ./buggy.sh > stdout.log 2> stderr.log
    if [[ $? -ne 0 ]]; then
        echo "在第 $count 次运行后失败"
        echo "stdout:"
        cat stdout.log
        echo "stderr:"
        cat stderr.log
        break
    fi
done
