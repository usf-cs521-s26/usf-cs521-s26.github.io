#!/usr/bin/env python3

from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
import sys

def main():
    if len(sys.argv) != 4:
        print('Usage: ./mkposts.py start-date end-date #sections')
        print('For example: ./mkposts.py 2025-01-21 2025-05-08 2')
        return

    start_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')
    end_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')
    sections = int(sys.argv[3])

    # start_date = datetime.strptime('2025-01-21', '%Y-%m-%d')
    # end_date = datetime.strptime('2025-05-08', '%Y-%m-%d')

    while start_date <= end_date:
        match start_date.weekday():
            case 1 | 2 | 3:  # Tue | Wed | Thu
                post_time = datetime(
                    start_date.year, 
                    start_date.month, 
                    start_date.day,
                    8, 0, 0, tzinfo=ZoneInfo("America/Los_Angeles")
                )
                fname = start_date.strftime('%Y-%m-%d') + '-post.md'
                with open(fname, 'w') as f:
                    f.write('---\n')
                    f.write('layout: post\n')
                    f.write('topics: \n')
                    f.write('date: ' + post_time.strftime('%Y-%m-%d %H:%M:%S %z') + "\n")
                    for s in range(sections):
                        ss = str(s+1)
                        f.write('notes' + ss + ': \n') 
                        f.write('code' + ss + ': \n')
                        f.write('video' + ss + ': \n') 
                    f.write('category: unfiled\n')
                    f.write('published: false\n')
                    f.write('---\n')
        start_date += timedelta(days=1)
    return

if __name__ == '__main__':
    main()
