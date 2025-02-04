#!/usr/bin/python3
"""
working with log parsing
"""

import sys
import re


def output(log: dict) -> None:
    """
    working with helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for kode in sorted(log["code_frequency"]):
        if log["code_frequency"][kode]:
            print("{}: {}".format(kode, log["code_frequency"][kode]))


if __name__ == "__main__":
    regex = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8

    ln_cnt = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {
        str(kode): 0 for kode in [
            200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if (match):
                ln_cnt += 1
                kode = match.group(1)
                file_size = int(match.group(2))


                log["file_size"] += file_size

                if (kode.isdecimal()):
                    log["code_frequency"][kode] += 1

                if (ln_cnt % 10 == 0):
                    output(log)
    finally:
        output(log)