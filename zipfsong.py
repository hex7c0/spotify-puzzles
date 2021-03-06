#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

'''
Input
The first line of input contains two integers n and m (1 ≤ n ≤ 50000, 1 ≤ m ≤ n), the number of songs on the album, and the number of songs to select. Then follow n lines. The i’th of these lines contains an integer fi and string si, where 0 ≤ fi ≤ 10^12 is the number of times the i’th song was listened to, and si is the name of the song. Each song name is at most 30 characters long and consists only of the characters ‘a’-‘z’, ‘0’-‘9’, and underscore (‘_’).

Output
Output a list of the m songs with the highest quality qi, in decreasing order of quality. If two songs have the same quality, give precedence to the one appearing first on the album (presumably there was a reason for the producers to put that song before the other).

Sample input 1
4 2
30 one
30 two
15 three
25 four
Sample output 1
four
two
Sample input 2
15 3
197812 re_hash
78906 5_4
189518 tomorrow_comes_today
39453 new_genious
210492 clint_eastwood
26302 man_research
22544 punk
19727 sound_check
17535 double_bass
18782 rock_the_house
198189 19_2000
13151 latin_simone
12139 starshine
11272 slow_country
10521 m1_a1
Sample output 2
19_2000
clint_eastwood
tomorrow_comes_today
'''

from operator import itemgetter

str_input = raw_input() # input from stdin
n, m = map(int, str_input.split(' ')) # cast array of string to int

songs = [()] * n # empty data

for i in xrange(1, n + 1):
    str_input = raw_input() # input from stdin
    fi, si = str_input.split(' ')

    # wrong
    #zi = 1.0 / float(i)
    #qi = float(fi) / zi

    qi = float(i) * float(fi)
    songs[i - 1] = (qi, si)

sorted_songs = sorted(songs, key = itemgetter(0), reverse = True) # orderBy qi DESC

for i in xrange(m):
    print sorted_songs[i][1]
