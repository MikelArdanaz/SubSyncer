# Subsyncer  
A dummy tool to help you to sync subtitles  
## Usage
```bash
$ ./subsyncer.py [-h] [-s INITIAL_TIME] subtitle.srt SECONDS
```
### Examples
```
positional arguments:
  subtitle.srt          The .srt file with the subtitle
  SECONDS               Seconds to delay (positive value) or speed (negative value) the dialogues of the subtitle

optional arguments:
  -h, --help            show this help message and exit
  -s INITIAL_TIME, --start INITIAL_TIME
                        Position in which you want the tool to start delaying or speeding the dialogues of the subtitle. Format is [H]H:MM:SS Default: 00:00:00
```
Add a 1 second offset to the subtitles
```bash
$ ./subsyncer.py MrRobotS03E04.srt 1  
```
Adds a 3 second offset to the dialogues that appear after the 13 minute 13 second
```bash  
$ ./subsyncer.py -s 00:13:13 MrRobotS03E04.srt 3
```
