# hidden-directory-breach

## Vulnerability Details:

### Affected URL: `http://{IP_ADDR}/.hidden`

### Issue Description:
During our investigation using DirB, we discovered a `robots.txt` file using the following command:
```
// We use the 'i' option to be case insensitive
dirb http://{IP_ADDR} -i
```
The `robots.txt` file is a standard used by websites to provide guidance to web crawlers about which parts of the site should not be processed or analyzed.

### Potential Exploitation:
Upon accessing the `robots.txt` file, we observed that it was blocking file access to a directory named `.hidden/`.<br/>
This directory includes a series of links, each leading to another set of links. Within each of these links, a `README` file is present, containing a message. The objective was to locate the flag within one of these readme files.<br />
To achieve this, a Python script was crafted (`readme-scrapper.py`) to recursively access all the links and open each readme file. The script then transferred the outputs to a designated output file, and subsequently, the term 'flag' was searched using grep from that file to obtain the flag:
```
cat out | grep flag
Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
```
