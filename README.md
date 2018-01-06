# Subsyncer  
A dummy tool to help you to sync subtitles  
## Usage
```bash
$ ./subsyncer.py [-h] [-s INITIAL_TIME] subtitle.srt SECONDS
```
### Examples
Add a 1 second offset to the subtitles
```bash
$ ./subsyncer.py MrRobotS03E04.srt 1  
```
Adds a 3 second offset to the dialogues that appear after the 13 minute 13 second
```bash  
$ ./subsyncer.py -s 00:13:13 MrRobotS03E04.srt 3
```
Help
```bash
$ ./subsyncer.py -h
```
