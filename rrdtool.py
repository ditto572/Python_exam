# -*- coding: utf-8 -*-
import rrdtool

def create():
    data_sources = [
        'DS:load1:GAUGE:600:0:U',
        'DS:load5:GAUGE:600:0:U',
        'DS:load15:GAUGE:600:0:U',
    ]
    rras = [
        'RRA:AVERAGE:0.5:1:600',
        'RRA:AVERAGE:0.5:6:700',
        'RRA:AVERAGE:0.5:24:775',
        'RRA:AVERAGE:0.5:288:797',
        'RRA:MAX:0.5:1:600',
        'RRA:MAX:0.5:6:700',
        'RRA:MAX:0.5:24:775',
        'RRA:MAX:0.5:288:797',
        'RRA:MIN:0.5:1:600',
        'RRA:MIN:0.5:6:700',
        'RRA:MIN:0.5:24:775',
        'RRA:MIN:0.5:288:797',
    ]

    rrdtool.create('pyload.rrd',
                   '--step', '300',
                   data_sources,
                   rras)

def main():
    create()

if __name__ == '__main__':
    main()
