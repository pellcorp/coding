#!/bin/bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd -P)"

start='<html><body><pre>'
end='</pre></body></html>'

pushd $CURRENT_DIR > /dev/null

index_start='<html><body><ul>'
index_end='</ul></body></html>'

find docs -name "index.html" -exec rm {} \;

files=$(find . -name "*.py" | sort)
for file in $files; do
  dirname=$(dirname $file | sed 's/\.\///g')
  basename=$(basename $file)
  name=${basename}.html

  echo "Writing: docs/$dirname/$name"
  mkdir -p docs/$dirname

  echo $start > "docs/$dirname/$name"
  cat $file >> "docs/$dirname/$name"
  echo $end >> "docs/$dirname/$name"

  if [ ! -f docs/$dirname/index.html ]; then
    echo "$index_start" > docs/$dirname/index.html
  fi
  echo "<li><a href=\"$name\">$basename</a></li>" >> docs/$dirname/index.html
done

pushd docs/python > /dev/null
dirs=$(find . -name "index.html" -exec dirname {} \; | sort | uniq)

echo "$index_start" > index.html
for dir in $dirs; do
  echo "$index_end" >> $dir/index.html
  echo "<li><a href=\"$dir\">$(basename $dir)</a></li>" >> index.html
done
echo "$index_end" >> index.html
