#!/bin/bash

# This is a shell script....

# echo "I got $# arguments"

case $# in
    1) echo I got one argument;;
    2) echo I got argument 1 = $1 arg 2 = $2;;
    *)
        for i in "$@"
        do
            case $i in
                *[aeiou]) echo oooooh ends in a vowel $i; exit 0;;
                ??) echo hey, a 2-character arg; exit 3;;
                *) echo arg: $i;;
            esac
        done
    ;;
esac

for file in *
do
    echo $file
done

function new()
{
    echo
    echo xxxxxxxxxxxxxxxxxxxxxxxx
    echo
}


new

x=4

if date | grep -q ' Oct '
then
    echo "It's October!"
else
    echo "It's NOT October!"
fi

new

if test -f flow.sh
then
    echo flow exists
fi

new

x=10

while [ $x -gt 0 ]
do
    echo $x
    # x=$(expr $x - 1)

    x=$((x - 1))
done


# Metachars
# | < > \ & $var [] ?



dir=/tmp/my-dir

if [ ! -d $dir ]
then
    mkdir $dir
fi

# Or....

test -d $dir || mkdir $dir
