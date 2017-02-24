#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from souwapy import SOUWA


def MakeArray(row):
    arr = [0 for i in range(row)]
    for i in range(0, row):
        arr[i] = [str(i + 1).zfill(7), 'a']
    return arr

ar = MakeArray(1234)
souwa = SOUWA.sou()
result = souwa.getcsvdata(ar, ",", "\n")
# You can see the result by displaying "result".
