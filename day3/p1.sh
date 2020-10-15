#!/bin/bash

for i in "$@"
do
    echo wc $i
done | parallel
