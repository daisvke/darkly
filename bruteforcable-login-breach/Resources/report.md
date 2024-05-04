# bruteforcable-login-breach

## Vulnerability Discovery:

### Affected URL: `http://{IP_ADDR}/index.php?page=signin`

### Issue Description:
We discovered a potential security vulnerability related to the authentication mechanism. It appears that the login functionality is susceptible to brute force attacks due to inadequate password strength enforcement.

## Exploitation Strategy:

### Bruteforce Login Using OWASP's 10k-Worst-Passwords:
We conducted a bruteforce attack on the login page using OWASP's 10k-worst-passwords wordlist available at [OWASP GitHub repository](https://github.com/OWASP/passfault/blob/master/wordlists/wordlists/10k-worst-passwords.txt) with the assistance of `Burp Intruder`. It took only 17 attempts to successfully login, thereby revealing the flag. <br />
We identified the successful login by observing that the response length was longer for the password 'shadow' used along with the username 'admin', indicating a successful authentication.

## Immediate Action Required:
- **Password Strength Enforcement**: Implement robust password policies that enforce stronger password requirements, including complexity and length criteria, to mitigate the risk of brute force attacks.
  
- **Account Lockout Mechanism**: Implement an account lockout mechanism to prevent repeated login attempts after a certain number of failed logins, thereby thwarting brute force attacks.
  
- **Monitoring and Logging**: Implement comprehensive monitoring and logging mechanisms to detect and alert on anomalous login attempts, enabling proactive response to potential security breaches.

Additionally, to enhance security further, consider implementing a random response length mechanism upon failed login attempts. This would make it more challenging for attackers to determine successful login attempts solely based on response length, thereby increasing the overall resilience of the authentication system.