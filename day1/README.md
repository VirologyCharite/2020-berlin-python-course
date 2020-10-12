# Introduction to the shell
## Being fast in the shell pays off
Understand the shell as a one-line editor. There are lots of hotkeys to e.g. copy & paste(yank) and to navigate.
For example:  
`ctrl+a` - jump to beginning of line  
`ctrl+e` - jump to end of line  
`ctr+w` - delete one word  
`ctr+u` - clear to beginning of line  
`ctr+k` - clear to end of line  
`ctr+r` - reverse search  
`alt+f` - jump word forward  
`alt+b` - jump word backward  
`alt+.` - evoke previous argument
## List of shell programs
Use `man` to find out more about these programs.  
`echo`
`head`
`less`
`cat`
`cut`
`wc`
`tr`
`awk`
`sort`
`uniq`
`date`
`jobs`
`parallel`
`grep`
`which`
`type`
`vim`
`pwd`
`chmod`
`umask`

Each of these programs has three input/output streams: _standard input_ (stdin), _standard output_ (stdout), _standard error_ (stderr). Usually, the streams are connected to the terminal.

Cutting a file at the delimiter `:`, three different ways:  
`cut -f7 -d: < /etc/passwd`  (`<` opens the file)  
`cut -f7 -d: /etc/passwd`  (`cut` reads the file)  
`/etc/passwd | cut -f7 -d:` (starting two programs and piping)  

## A one line program
One can use bash's meta-character `|` to _pipe_ the standard output of one program into the standard input of the next program. Eg.:  
`cat /etc/passwd | tr : _ | head -n 5`  
`cat` reads the file `/etc/passwd` and passes the file content to `tr` which exchanges all `:` in the text to `_` of which only the 5 first lines (head) are shown.  

Word count of the last cell in a file:  
`cat /etc/passwd | tr : _ | awk -F: '{print $NF}' | sort | uniq -c | head -n 5`  

## Running a bash script
1. `vim silly` to make a file called silly (or use some other editor).
2. fill the file, eg.
```
for value in a b c
do
echo $value | wc -c
done
```
3. run the file via `bash silly`, or (better) make it executable:  
`ls -la` to see permissions of the files.  
`chmod u+x silly` to make it executable for the user.
4. add the hashbang to the first line of the silly file
`#!/bin/bash`.
5. Now you can run `./silly`
If you have the local directory at the beginning of the system path, you can just run `silly`. (To see the paths, do `echo $PATH`).

You can directly execute a python file just the same by e.g. using the hashbang `#! /bin/env python`, which uses your system's python.  
What python is your system using? - `which python`  
What python programs exist on your system? - `type -all python`
