# These are the notes from the course...

## Proposed schedule going forward

### Tuesday Oct 13

`Morning`: Python: conda, matplotlib (maybe plot.ly), histogram.py (see example use below)

`Afternoon`: Shell basics (see below) and some random hacks

### Wednesday Oct 14

`Morning`: Shell: working with git, `less`, [GNU Parallel](https://www.gnu.org/software/parallel/)
    ([Terry talk](http://antigenic-cartography.org/terry/do-stuff-on-things-in-parallel.html)).

`Afternoon`: Python with Udo: pandas  

* [Link](https://github.com/jvns/pandas-cookbook) to github repo  
* [Link](https://mybinder.org/v2/gh/jvns/pandas-cookbook/master) to online notebook


### Thursday Oct 15

`Morning`: Shell: working with make. Little languages: awk, perl, sed. More random hacks.

`Afternoon`: Python with Leonie: Jupyter notebooks

### Friday Oct 16

`Morning`: Python scripts. argparse (tidy-columns.py), decorators, generators.

`Afternoon`: Python classes [2017 notes](https://github.com/VirologyCharite/berlin-python-course-2017/blob/master/classes/),
    dark matter



## Things we could learn about

### Shell

#### Basics

* Shell control flow
* Shell metacharacters: `? [] * < > |` etc
* Redirection
* Affecting the current shell environment
* Using `$(...)`
* Putting scripts into your `~/bin`.
* Regular expressions
* Command exit status
* Special variables
* How to be careful in shell scripting
* `/dev/null`
* `/tmp`

#### Random hacks

* `perl -pi.bak -e 's/xxx/yyy/'`
* Converting whitespace to newlines
* Finding weird characters using `tr -d -c ...`.
* Convert space separated into TAB separated: `cat output/LC480-or-T2/category-stats.txt | tr -s ' ' \t`
* Looking for negative, positive, negative in JSON output for Guido:
  `egrep -A 2 '0\.0,$' output/LC480-or-T2/sa-min-3.json | egrep '0\.0$'`
* Copying latest papers to print onto my USB drive: `cp -i $(grep -A 2000 'To print' papers.md | grep papers | tr '/),' ' ' | awk '{print $NF}') /media/terry/TERRY-KEYRI/vl/`
* histogram input `tail -n +3 < /tmp/out-$days.txt | cut -f3 -d\ | histogram.py --bins 46 --x 'Error in estimate (days)' --title 'Optimization error histogram' --save /tmp/hist.png --noShow`
* Are there any duplicated lines?
* Find SARS-2 people with Ct value greater than some X

#### Other

* ssh to a server, then running `tmux`.
* Most useful args to different common commands.
* Random stuff from Terry's bin
    * [SpreadD3 hack](https://github.com/VirologyCharite/convert-spread3)
    * td, yd, tm (useful with `$(...)`).
    * lat, unt.
    * What are the file types in my bin?
    * Tiny `to-papers` script I just wrote.
    * eks / uneks
* [Github](https://github.com) and git!

### Python

* Jupyter notebooks
* Bioinfomatics tools
* dark matter tools
* PYTHONPATH
* Conda
* Argparse
* BioPython
* Classes
* Decorators
* Generators
* Testing

## Shell utilities we like

* paste
* comm
* tr
* grep
* cut
* echo
* cat
* less
* awk
* sed
* perl
* test
* make
* tmux
