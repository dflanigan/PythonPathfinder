#! /usr/bin/env python

import random


colors = ['red','blue','yellow']

samples = {}
for color in colors:
    samples[color] = 0

for count in range(100):
    #value = random.sample(colors,1)[0]
    value = colors[random.randint(0,len(colors) - 1)]
    samples[value] += 1

print samples


