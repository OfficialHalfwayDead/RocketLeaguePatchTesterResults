#!/bin/zsh

cd ../1_53

echo "using diff tolerance ${1:-'0.01'}" >&2

for file in logs/*/*; do
  numdiff --absolute-tolerance=${1:-'0.01'} -s ',\n' $file ../1_52/$file 2>&1 | grep '+++'
done

