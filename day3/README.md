# awk
Filter for data extraction.

`awk 'pattern {actions}'`  
`awk '$1 == 1962 {print $1, $2}' < medals.txt`  
The `$` addresses columns. `$0` is the whole line, `$1` is the first column. One column is separated from another column by any amount of whitespaces (or another specified delimter).  
The above prints columns 1 and 2 for all column-1-fields that equal 1962 in the `medals.txt` file.

# sed
Parses and transforms text.

`sed -e 's/Speed skating/Speed-skating/ < medals.txt'`  
Exchange string 'Speed skating' for 'Speed-skating'

# perl
High-level, general-purpose, interpreted, dynamic programming languages.

`perl -pi.bak -e 's/kating/nowing' models2.txt models3.txt`  
In-place editing.

# less
View (but not change) the contents of a text file.

`/` search mode  
`n` goto next match  
`N` goto previous match

`g` jump to top  
`G` jump to bottom  
`space` down one page   
`b` up one page  
`d` down half page  
`u` up half page  
`y` up one line  
`e` down one line

# GNU parallel
https://blogs.fluidinfo.com/terry/2017/08/05/do-stuff-on-things-in-parallel/

# scattered wisdom
* the power of brace expansions  
`filename.{1,2,3} -> filename.1 filename.2 filename.3`
* you can use `find` to find things.  
Flags:   
find file: `-type f`   
find directory: `-type d`  
find name: `-name '*.txt'`  
execute command: `-exec`  
Run a command on a set of found filenames:
Use `xargs`
* use `\` to escape meta-characters of the shell. E.g. `\;`.
