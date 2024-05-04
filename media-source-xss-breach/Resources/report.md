# media-source-xss-breach

## Vulnerability Discovery:

### Affected URL: `http://{IP_ADDR}/index.php?page=media&src=`

### Issue Description:
We identified a critical Cross-Site Scripting (XSS) vulnerability. The vulnerability is located in the `src` parameter of the `media` page, which accepts user input without proper validation or sanitization.
<br /><br />
By injecting a specially crafted payload into the `src` parameter, an attacker can execute arbitrary JavaScript code within the context of the vulnerable web page. This could lead to various malicious activities, including session hijacking, phishing attacks, defacement, or theft of sensitive user information.

### Proof of Concept:
Payload used: `<script>alert()</script>`<br />
Encoded Base64 payload: `PHNjcmlwdD5hbGVydCgpPC9zY3JpcHQ+`<br />
We get the flag when accessing `http://{IP_ADDR}/index.php?page=media&src=PHNjcmlwdD5hbGVydCgpPC9zY3JpcHQ+`

## Immediate Action Required:
- Input Validation and Sanitization: Implement strict input validation and sanitization mechanisms to prevent the execution of arbitrary JavaScript code. Validate and filter input received through URL parameters to ensure that it adheres to expected patterns and does not contain executable code.
- Output Encoding: Encode user-generated content before rendering it in HTML output to prevent script execution. Use appropriate encoding techniques such as HTML entity encoding or Content Security Policy (CSP) to mitigate XSS vulnerabilities.
- Content Security Policy (CSP): Implement and enforce a robust CSP to restrict the sources from which content can be loaded, thereby reducing the impact of XSS attacks.