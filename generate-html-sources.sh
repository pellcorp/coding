#!/bin/bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd -P)"

pushd $CURRENT_DIR > /dev/null

find docs/python/ -name "*.py.html" -exec rm {} \;
find docs -name "index.html" -exec rm {} \;

dirs=$(find python -type d | sort)
for dir in $dirs; do
  mkdir -p docs/$dir
  echo "<html><body><ul>" > docs/$dir/index.html
  echo "<a href=\"..\">Back</a>" > docs/$dir/index.html

  files=$(find $dir -maxdepth 1 -type f | sort)
  for file in $files; do
    basename=$(basename $file)
    extension="${basename##*.}"
    if [ "$basename" != "index.html" ]; then
      if [ "$extension" = "py" ] || [ "$extension" = "bat" ]; then
        name=${basename}.html
        echo '<html><body><pre>' > docs/$dir/$name
        cat $file >> docs/$dir/$name
        echo '</pre></body></html>' >> docs/$dir/$name
        echo "<li><a href=\"$name\">$basename</a></li>" >> docs/$dir/index.html
      else
        echo "<li><a href=\"../../../python/$dir/$basename\">$basename</a></li>" >> docs/$dir/index.html
      fi
    fi
  done
done

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
