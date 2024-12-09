# Environment
Python 3.12
package:
- requests
- urlib3

# Description
The python script will do the following thing:
- read .m3u8 playlist to retrieve list of video chunks
- download those video chunks from resources server
- save downloaded video into 'cache' folder

Please be noticed that the script do not merge video chunks into a single video file. You need to do it yourself with other method (e.g. ffmpeg)
