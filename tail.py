#!/usr/bin/env python

import os


def tail(filename, number_lines):
    """
    Simple tail function
    """
    buff = 4096
    lines = []

    file_size = os.stat(filename).st_size

    with open(filename, 'r') as fh:

        if buff > file_size:
            buff = file_size

        fh.seek(0, os.SEEK_END)
        position = fh.tell()

        while position > 0:
            position -= buff

            fh.seek(position)

            content = fh.read()

            if not content:
                break

            if content.count('\n') > number_lines:
                content = content[content.index('\n') + 1:].splitlines()
                for line in content[-number_lines:]:
                    lines.append(line)
                return lines

    return content.splitlines()


if __name__ == '__main__':

    print('\n'.join(tail('/etc/passwd', 5)))
    print('\n'.join(tail('/etc/redhat-release', 5)))
