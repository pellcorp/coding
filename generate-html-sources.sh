#!/bin/bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd -P)"

pushd $CURRENT_DIR > /dev/null

find docs -name "*.py.html" -exec rm {} \;
find docs -name "index.html" -exec rm {} \;

files=$(find . -name "*.py" | sort)
for file in $files; do
  dirname=$(dirname $file | sed 's/\.\///g')
  basename=$(basename $file)
  name=${basename}.html

  mkdir -p docs/$dirname
  echo '<html><body><pre>' > "docs/$dirname/$name"
  cat $file >> "docs/$dirname/$name"
  echo '</pre></body></html>' >> "docs/$dirname/$name"

  echo "<li><a href=\"$name\">$basename</a></li>" >> docs/$dirname/index.html
done

pushd docs/python > /dev/null
dirs=$(find . -name "index.html" -exec dirname {} \; | sort | uniq)

echo "<html><body><ul>" > index.html
echo "<a href=\"..\">Back</a>" > index.html
for dir in $dirs; do
  echo "<html><body>" > $dir/index.html
  echo "<a href=\"..\">Back</a>" >> $dir/index.html
  echo "<ul>" >> $dir/index.html
  files=$(find $dir -type f | sort)
  for file in $files; do
    if [ "$(basename $file)" != "index.html" ]; then
      echo "<li><a href=\"$(basename $file)\">$(basename $file .html)</a></li>" >> $dir/index.html
    fi
  done

  # now write the other files
  files=$(find ../../python/$dir -type f)
  for file in $files; do
    extension="${file##*.}"
    if [ "$extension" != "py" ]; then
      echo "<li><a href=\"../../../python/$dir/$(basename $file)\">$(basename $file)</a></li>" >> $dir/index.html
    fi
  done

  echo "</ul></body></html>" >> $dir/index.html

  echo "<li><a href=\"$dir\">$(basename $dir)</a></li>" >> index.html
done

files=$(find . -maxdepth 1 -type f | sort)
for file in $files; do
  extension="${file##*.}"
  if [ "$(basename $file)" != "index.html" ] && [ "$extension" != "py" ]; then
    echo "<li><a href=\"$(basename $file)\">$(basename $file .html)</a></li>" >> index.html
  fi
done
echo "</ul></body></html>" >> index.html
popd > /dev/null

files=()
while IFS=  read -r -d $'\0'; do
    files+=("$REPLY")
done < <(find docs -name "*.pdf" -print0)

echo "<html><body>" > docs/index.html

echo "<a href=\"..\">Back</a>" >> docs/index.html
echo "<ul>" >> docs/index.html
echo "<li><a href=\"python\">python</a></li>" >> docs/index.html

for file in "${files[@]}"; do
  basename=$(basename "$file")
  echo "<li><a href=\"$basename\">$basename</a></li>" >> docs/index.html
done
echo "</ul></body></html>" >> docs/index.html

echo "<html><body><ul>" > index.html
echo "<li><a href=\"docs\">docs</a></li>" >> index.html
echo "</ul></body></html>" >> index.html
