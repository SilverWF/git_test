#!bin/bash

ch_size(){
    local path="$1"
    local size=$(du -h -s "$path" 2>/dev/null | cut -f1)
    echo $size
}

dirc=$(pwd)
echo "Список файлов в директории " $dirc

fils=$(ls -A)

for fil in $fils; do
    size=$(ch_size "$fil")
    echo -e "$size\t$fil"
done | sort -rh -k1,1

