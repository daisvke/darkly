# session-hijacking-breach

## Vulnerability Details:

### Issue Description:
This security issue pertains to a vulnerability in the handling of cookies within the website:<br />
<br />
From the browser's inspector, navigate to the storage tab of the navigator. There, you'll find an MD5-like value, which is `68934a3e9455fa72420237eb05902327`. <br />
Decrypting this hash using a tool like https://md5decrypt.net/ reveals the word `false`. Given that the cookie name is `i_am_admin`, the inspector shows:
```
cookie_name   |   cookie_value
i_am_admin         false
```
We can therefore deduce that obtaining the MD5 hash of the string `true` (specifically, `b326b5062b2f0e69046810717534cb09`) and replacing the current value with it would likely grant access to the admin session.<br />
<br />
Upon reloading, an alert window appears, providing us with the flag.

### Potential Exploitation:
Once an attacker obtains the session information, he can impersonate the user and gain unauthorized access to the user's account or system.

## Immediate Actions Required:
* Cookie Handling Mechanism:
Immediately review and strengthen the cookie handling mechanism.
Implement stronger encryption or hashing algorithms to secure cookie values.

* Authentication Process:
Enhance the overall session management and authentication processes.
Implement additional layers of authentication or authorization checks.
