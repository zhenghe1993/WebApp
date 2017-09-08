# -*- coding:utf-8 -*-

from Instant_mark.utils import blocks

with open("../Instant_mark/text.txt", "r") as f:
    for line in blocks(f):
        print("blocks --- {}".format(line))


