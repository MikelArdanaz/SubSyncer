#!/usr/bin/env python3
import argparse
from argparse import RawTextHelpFormatter
import datetime
import os
import re
import sys


class SubSyncer:
    SUB_TIME_FORMAT = "(\d{2}:\d{2}:\d{2},\d{3}) \-\-> "\
        "(\d{2}:\d{2}:\d{2},\d{3})"

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='A dummy tool to help you to sync subtitles\nMade by @mikelillo_1 \nGitHub: MikelArdanaz', formatter_class=RawTextHelpFormatter)
        parser.add_argument('subtitle', metavar='subtitle.srt', type=str,
                            help='The .srt file with the subtitle')
        parser.add_argument('delay', metavar='SECONDS', type=int,
                            help='Seconds to delay (positive value) or speed (negative value) the dialogues of the subtitle')
        parser.add_argument('-s', '--start', metavar='INITIAL_TIME',
                            help='Position in which you want the tool to start delaying or speeding the dialogues of the subtitle. Format is [H]H:MM:SS Default: 00:00:00')
        args = parser.parse_args()
        self.input_file = args.subtitle
        self.input_delay = args.delay
        if not os.path.isfile(self.input_file):
            parser.error('{} does not exist'.format(self.input_file))
        self.output_temp = '{}_tmp.srt'.format(os.path.splitext(self.input_file)[0])
        # Check if optional argument is set
        if args.start is not None:
            if(re.match('(\d{1,2}:)+(\d{2}:)+(\d{2})$', args.start) is None):
                parser.error(
                    '{} is not a valid offset, format is [H]H:MM:SS'.format(args.start))
            self.start_time=datetime.datetime.strptime(args.start, '%H:%M:%S')
        else:
            self.start_time=datetime.datetime.strptime('00:00:00', '%H:%M:%S')  # Default value
        # $ Matches the end of the string

        self.syncsub()

    def syncsub(self):
        with open(self.input_file, 'r') as _input:
            with open(self.output_temp, 'w') as output:
                for line in _input:
                    parsed=re.search(self.SUB_TIME_FORMAT, line)
                    if parsed:
                        inicio,fin=(parsed.group(1),parsed.group(2))#https://docs.python.org/2/howto/regex.html#grouping
                        dt=datetime.datetime.strptime(inicio, '%H:%M:%S,%f')# %f->Microseconds not miliseconds
                        if dt >= self.start_time:
                            dt+=datetime.timedelta(seconds=self.input_delay)
                            dt=dt.strftime('%H:%M:%S,%f')[:-3] #Microseconds to miliseconds
                            finaldt=datetime.datetime.strptime(fin, '%H:%M:%S,%f')# %f->Microseconds not miliseconds
                            finaldt+=datetime.timedelta(seconds=self.input_delay)
                            finaldt=finaldt.strftime('%H:%M:%S,%f')[:-3] #Microseconds to miliseconds
                            output.write('{} --> {}\n'.format(dt,finaldt))
                        else:
                            output.write(line)
                    else:
                        output.write(line)
        os.rename(self.output_temp,self.input_file)

if __name__ == '__main__':
    SubSyncer()
