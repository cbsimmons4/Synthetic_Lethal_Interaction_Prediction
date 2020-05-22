import os
import sys
import json
from subprocess import call


def read_config(config_fname):
    try:
        with open(config_fname, 'r') as data_file:
            config = json.load(data_file)

        return config 
    except:
        print ('Specified config not found, using default values')
        return dict()


def get_cmd(config):
    i = config['i'] if 'i' in config else 'input.edgelist' # custom default
    o = config['o'] if 'o' in config else 'output.emb' 
    d = config['d'] if 'd' in config else 2 
    l = config['l'] if 'l' in config else 80  # rest of defaults taken from node2vec docs
    r = config['r'] if 'r' in config else 10
    k = config['k'] if 'k' in config else 10
    e = config['e'] if 'e' in config else 1
    p = config['p'] if 'p' in config else 1
    q = config['q'] if 'q' in config else 1
    v = 'v' in config
    dr = 'dr' in config
    w = 'w' in config
    ow = 'ow' in config

    cmd = './node2vec -i:%s -o:%s -d:%d -l:%d -r:%d -k:%d -e:%d -p:%d -q:%d' % (i, o, d, l, r, k, e, p, q)

    if v:
        cmd += ' -v'

    if dr:
        cmd += ' -dr'

    if w:
        cmd += ' -w'

    if ow:
        cmd += ' -ow'

    return cmd


def call_cmd(cmd):
    call(cmd.split())


def main(config_fname):
    config = read_config(config_fname)
    cmd = get_cmd(config)
    call_cmd(cmd)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        main('bs')
    else:
        main(sys.argv[1])



