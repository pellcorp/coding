#!/bin/bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd -P)"

start='<html><body><pre>'
end='</pre></body></html>'

pushd $CURRENT_DIR > /dev/null
files=$(find . -name "*.py")
for file in $files; do
  dirname=$(dirname $file | sed 's/\.\///g')
  name=$(basename $file).html

  echo "Writing: docs/$dirname/$name"
  mkdir -p docs/$dirname

  echo $start > "docs/$dirname/$name"
  cat $file >> "docs/$dirname/$name"
  echo $end >> "docs/$dirname/$name"
done
