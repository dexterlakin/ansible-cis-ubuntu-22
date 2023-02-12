#!/usr/bin/env bash

function create_toc_txt() {
  while read -r line; do
    #The awk script reads each line of the input file and splits it into fields, using whitespace as the default field separator.
    # The script then specifies the field separators as "." using the FS variable.
    # The script then uses the built-in sub function to remove all characters after the 40th character in each field.
    # Finally, the script outputs the resulting modified string using the print statement.
    result=$(echo "$line" | awk '{gsub(/[.]{3,}.*/,""); print $0}' | tr ' ' '_')

    # print the modified line
    echo "$result" >>toc2.txt

  done <toc.txt
}

# Loop through each line of the string
while read -r line; do
  # Extract the prefix by removing everything after the last dot
  prefix="${line%%.*}"
  echo "$prefix"
done <toc2.txt
