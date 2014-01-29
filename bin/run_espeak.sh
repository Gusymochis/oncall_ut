#!/bin/bash

rm final.mp3
espeak $1 --stdout | ffmpeg -i - -ar 44100 -ac 2 -ab 192k -f mp3 final.mp3
