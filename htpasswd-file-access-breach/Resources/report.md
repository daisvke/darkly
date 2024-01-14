# htpasswd-file-access-breach

## Vulnerability Details:

### Affected URL: `http://{IP_ADDR}/whatever`

### Issue Description:
During our investigation using DirB, we discovered a directory named `http://{IP_ADDR}/admin` and a `robots.txt` file using the following command:
```
// We use the 'i' option to be case insensitive
dirb http://{IP_ADDR} -i
```
The `robots.txt` file is a standard used by websites to provide guidance to web crawlers about which parts of the site should not be processed or analyzed.

### Potential Exploitation:
Upon accessing the `robots.txt` file, we observed that it was blocking file access to a directory named `whatever/`. Further exploration of this directory revealed a file named `htpasswd` that was downloadable. This file contained sensitive information, specifically the access credentials for a user named 'root':
```
$ cat htpasswd
root:437394baff5aa33daa618be47b75cb49
```
Subsequently, we utilized these credentials to gain unauthorized access to the admin page at `http://{IP_ADDR}/admin`, ultimately retrieving the flag.

## Immediate Action Required:
* Change the compromised password.
* Remove the file from the directory
