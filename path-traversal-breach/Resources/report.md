# path Traversal Breach

## Vulnerability Details:

### Affected URL: `http://{IP_ADDR}/?page=`

### Issue Description:
During our investigation using path traversal techniques, we discovered a vulnerability on the webpage accessible via the affected URL. The application is susceptible to a path traversal attack, allowing an attacker to read arbitrary files from the server's filesystem.

### Potential Exploitation:
By manipulating the page parameter in the URL, an attacker can traverse the directory structure beyond the intended scope and access sensitive files on the server. In our case, we were able to reveal the contents of the /etc/passwd file, which should contain user account information, including system usernames.

To exploit this vulnerability, a Python script named `path-traversal.py` was crafted to automate the path traversal attack. The script iterates through various directory traversal patterns to locate and read the /etc/passwd file.

## Documentation
https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/path-traversal-apprentice/file-path-traversal/reading-arbitrary-files-via-path-traversal