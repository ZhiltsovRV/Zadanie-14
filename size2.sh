#!/bin/bash
echo "Вывод по 10 строк, для вывода следующих 10 строк нажмите пробел."
get_size()  {
    local path="$1"
    local size=$(du -sh "$path" 2>/dev/null | cut -f1)
    echo $size
}
for item in .* *; do
    if [[ "$item" == ".." ]]; then
<------>continue
    fi
    size=$(get_size "$item")
    #echo "$item"
    echo -e "$size\t$item"
done | sort  -hr -k1 | more -10