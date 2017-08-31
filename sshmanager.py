#!/usr/bin/env python3
import json
from pathlib import Path
from subprocess import call


class Color(object):
    BLUE = '\033[94m'
    END = '\033[0m'


def main():
    config_path = Path.home().joinpath('.ssh-servers.json')

    with open(str(config_path)) as f:
        servers = json.load(f)

    for i, server in enumerate(servers):
        print(Color.BLUE, i + 1, Color.END, "{}@{}:{}".format(server['user'], server['host'], server['port']))

    print('\nCan I have your number?\n> ', end='')
    choice = servers[int(input()) - 1]
    call(['ssh', '-l', choice['user'], '-p', str(choice['port']), choice['host']])


if __name__ == '__main__':
    main()
